'''
    IMPORTS
'''

# temporary fix for the bug described here: https://bugs.python.org/issue45681
# a permananet fix has already been issued but was not included in python 3.10 for some reason
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(ctypes.c_int(0))
except:
    pass

import tkinter as tk # gui
from fuzzywuzzy import fuzz # fuzzy string comparison
import pyperclip, pyautogui # clipboard
import tempfile, pathlib, json, urllib.request # remote quiz data and caching
import threading

'''
    QUIZ DATA
'''
QUIZ_DATA = None # None = not ready, False = download failed
def get_quiz_data():
    global QUIZ_DATA
    
    # first things first, find our local copy
    current_file_data = None
    filepath = pathlib.Path(tempfile.gettempdir()) / "Wizard101Trivia_quizdata.json"
    try:
        with open(filepath, "r") as f:
            current_file_data = json.load(f)
        
        assert "quiz_data" in current_file_data
        assert "version" in current_file_data
    except:
        # if anything goes wrong, then the file doesn't exist or is invalid
        current_file_data = None
    
    # set QUIZ_DATA to current information
    # so the program can get to work ASAP
    if current_file_data:
        QUIZ_DATA = current_file_data["quiz_data"]
    
    # get remote version
    remote_url = "https://raw.githubusercontent.com/GabeMillikan/Wizard101Trivia/main/"
    try:
        remote_version = urllib.request.urlopen(remote_url + "quiz_data/version.txt").read()
        remote_version = remote_version.decode().strip()
    except:
        if not current_file_data:
            QUIZ_DATA = False # download failed
        raise
    
    # get remote data
    if not current_file_data or current_file_data["version"] != remote_version:
        try:
            remote_quizzes = json.load(urllib.request.urlopen(remote_url + "quiz_data/quizzes.json"))
        except:
            if not current_file_data:
                QUIZ_DATA = False # download failed
            raise
        
        QUIZ_DATA = remote_quizzes
        
        with open(filepath, "w") as f:
            json.dump({"quiz_data": remote_quizzes, "version": remote_version}, f)

threading.Thread(target = get_quiz_data).start()

'''
    THE GUI
'''
window = tk.Tk()
window.title("github.com/GabeMillikan/Wizard101Trivia")
window.columnconfigure(0, weight = 1)

# top
top_frame = tk.Frame()

description = tk.Label(master = top_frame, text = "This program reads from your clipboard. Copy the question to get the answer.", justify = "left")
description.grid(row = 0, sticky = "w")

autocopy = tk.ttk.Checkbutton(master = top_frame, text = "Automatically copy selected text.", takefocus = 0)
autocopy.grid(row = 1, sticky = "w")

top_frame.grid(column = 0, sticky = "w", padx = 8, pady = 8)

# bottom
separator = tk.ttk.Separator(window, orient = 'horizontal')
separator.grid(column = 0, row = 1, sticky = "ew")

output = tk.Label(window, text = "Nothing was found.", justify = "left")
output.grid(column = 0, row = 2, sticky = "w", padx = 8, pady = 8)

'''
    THE AUTO-COPY AND SEARCH ALGO
'''

# cycle through until autocopy is on
while "selected" not in autocopy.state():
    autocopy.invoke()

# then turn it off
autocopy.invoke()

# calls a function at a set interval (immediate initial call) 
def periodic(milliseconds = 1000):
    def decorator(user_func):
    
        def looper():
            window.after(milliseconds, looper)
            user_func()
            
        looper()
    
    return decorator

# presses ctrl+c if autocopy is enableed
@periodic(milliseconds = 50)
def attempt_autocopy():
    if "selected" not in autocopy.state():
        return
    
    # needs to happen in a separate thread because pyautogui 
    # has a bunch of delays that mess up the Tk event loop
    threading.Thread(
        target = pyautogui.hotkey,
        args = ("ctrl", "c")
    ).start()

# returns a list of [score, quiz_name, answer] pairs based on a given query
def find_matching_question(query_question):
    results = [] # stores [score, quiz_name, answer]
    
    for (quiz_name, quiz_questions) in QUIZ_DATA.items():
        for [quiz_question, answer] in quiz_questions:
            score = fuzz.ratio(query_question, quiz_question) / 100.0
            
            # don't add unless better than the current worst result
            if len(results) < 3 or score > results[-1][0]:
            
                result = [score, quiz_name, answer]
                
                # find insertion point, right before the first one with a lower score
                found_insertion = False
                for i in range(len(results)):
                    if results[i][0] < score:
                        found_insertion = True
                        results.insert(i, result)
                        break
                
                if not found_insertion:
                    results.append(result)
                
                results = results[:3] # truncate fourth item
    
    return results

# main operation, reads from clipboard and places the output in the window
last_searched_question = ""
@periodic(milliseconds = 10)
def update():
    global last_searched_question
    
    if QUIZ_DATA is None:
        output["text"] = "Downloading quiz answers..."
        return
    elif QUIZ_DATA is False:
        output["text"] = "Download failed\nYou must have internet for the very first run\nMake sure that your firewall isn't blocking Python"
        return
    
    pasted = pyperclip.paste()
    if last_searched_question == pasted:
        return
    
    last_searched_question = pasted
    
    results = find_matching_question(pasted)
    output["text"] = "\n".join(f"{score*100:.0f}% - [{quiz_name}] - {answer}" for [score, quiz_name, answer] in results)


# RUN
window.resizable(False, False)
window.attributes('-topmost',True)
window.mainloop()