# Wizard101Trivia
Easily answer wizard101 trivia questions

<img alt="preview" src="https://i.imgur.com/S8Wvay8.gif">

# Notes
- I wrote this program in October, and am only publishing it on GitHub now in december
- If you disable the "Auto Spam Ctrl+C" option (see section below), then this should theoretically be impossible to detect by the Kingsisle website. Because from their point of view, you're simply copying the question, then as far as they know probably googling it, then clicking the answer.
- I have only tested this program on windows 10, but I believe that it should work on older windows versions and probably on MacOS or Linux distributions.
- If you want to add support for a new quiz, then look at the code around line 12 where it says `QUIZ_ANSWERS = {`, and hopefully you can notice that there is a pattern. You're welcome to expand the list.

# What is "Auto Spam Ctrl+C"
- It's exactly what it says, it will press the "Control" and "C" keys every 0.1 seconds.
- This means that it will automatically copy any text that you highlight, which is nice because then you don't have to do it yourself.
- The drawback is that Kingsisle might notice that you press those keys every exactly 0.1 seconds, which might seem a bit suspicious considering that most people don't constantly spam Ctrl+C unless they're a robot. 

# How to Install
1. Download python from https://www.python.org/downloads/ (it's the big yellow button)
2. Install it, if you're on windows, make sure to check this box at the bottom of the first screen of the installer:
    - <img alt="Add Python to PATH" src="https://i.imgur.com/hLaUKge.png">
3. If any of the steps after this don't work, you might need to restart your computer and start back at step 4
4. Open a command prompt or terminal (it is important to open it AFTER step 2 is complete)
    - How to do it on Windows: https://www.youtube.com/watch?v=uE9WgNr3OjM
    - How to do it on MacOS: https://www.youtube.com/watch?v=zw7Nd67_aFw
    - I imagine if you're on Linux you already know how (or just google it for your specific version)
5. For each bullet point, copy/paste it into the console, then press enter. Wait for it to finish, then paste the next one.
    - python -m pip install pyperclip
    - python -m pip install pyautogui
    - python -m pip install PyQt5
6. Download the file in this github page and save it as "trivia.pyw"
    - Here's a direct link to the code: https://raw.githubusercontent.com/GabeMillikan/Wizard101Trivia/main/trivia.pyw
    - You may just right click and press "Save" once you're at the above link
    - Otherwise, create a file named "trivia.pyw" on your computer, then edit it with a text editor (ex: notepad) and copy/paste the whole code into it
    - Be careful to make sure that the file is called "trivia.pyw" and not "trivia.pyw.txt" or "trivia.pyw.py"
7. Double click the file, or open it with python (which was installed in step 2)
    - If the window does not open, or something does not work, feel free to message me.

# How to Use
1. Run the program
2. Go to your favorite Wizard101 trivia from the supported list below
3. Copy the question (or enable Auto Spam Ctrl+C and just highlight it)
4. Select the answer provided

# Supported Quizzes (as of December 19, 2020)
 * Supported very well:
     - World Capitals
     - Weather
     - State Nicknames
     - State Capitals
     - State Birds
     - State Animals
     - Solar System
     - Primates
     - Norse Mythology
     - Landforms
     - Heart
     - Habitats
     - Greek Mythology
     - Famous World Leaders
     - Famous Poets
     - Famous Authors
     - Early American History
     - Dinosaur
     - Constellations
     - Chemical Elements
     - Book Quotes
     - Big Cats
     - Apollo Missions
     - Ancient Egypt
     - American Presidents
 * Supported but a bit buggy:
     - Spelling & Advanced Spelling (because all the questions are identical)
     - 9th, 10th, 11th and 12th Grade Vocabulary (because the questions are very short; 1 word)
     - English Punctuation (some questions are identical)
     
