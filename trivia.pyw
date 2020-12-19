import pyautogui
import pyperclip
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading

FONT = QFont('Arial', 14)

QUIZ_ANSWERS = {
    "English Punctuation Trivia": [
        ["Where does the period go in a sentence?", "At the end"],
        ["What is the apostrophe's main function?", "Show ownership or posession"],
        ["Which sentence uses a semi-colon correctly?", "I set out on a quest; the enemies looked fierce."],
        ["Which sentence below uses a comma correctly?", "Before you begin, let us learn to play."],
        ["An exclamation mark is often used to express what?", "Excitement"],
        ["Which sentence correctly uses an apostrophe?", "The horse's tail is so pretty."],
        ["Which sentence below uses a comma(s) correctly?", "Megan who lives next door, loves dogs."],
        ["Which sentence correctly uses an apostrophe?", "I can't do it, because it is too hard."],
        ["A semi-colon is primarily used to:", "Connect two unrelated phrases"],
        ["Quotation marks are used to do what?", "Show speech"],
        ["A period is also used to __________ words.", "Abbreviate"],
        ["Which sentence uses quotation marks correctly?", "Sally said, \"It's time to cook dinner.\""],
    ],
    "Advanced Spelling": [
        ["Which word is spelled correctly?", "autochthonous"],
        ["Which word is spelled correctly?", "Czechoslovakia"],
        ["Which word is spelled correctly?", "elucubrate"],
        ["Which word is spelled correctly?", "esquamulose"],
        ["Which word is spelled correctly?", "eudaemonic"],
        ["Which word is spelled correctly?", "euonym"],
        ["Which word is spelled correctly?", "insouciant"],
        ["Which word is spelled correctly?", "Laodicean"],
        ["Which word is spelled correctly?", "logorrhea"],
        ["Which word is spelled correctly?", "Presbyterian"],
        ["Which word is spelled correctly?", "prospicience"],
        ["Which word is spelled correctly?", "smaragdine"],
        ["Which word is spelled correctly?", "spoliator"],
        ["Which word is spelled correctly?", "vivisepulture"]
    ],
    "American Presidents": [
        ["Who was the 1st president of the United States?", " George Washington"],
        ["Who was the 2nd president of the United States?", "John Adams"],
        ["Who was the 3rd president of the United States?", "Thomas Jefferson"],
        ["Who was the 4th president of the United States?", "James Madison"],
        ["Who was the 5th president of the United States?", "James Monroe"],
        ["Who was the 6th president of the United States?", "John Quincy Adams"],
        ["Who was the 7th president of the United States?", "Andrew Jackson"],
        ["Who was the 8th president of the United States?", "Martin Van Buren"],
        ["Who was the 9th president of the United States?", "William Henry Harrison"],
        ["Who was the 10th president of the United States?", "John Tyler"],
        ["Who was the 11th president of the United States?", "James K. Polk"],
        ["Who was the 12th president of the United States?", "Zachary Taylor"],
        ["Who was the 13th president of the United States?", "Millard Fillmore"],
        ["Who was the 14th president of the United States?", "Franklin Pierce"],
        ["Who was the 15th president of the United States?", "James Buchanan"],
        ["Who was the 16th president of the United States?", "Abraham Lincoln"],
        ["Who was the 17th president of the United States?", "Andrew Johnson"],
        ["Who was the 18th president of the United States?", "Ulysses S. Grant"],
        ["Who was the 19th president of the United States?", "Rutherford B. Hayes"],
        ["Who was the 20th president of the United States?", "James A. Garfield"],
        ["Who was the 21st president of the United States?", "Chester A. Arthur"],
        ["Who was the 22nd president of the United States?", "Grover Cleveland"],
        ["Who was the 23rd president of the United States?", "Benjamin Harrison"],
        ["Who was the 24th president of the United States?", "Grover Cleveland"],
        ["Who was the 25th president of the United States?", "William McKinley"],
        ["Who was the 26th president of the United States?", "Theodore Roosevelt"],
        ["Who was the 27th president of the United States?", "William Howard Taft"],
        ["Who was the 28th president of the United States?", "Woodrow Wilson"],
        ["Who was the 29th president of the United States?", "Warren G. Harding"],
        ["Who was the 30th president of the United States?", "Calvin Coolidge"],
        ["Who was the 31st president of the United States?", "Herbert Hoover"],
        ["Who was the 32nd president of the United States?", "Franklin D. Roosevelt"],
        ["Who was the 33rd president of the United States?", "Harry S. Truman"],
        ["Who was the 34th president of the United States?", "Dwight D. Eisenhower"],
        ["Who was the 35th president of the United States?", "John F. Kennedy"],
        ["Who was the 36th president of the United States?", "Lyndon B. Johnson"],
        ["Who was the 37th president of the United States?", "Richard Nixon"],
        ["Who was the 38th president of the United States?", "Gerald Ford"],
        ["Who was the 39th president of the United States?", "Jimmy Carter"],
        ["Who was the 40th president of the United States?", "Ronald Reagan"],
        ["Who was the 41st president of the United States?", "George W. H. Bush"],
        ["Who was the 42nd president of the United States?", "Bill Clinton"],
        ["Who was the 43rd president of the United States?", "George W. Bush"],
        ["Who was the 44th president of the United States?", "Barack Obama"]
    ],
    "Ancient Egypt": [
        ["A Pharaoh never let his ______ be seen.", "Hair"],
        ["Because they believed in ________, ancient Egyptians mummified bodies.", "the afterlife"],
        ["How many pyramids have been discovered in Egypt so far?", "Over 130"],
        ["Roughly how many different deities did the Ancient Egyptians believe in?", "More than 2,000"],
        ["The Ancient Egyptians were the first civilization to invent __________.", "Writing"],
        ["The Egyptian alphabet consisted of more than ______ hieroglyphs.", "700"],
        ["The famous Great Sphinx is missing what part?", "Nose"],
        ["What did Ancient Egyptians believe made the Nile River overflow every year?", "The tears of Isis"],
        ["What is the largest pyramid in Egypt?", "Pyramid of Khufu"],
        ["What is the name of the most popular board game developed by Ancient Egyptians?", "Senet"],
        ["What type of animal did Ancient Egypt not typically keep as a pet?", "Hippo"],
        ["When did the Ancient Egyptian Empire begin to weaken?", "700 BC"],
        ["Which empire was the first to conquer the Ancient Egyptians?", "Assyrian Empire"],
        ["Which is not considered a phase of the Ancient Egyptian society?", "Glorious Kingdom"],
        ["Which of the following was a calendar not followed by the Ancient Egyptians?", "Animal Calendar"],
        ["Which of these animals considered sacred by Ancient Egyptians?", "Cat"],
        ["Who is considered to be the first Pharaoh of Egypt?", "King Menes"],
        ["Who is considered to be the most important Egyptian god?", "Ra"]
    ],
    "Apollo Missions": [
        ["In which mission did an astronaut perform a golf shot on the moon?", "Apollo 14"],
        ["This Apollo mission never launched and ended in tragedy, when a fire erupted in the command module during a test and killed three astronauts.", "Apollo 1"],
        ["Which astronaut was not present on the Apollo 11 mission?", "Cernan"],
        ["Which mission cancelled their landing on the moon due to technical problems?", "Apollo 13"],
        ["Which mission conducted the first manned flight test of the Lunar Module?", "Apollo 9"],
        ["Which mission had a SM oxygen tank explode, which caused many problems?", "Apollo 13"],
        ["Which mission had two lightning strikes to the spacecraft during launch?", "Apollo 12"],
        ["Which mission provided the first color video images from the surface of the moon?", "Apollo 14"],
        ["Which mission sent broadcasted some of the first live television pictures from space?", "Apollo 8"],
        ["Which mission used the Lunar RV for the first time?", "Apollo 15"],
        ["Which mission was considered a \"dress rehearsal\" for a lunar landing?", "Apollo 10"],
        ["Which mission was the first manned Apollo flight?", "Apollo 7"],
        ["Which mission was the first manned circumlunar flight?", "Apollo 8"],
        ["Which mission was the first manned landing on the moon?", "Apollo 11"],
        ["Which mission was the first night launch?", "Apollo 17"],
        ["Which was the last Apollo mission?", "Apollo 17"]
    ],
    "Big Cats": [
        ["A cheetah can run up to speeds of ____ miles an hour.", "70"],
        ["Big cats are ________.", "Carnivores"],
        ["How far can a lions's roar be heard from?", "5 miles"],
        ["One common way to determine what is considered a big cat, is a feline that can ________.", "Roar"],
        ["The main threats to big cats are ___________.", "poaching and habitat destruction"],
        ["Tigers are often poached for their parts, used in traditional ________ medicine.", "Chinese"],
        ["Which big cat is in the genus Acinonyx?", "Cheetah"],
        ["Which big cat is in the genus Puma?", "Cougar"],
        ["Which big cat is in the genus Uncia?", "Snow Leopard"],
        ["Which big cat is named from the Native American word meaning \"he who kills with one leap\"?", "Jaguar"],
        ["Which big cat is not in the genus Panthera?", "Cheetah"],
        ["Which is the best climber of all the big cats?", "Leopard"],
        ["Which is the most endangered big cat?", "Amur Leopard"],
        ["Which is the only big cat that lives in groups?", "Lion"],
        ["Which of the following is not a criteria for an accredited US Fish & Wildlife Service animal sanctuary?", "Must provide enrichment activities for big cats"],
        ["Which of the following is not considered a big cat?", "Bobcat"],
        ["Which of these big cats is an excellent swimmer who loves water?", "Tiger"],
        ["Which of these big cats purrs instead of roars?", "Cheetah"],
        ["Which of these lions are recently extinct?", "Barbary Lion"],
        ["Which type of tiger is extinct?", "Caspian Tiger"]
    ],
    "Book Quotes": [
        ["\"Call me Ishmael.\"", "Moby Dick"],
        ["\"I have been bent and broken, but - I hope - into a better shape.\"", "Great Expectations"],
        ["\"I'm not afraid of storms, for I'm learning how to sail my ship.\"", "Little Women"],
        ["\"In spite of everything I still believe that people are really good at heart\"", "The Diary of Anne Frank"],
        ["\"It was a pleasure to burn.\"", "Farenheit 451"],
        ["\"The sky above the port was the color of television, tuned to a dead channel.\"", "Neuromancer"],
        ["\"You don't know about me without you have read a book by the name of 'The Adventures of Tom Sawyer'; but that ain't no matter. That book was made by a Mr Mark Twain, and he told the truth, mainly.\"", "The Adventures of Huckleberry Finn"],
        ["\"All animals are equal, but some animals are more equal than others\"", "Animal Farm"],
        ["\"All grown-ups were once children\"but only few of them remember it.\"", "The Little Prince"],
        ["\"Anything worth dying for is certainly worth living for.\"", "Catch-22"],
        ["\"Don't ever tell anybody anything. If you do, you start missing everybody.\"", "The Catcher in the Rye"],
        ["\"I wanted you to see what real courage is, instead of getting the idea that courage is a man with a gun in his hand. It\"s when you know you\"re licked before you begin but you begin anyway and you see it through no matter what.\"", "To Kill a Mockingbird"],
        ["\"I was benevolent and good; misery made me a fiend. Make me happy, and I shall again be virtuous.\"", "Frankenstein"],
        ["\"It is to the credit of human nature that, except where its selfishness is brought into play, it loves more readily than it hates.\"", "The Scarlet Letter"],
        ["\"Most people were heartless about turtles because a turtle\"s heart will beat for hours after it has been cut up and butchered. But the old man thought, I have such a heart too.\"", "The Old Man and the Sea"],
        ["\"Not all those who wander are lost.\"", "The Lord of the Rings"]
    ],
    "Chemical Elements": [
        ["Most of the earth's atmosphere consists of this gas.", "N"],
        ["The symbol 'Au' refers to which chemical element?", "Gold"],
        ["The symbol 'Co' refers to which chemical element?", "Cobalt"],
        ["The symbol 'Cu' refers to which chemical element?", "Copper"],
        ["The symbol 'F' refers to which chemical element?", "Fluorine"],
        ["The symbol 'H' refers to which chemical element?", "Hydrogen"],
        ["The symbol 'Pb' refers to which chemical element?", "Lead"],
        ["The symbol 'S' refers to which chemical element?", "Sulfur"],
        ["This element give plants the energy they need to grow.", "P"],
        ["This element is the building block of life.", "C"],
        ["This element was discovered by Hans Christian Oersted in 1825.", "Al"],
        ["This element was discovered by Joseph Priestly and Carl Scheele in 1774.", "O"],
        ["This element was discovered in 1808.", "B"],
        ["This element when combined with Chlorine makes table salt.", "Na"],
        ["What is the symbol for Potassium?", "K"],
        ["Which element has a reddish color in a gas and liquid state?", "Br"],
        ["Which element has a silver-gray appearance?", "Zn"],
        ["Which of these elements is considered a Metal.", "Fe"],
        ["Which of these elements is NOT considered a Metalloid.", "Sn"],
        ["Which of these elements is NOT considered a Noble Gas.", "H"]
    ],
    "Constellations": [
        ["Aquila is a constellation named after what bird?", "Eagle"],
        ["Cancer is a constellation in the shape of what animal?", "Crab"],
        ["Canis Major is otherwise known as the Great _____.", "Dog"],
        ["Capricornus is in the shape of what mythical animal?", "Sea-Goat"],
        ["The Auriga constellation is in the shape of a __________.", "Charioteer"],
        ["The constellation Cygnus is in the shape of what bird?", "Swan"],
        ["The constellation Libra represents a ___________.", "Balance Scale"],
        ["The Gemini constellation represents _______.", "Twins"],
        ["The Lyra constellation is in the shape of a what?", "Harp"],
        ["This bright star in Auriga is yellow like our sun.", "Capella"],
        ["What is the brightest star in Cygnus?", "Deneb"],
        ["What is the brightest star in the Aquila constellation?", "Altair"],
        ["What is the brightest star in the Leo constellation?", "Regulus"],
        ["What is the brightest star in the Lyra constellation?", "Vega"],
        ["What is the brightest star in the Pegasus constellation?", "Markab"],
        ["What shape marks the Pegasus constellation?", "Great Square"],
        ["Which constellation can you find M44 or the \"Beehive Cluster\" in?", "Cancer"],
        ["Which constellation holds the brightest star in the north sky?", "Canis Major"],
        ["Which is the brightest star in the Aries constellation?", "Hamal"],
        ["Which is the brightest star in the Canis Major constellation?", "Sirius"]
    ],
    "Dinosaur": [
        ["Dinosaurs belonged to which group of animals?", "Reptiles"],
        ["In what era did dinosaurs live?", "Mesozoic"],
        ["In what period did the Coelophysis live?", "Late Triassic"],
        ["In what period did the Diplodocus live?", "Late Jurassic"],
        ["In what period did the Stegosaurus live?", "Late Jurassic"],
        ["In what period did the Triceratops live?", "Late Cretaceous"],
        ["In what period did the Tyrannosaurus live?", "Late Cretaceous"],
        ["The largest dinosaurs were __________________.", "Sauropods"],
        ["What caused the extinction of dinosaurs according to scientists?", "Scientists are not 100% sure. There is still heavy debate."],
        ["What does the name 'Triceratops' mean?", "three-horned face"],
        ["What does the word 'dinosaur' mean?", "Terrible Lizard"],
        ["What profession studies dinosaur fossils?", "Paleontologist"],
        ["When did dinosaurs become extinct?", "65 million years ago"],
        ["Which carnivorous dinosaur had teeth up to 8 inches long?", "Tyrannosaurus"],
        ["Which dinosaur had a long neck to help reach high and low vegetation?", "Diplodocus"],
        ["Which dinosaur had hollow limb bones?", "Coelophysis"],
        ["Which dinosaur most closely resembles a rhinoceros?", "Triceratops"],
        ["Which of the following was not a flying reptile?", "Stegosaurus"],
        ["Which of these is not a dinosaur?", "Pterodactyl"],
        ["Who coined the term 'dinosauria?'", "Sir Richard Owen"]
    ],
    "Early American History": [
        ["11 Southern states succeeded from the union in 1860 to form the _________ States of America.", "Confederate"],
        ["Francis Scott Key wrote which famous piece of American history?", "The Star Spangled Banner"],
        ["How long did the Civil War last?", "Four Years"],
        ["Most of the original American settlers were from what country?", "England"],
        ["President Thomas Jefferson made what large purchase to buy American a lot of new territory?", "Louisiana Purchase"],
        ["The American Revolution was against the ________, the English army.", "Red Coats"],
        ["This famous American colony is in modern Massachusetts.", "Plymouth"],
        ["This famous display against England's taxation threw a luxury item into the sea.", "Boston Tea Party"],
        ["What year did the British surrender in the American Revolution?", "1781"],
        ["What year was the Declaration of Independence signed?", "1776"],
        ["Where was President Abraham Lincoln assassinated?", "The Theatre"],
        ["Which early tax act made American settlers very angry pre-revolution?", "Stamp Act of 1765"],
        ["Which natural resource was a large reason many Americans choose to journey westward in the 1800's?", "Gold"],
        ["Which two amendments make up the Reconstruction Acts of 1867 and give African Americans additional freedoms?", "Fourteenth and Fifteenth"],
        ["Who did the United States purchase Alaska from?", "Russia"]
    ],
    "Eleventh Grade Vocabulary": [
        ["Allegory", "a representation of an abstract or spiritual meaning through concrete or material forms"],
        ["Ambiguity", "doubtfulness or uncertainty of meaning or intention"],
        ["Anecdote", "a short account of a particular incident or event of an interesting or amusing nature, often biographical."],
        ["Annotated", "supplied with or containing explanatory notes and textual comments"],
        ["Assuage", "to relieve or soothe"],
        ["Auspicious", "favorable, noteworthy"],
        ["Buoyancy", "the power to float or rise in a fluid, the upward pressure exerted by the fluid in which a body is immersed"],
        ["Conceit", "an excessively favorable opinion of one's own ability, importance or wit"],
        ["Conspicuous", "noticeable, obvious"],
        ["Denotation", "a word that names or signifies something specific"],
        ["Discern", "to recognize the difference"],
        ["Enigma", "a mystery"],
        ["Euphemism", "the substitution of a mild, indirect, or vague expression for one thought to be offensive, harsh, or blunt"],
        ["Principle", "a fundamental, primary, or general law or truth from which others are derived"],
        ["Procure", "to obtain"],
        ["Quandary", "a state of perplexity or uncertainty"]
    ],
    "English Punctuation": [
        ["A period is also used to __________ words.", "Abbreviate"],
        ["A semi-colon is primarily used to:", "Join two connected sentences"],
        ["An exclamation mark is often used to express what?", "Excitement"],
        ["Three periods in a row are called _________.", "Ellipses"],
        ["Where does the period go in a sentence?", "At the end"],
        ["Which of the following is NOT a reason to use an exclamation mark (!) ?", "Boredom"],
        ["Which sentence below uses a comma correctly?", "Before you begin, let us learn to play."],
        ["Which sentence below uses a comma correctly?", "I love to play video games, but they are hard."],
        ["Which sentence below uses a comma(s) correctly?", "Megan, who lives next door, loves dogs."],
        ["Which sentence correctly uses an apostrophe?", "The horse's tail is so pretty."],
        ["Which sentence uses a semi-colon correctly?", "I set out on a quest; the enemies looked fierce."],
        ["Which sentence uses quotation marks correctly?", "Sally said, \"It's time to cook dinner.\""],
        ["Which date below uses a comma correctly?", "January 1st, 2014"],
        ["Quotation marks are used to do what?", "Show speech"],
        ["What is the apostrophe's main function?", "Show ownership or posession"]
    ],
    "Famous Authors": [
        ["Who wrote 1984?", "George Orwell"],
        ["Who wrote A Clockwork Orange?", "Anthony Burgess"],
        ["Who wrote Animal Farm?", "George Orwell"],
        ["Who wrote Are You There God? It's Me, Margaret?", "Judy Blume"],
        ["Who wrote Atonement?", "Ian McEwan"],
        ["Who wrote Beloved?", "Toni Morrison"],
        ["Who wrote Catch-22?", "Joseph Heller"],
        ["Who wrote Gone with the Wind?", "Margaret Mitchell"],
        ["Who wrote Lolita?", "Vladimir Nabokov"],
        ["Who wrote Lord of the Flies?", "William Golding"],
        ["Who wrote Mrs. Dalloway?", "Virginia Woolf"],
        ["Who wrote Never Let Me Go?", "Kazuo Ishiguro"],
        ["Who wrote On the Road?", "Jack Kerouac"],
        ["Who wrote Slaughterhouse-Five?", "Kurt Vonnegut"],
        ["Who wrote The Catcher in the Rye?", "J.D. Salinger"],
        ["Who wrote The Grapes of Wrath?", "John Steinbeck"],
        ["Who wrote The Great Gatsby?", "F. Scott Fitzgerald"],
        ["Who wrote The Heart is a Lonely Hunter?", "Carson McCullers"],
        ["Who wrote The Lion, The Witch and the Wardrobe?", "C.S. Lewis"],
        ["Who wrote The Lord of the Rings?", "J.R.R. Tolkien"],
        ["Who wrote The Sound and the Fury?", "William Faulkner"],
        ["Who wrote The Sun Also Rises?", "Ernest Hemingway"],
        ["Who wrote Their Eyes Were Watching God?", "Zora Neale Hurston"],
        ["Who wrote Things Fall Apart?", "Chinua Achebe"],
        ["Who wrote To Kill a Mockingbird?", "Harper Lee"],
        ["Who wrote Watchmen?", "Alan Moore"]
    ],
    "Famous Poets": [
        ["Who wrote \"A Dream Within A Dream\"?", "Edgar Allan Poe"],
        ["Who wrote \"A Girl\"?", "Ezra Pound"],
        ["Who wrote \"Do Not Go Gentle To That Good Night\"?", "Dylan Thomas"],
        ["Who wrote \"Funeral Blues\"?", "W.H. Auden"],
        ["Who Wrote \"I Carry Your Heart With Me\"?", "E.E. Cummings"],
        ["Who wrote \"If those I loved were lost\"?", "Emily Dickinson"],
        ["Who Wrote \"If You Forget Me\"?", "Pablo Neruda"],
        ["Who wrote \"Life is Fine\"?", "Langston Hughes"],
        ["Who wrote \"Messy Room\"?", "Shel Silverstein"],
        ["Who wrote \"Phenomenal Woman\"?", "Maya Angelou"],
        ["Who wrote \"Stopping by the Woods on a Snowy Evening\"?", "Robert Frost"],
        ["Who wrote \"The Road Not Taken\"?", "Robert Frost"],
        ["Who wrote \"There is Another Sky\"?", "Emily Dickinson"],
        ["Who wrote \"To You\"?", "Walt Whitman"],
        ["Who wrote \"Where the Sidewalk Ends\"?", "Shel Silverstein"]
    ],
    "Famous World Leaders": [
        ["Abraham Lincoln is most famous for _____________.", "Working to end slavery in America"],
        ["Akbar created a thriving empire through what modern country?", "India"],
        ["Alexander the Great created ____________________.", "One of the largest empires in the ancient world"],
        ["Chairman Mao led which government party to victory in China?", "Communism"],
        ["Henry VIII wanted to remarry, which contributed to the creation of which religion?", "The Church of England"],
        ["Joan of Arc fought bravely for what cause?", "French Independence"],
        ["Julius Caesar was key in the expansion of the ___________.", "Roman Empire"],
        ["King Henry VIII had how many wives?", "Six"],
        ["Mahatma Gandhi devoted his life to what?", "Indian independence"],
        ["Napoleon Bonaparte was the famous emperor of _______.", "France"],
        ["Nelson Mandela ___________________ before becoming the first President of democratic South Africa in 1994?", "spent over 20 years in jail"],
        ["Thomas Jefferson wrote which famous US document?", "The Declaration of Independence"],
        ["What was Julius Caesar's motto?", "I came, I saw, I conquered"],
        ["Who was Margaret Thatcher?", "British Prime Minister"]
    ],
    "Greek Mythology": [
        ["Which Greek god is the god of fertility and wine?", "Dionysus"],
        ["Which Greek god is the god of fire and forge?", "Hephaestus"],
        ["Which Greek god is the god of flocks and shepherds?", "Pan"],
        ["Which Greek god is the god of love?", "Eros"],
        ["Which Greek god is the god of music, healing, light and truth?", "Apollo"],
        ["Which Greek god is the god of the sun?", "Helios"],
        ["Which Greek god is the god of war?", "Ares"],
        ["Which Greek god is the goddess of corn, grain and harvest?", "Demeter"],
        ["Which Greek god is the goddess of discord?", "Eris"],
        ["Which Greek god is the goddess of intelligence and the arts?", "Athena"],
        ["Which Greek god is the goddess of love, desire and beauty?", "Aphrodite"],
        ["Which Greek god is the goddess of marriage and childbirth?", "Hera"],
        ["Which Greek god is the goddess of springtime?", "Persephone"],
        ["Which Greek god is the goddess of youth?", "Hebe"],
        ["Which Greek god is the lord of the underworld?", "Hades"],
        ["Which Greek god is the personification of death?", "Thanatos"],
        ["Which Greek god is the protector of all waters?", "Poseidon"],
        ["Which Greek god is the ruler of the Olympian gods?", "Zeus"]
    ],
    "Habitats": [
        ["Animals in the desert have adopted a ___________ lifestyle to survive the heat.", "Nocturnal"],
        ["How are freshwater lakes and rivers created?", "Streams high in the Mountains that flow down"],
        ["The largest animal in the world, the blue whale, resides in which habitat?", "Ocean"],
        ["What is a habitat?", "The natural home or environment of an animal, plant, or other organism"],
        ["What is the coldest habitat?", "Tundra"],
        ["What is the habitat that has little rain and intense sunshine?", "Desert"],
        ["What is the largest habitat on the planet?", "Ocean"],
        ["What kind of a climate does a swamp have?", "Warm, wet, humid"],
        ["What type of habitat can be found in all ranges of climate?", "Temperate Forests"],
        ["What type of plant grows in the desert?", "Cactus"],
        ["Which continent does NOT have Grasslands?", "Antarctica"],
        ["Which habitat do animals have to withstand lower oxygen levels?", "Mountains"],
        ["Which habitat has trees with needle shaped leaves?", "Coniferous Forest"],
        ["Which habitat is found in tropical regions?", "Rainforest"],
        ["Which is a large predator that lives in Coniferous Forests?", "Bear"],
        ["Which of the following is NOT a habitat found on land?", "Coral Reef"],
        ["Which of the following is NOT a habitat?", "Bottle"],
        ["Which of the following is NOT part of the Ocean landscape?", "Hills"]
    ],
    "Heart": [
        ["How many chambers does a human heart have?", "4"],
        ["The heart beats approximately ____________ times each day.", "100,000"],
        ["What anatomical system is the heart a part of?", "Cardiovascular system"],
        ["What blood vessel carries oxygen-rich blood to the body?", "Artery"],
        ["What blood vessel returns oxygen-poor blood to the heart?", "Vein"],
        ["What does the heart do?", "Pumps blood throughout the body"],
        ["What does the heart pump?", "Blood"],
        ["What is a normal resting heart rate for adults over the age 18?", "60-100 bpm"],
        ["What is a normal resting heart rate range for children?", "70-100 bpm"],
        ["What is the name of the largest artery in the body?", "Aorta"],
        ["What tiny blood vessels transport blood from an artery to a vein?", "Capillaries"],
        ["Where is the heart located?", "Chest"],
        ["Which artery carries blood from the heart to the lungs?", "Pulmonary Artery"],
        ["Which atrium receives oxygen-poor blood from the body?", "Right atrium"],
        ["Which atrium receives oxygen-rich blood from the lungs?", "Left atrium"],
        ["Which of the following is not a systemic artery?", "Pulmonary Artery"],
        ["Which part of the heart allows blood to flow in only one direction?", "Valve"],
        ["Which vein carries oxygen-rich blood to the heart from the lungs?", "Pulmonary Veins"],
        ["Which ventricle pumps oxygen-rich blood to the body?", "Left ventricle"],
        ["Which ventricle pumps oxygen-poor blood to the lungs?", "Right ventricle"]
    ],
    "Landforms": [
        ["Bayou, Gully, Marsh and Shoal are examples of what?", "Fluvial landforms"],
        ["Caldera, Maar, Vent, and Tuya are examples of what?", "Volcanic landforms"],
        ["Cave, Cenote, Karren and Mogote are examples of what?", "Karst landforms"],
        ["Erosion landforms are caused by what?", "Weathering"],
        ["Impact landforms are caused by ________________ impacts.", "Extraterrestrial"],
        ["Lacustrine landforms are primarily filled with __________.", "Incoming sediment"],
        ["What forms Aeolian landforms?", "Wind"],
        ["Which of the following are not associated with fluvial landforms?", "Volcanoes"],
        ["Which of the following is not considered a coastal landform?", "Yardang"],
        ["Which of the following is not considered a fluvial landform?", "Sinkhole"],
        ["Which of the following is not considered a karst landform?", "Valley"],
        ["Which of the following is not considered a mountain or glacial landform?", "Oasis"],
        ["Which of the following is not considered a slope landform?", "Pull apart basin"],
        ["Which of the following is not considered a tectonic landform?", "Sinkhole"],
        ["Which of the following is not considered an Aeolian landform?", "Sound"],
        ["Which type of rock is not generally a cause for karst typography?", "Granite"]
    ],
    "Ninth Grade Vocabulary": [
        ["Abstract", "a concept or idea not associated with any specific instance"],
        ["Advocate", "a person who pleads for a cause or propounds an idea"],
        ["Belittle", "lessen the authority, dignity, or reputation of"],
        ["Censure", "harsh criticism or disapproval"],
        ["Comply", "act in accordance with someone's rules, commands, or wishes"],
        ["Deference", "a disposition or tendency to yield to the will of others"],
        ["Eccentric", "a person of a specified kind (usually with many eccentricities)"],
        ["Facilitate", "make easier"],
        ["Guile", "shrewdness as demonstrated by being skilled in deception"],
        ["Heed", "paying particular notice (as to children or helpless people)"],
        ["Inadvertent", "without intention (especially resulting from heedless action)"],
        ["Mar", "a mark or flaw that spoils the appearance of something (especially on a person's body)"],
        ["Parsimony", "extreme care in spending money"],
        ["Recalcitrant", "marked by stubborn resistance to authority"],
        ["Tangible", "possible to be treated as fact"],
        ["Verbose", "using or containing too many words"]
    ],
    "Norse Mythology": [
        ["Baldr was the god of what?", "Beauty, innocence, peace and rebirth"],
        ["Who was the first Norse god?", "Buri"],
        ["Who was the god of dawn?", "Delling"],
        ["Who was the god of inspiration?", "Kvasir"],
        ["Who was the god of justice, peace and truth?", "Forseti"],
        ["Who was the god of revenge?", "Vali"],
        ["Who was the god of skiing, winter, hunting and dueling?", "Ullr"],
        ["Who was the god of strength and son of Thor?", "Magni"],
        ["Who was the god of the daytime?", "Dagr"],
        ["Who was the god of war and the \"All Father\"?", "Odin"],
        ["Who was the goddess of consolation and protection?", "Hlin"],
        ["Who was the goddess of fertility and plough?", "Gefjun"],
        ["Who was the goddess of healing?", "Eir"],
        ["Who was the goddess of marriage and motherhood?", "Frigg"],
        ["Who was the goddess of prudence?", "Snotra"],
        ["Who was the goddess of the sun?", "Sol"],
        ["Who was the goddess of wisdom?", "Vor"],
        ["Who was the wife of Thor and goddess of the harvest?", "Sif"]
    ],
    "Primates": [
        ["Roughly how many species of primate does the IUCN recognize?", "600"],
        ["This primate hunts by tapping on trees and digging out insect larvae.", "Aye-aye"],
        ["What is the largest living primate?", "Gorilla"],
        ["What is the largest tree climbing mammal in the world?", "Orangutan"],
        ["What is the largest type of monkey?", "Mandrill"],
        ["What is the primary difference between monkeys and apes?", "Apes don't have tails"],
        ["What is the smallest primate?", "Pygmy Mouse Lemur"],
        ["Which continent are apes and monkeys not native to?", "North America"],
        ["Which is the following is not considered a Promisian?", "Marmoset"],
        ["Which of the following is not a type of Gorilla?", "Macaque"],
        ["Which of the following is not a word used to describe a group of monkeys?", "Barrel"],
        ["Which of the following is not considered a Great Ape?", "Gibbon"],
        ["Which of these monkeys is not a new world monkey?", "Macauqe"],
        ["Which of these monkeys is not an old world monkey?", "Marmoset"],
        ["Which primate is easily recognized by their orange fur and very long arms?", "Orangutan"],
        ["Why do howler monkeys howl?", "Defend their territory"]
    ],
    "Solar System": [
        ["Every object in our solar system revolves around the _______.", "Sun"],
        ["How many planets are in our solar system?", "Eight"],
        ["Jupiter has a ________ in its atmosphere but no solid surface.", "Hurricane"],
        ["Mars is known as the _____ planet.", "Red"],
        ["Saturn is famous for its ________ that rotate around it.", "Rings"],
        ["Uranus has a _______ glow to it.", "Blue"],
        ["Venus' atmosphere is primarily made up of what gas?", "Carbon Dioxide"],
        ["What are comets made of?", "Dirty Ice"],
        ["What is the correct term for Pluto?", "Dwarf Planet"],
        ["What is the largest planet in the solar system?", "Jupiter"],
        ["What man-made objects exist in our solar system?", "Satellites & Space Junk"],
        ["What separates the inner and outer solar system?", "Band of asteroids"],
        ["Which is the smallest planet in the solar system?", "Mercury"],
        ["Which planet is closest to the sun?", "Mercury"],
        ["Which planet is furthest from the sun?", "Neptune"],
        ["Which two planets are Earth's \"neighbors\"?", "Venus & Mars"]
    ],
    "Spelling": [
        ["Which word is spelled correctly?", "Abbreviate"],
        ["Which word is spelled correctly?", "Abyss"],
        ["Which word is spelled correctly?", "Accidentally"],
        ["Which word is spelled correctly?", "Aggressive"],
        ["Which word is spelled correctly?", "Anonymous"],
        ["Which word is spelled correctly?", "Australia"],
        ["Which word is spelled correctly?", "Bureaucratic"],
        ["Which word is spelled correctly?", "Camouflage"],
        ["Which word is spelled correctly?", "Connecticut"],
        ["Which word is spelled correctly?", "Connoisseur"],
        ["Which word is spelled correctly?", "Disappointed"],
        ["Which word is spelled correctly?", "February"],
        ["Which word is spelled correctly?", "Hygiene"],
        ["Which word is spelled correctly?", "Physique"],
        ["Which word is spelled correctly?", "Wednesday"]
    ],
    "State Animals": [
        ["What is the state animal of California?", "Grizzly Bear"],
        ["What is the state animal of Florida?", "Florida Panther"],
        ["What is the state animal of Illinois?", "White-Tailed Deer"],
        ["What is the state animal of Kansas?", "American Buffalo"],
        ["What is the state animal of Missouri?", "Missouri Mule"],
        ["What is the state animal of Nevada?", "Desert Bighorn Sheep"],
        ["What is the state animal of New Jersey?", "Horse"],
        ["What is the state animal of New Mexico?", "Black Bear"],
        ["What is the state animal of Ohio?", "White-Tailed Deer"],
        ["What is the state animal of Oregon?", "Beaver"],
        ["What is the state animal of Pennsylvania?", "White-Tailed Deer"],
        ["What is the state animal of South Carolina?", "White-Tailed Deer"],
        ["What is the state animal of South Dakota?", "Coyote"],
        ["What is the state animal of Utah?", "Rocky Mountain Elk"],
        ["What is the state animal of Wisconsin?", "Badger"],
        ["What is the state cat of Maine?", "Maine Coon Cat"],
        ["What is the state cat of Maryland?", "Calico Cat"],
        ["What is the state cat of Massachusetts?", "Tabby Cat"],
        ["What is the state dog of Alaska?", "Alaskan Malamute"],
        ["What is the state dog of Maryland?", "Chesapeake Bay Retriever"],
        ["What is the state dog of Massachusetts?", "Boston Terrier"],
        ["What is the state dog of South Carolina?", "Boykin Spaniel"],
        ["What is the state dog of Texas?", "Blue Lacy"],
        ["What is the state dog of Virginia?", "American Foxhound"],
        ["What is the state dog of Wisconsin?", "American Water Spaniel"],
        ["What is the state horse of Idaho?", "Appaloosa"],
        ["What is the state horse of Maryland?", "Thoroughbred"],
        ["What is the state horse of Massachusetts?", "Morgan Horse"],
        ["What is the state horse of Missouri?", "Missouri Fox Trotting Horse"],
        ["What is the state horse of North Carolina?", "Colonial Spanish Mustang"],
        ["What is the state horse of Texas?", "Quarter Horse"],
        ["What is the state land animal of Alaska?", "Moose"],
        ["What is the state large mammal of Texas?", "Longhorn"],
        ["What is the state mammal of Alabama?", "Black Bear"],
        ["What is the state mammal of Arizona?", "Ringtail"],
        ["What is the state mammal of Arkansas?", "White-Tailed Deer"],
        ["What is the state mammal of Hawaii?", "Hawaiian Monk Seal"],
        ["What is the state mammal of Louisiana?", "Black Bear"],
        ["What is the state mammal of Nebraska?", "White-Tailed Deer"],
        ["What is the state marine mammal of Alaska?", "Bowhead Whale"],
        ["What is the state marine mammal of California?", "Gray Whale"],
        ["What is the state marine mammal of Florida?", "Manatee"],
        ["What is the state marine mammal of Massachusetts?", "Right Whale"],
        ["What is the state small mammal of Texas?", "Nine-Banded Armadillo"],
        ["What is the state water mammal of Mississippi?", "Dolphin"],
        ["What is the state wild animal of Tennessee?", "Raccoon"]
    ],
    "State Birds": [
        ["What is the state bird of Alabama?", "Yellowhammer"],
        ["What is the state bird of Alaska?", "Willow Ptarmigan"],
        ["What is the state bird of Arizona?", "Cactus Wren"],
        ["What is the state bird of Arkansas?", "Mockingbird"],
        ["What is the state bird of California?", "California Quail"],
        ["What is the state bird of Colorado?", "Lark Bunting"],
        ["What is the state bird of Connecticut?", "American Robin"],
        ["What is the state bird of Delaware?", "Delaware Blue Hen"],
        ["What is the state bird of Florida?", "Mockingbird"],
        ["What is the state bird of Georgia?", "Brown Thrasher"],
        ["What is the state bird of Hawaii?", "Nene"],
        ["What is the state bird of Idaho?", "Mountain Bluebird"],
        ["What is the state bird of Illinois?", "Cardinal"],
        ["What is the state bird of Indiana?", "Cardinal"],
        ["What is the state bird of Iowa?", "American Goldfinch"],
        ["What is the state bird of Kansas?", "Western Meadowlark"],
        ["What is the state bird of Kentucky?", "Cardinal"],
        ["What is the state bird of Louisiana?", "Brown Pelican"],
        ["What is the state bird of Maine?", "Black-Capped Chickadee"],
        ["What is the state bird of Maryland?", "Baltimore Oriole"],
        ["What is the state bird of Massachusetts?", "Black-Capped Chickadee"],
        ["What is the state bird of Michigan?", "American Robin"],
        ["What is the state bird of Minnesota?", "Common Loon"],
        ["What is the state bird of Mississippi ?", "Mockingbird"],
        ["What is the state bird of Missouri?", "Eastern Bluebird"],
        ["What is the state bird of Montana?", "Western Meadowlark"],
        ["What is the state bird of Nebraska?", "Western Meadowlark"],
        ["What is the state bird of Nevada?", "Mountain Bluebird"],
        ["What is the state bird of New Hampshire?", "Purple Finch"],
        ["What is the state bird of New Jersey?", "American Goldfinch"],
        ["What is the state bird of New Mexico?", "Roadrunner"],
        ["What is the state bird of New York?", "Eastern Bluebird"],
        ["What is the state bird of North Carolina?", "Cardinal"],
        ["What is the state bird of North Dakota?", "Western Meadowlark"],
        ["What is the state bird of Ohio?", "Cardinal"],
        ["What is the state bird of Oklahoma?", "Scissor-Tailed Flycatcher"],
        ["What is the state bird of Oregon?", "Western Meadowlark"],
        ["What is the state bird of Pennysylvania?", "Ruffed Grouse"],
        ["What is the state bird of Rhode Island?", "Rhode Island Red"],
        ["What is the state bird of South Carolina?", "Carolina Wren"],
        ["What is the state bird of South Dakota?", "Ring-Necked Pheasant"],
        ["What is the state bird of Tennessee?", "Mockingbird"],
        ["What is the state bird of Texas?", "Mockingbird"],
        ["What is the state bird of Utah?", "California Gull"],
        ["What is the state bird of Vermont?", "Hermit Thrush"],
        ["What is the state bird of Virginia?", "Cardinal"],
        ["What is the state bird of Washington?", "American Goldfinch"],
        ["What is the state bird of West Virginia?", "Cardinal"],
        ["What is the state bird of Wisconsin?", "American Robin"],
        ["What is the state bird of Wyoming?", "Western Meadowlark"]
    ],
    "State Capitals": [
        ["What is the capital of Alabama?", "Montgomery"],
        ["What is the capital of Alaska?", "Juneau"],
        ["What is the capital of Arizona?", "Phoenix"],
        ["What is the capital of Arkansas?", "Little Rock"],
        ["What is the capital of California?", "Sacramento"],
        ["What is the capital of Colorado?", "Denver"],
        ["What is the capital of Connecticut?", "Hartford"],
        ["What is the capital of Delaware?", "Dover"],
        ["What is the capital of Florida?", "Tallahassee"],
        ["What is the capital of Georgia?", "Atlanta"],
        ["What is the capital of Hawaii?", "Honolulu"],
        ["What is the capital of Idaho?", "Boise"],
        ["What is the capital of Illinois?", "Springfield"],
        ["What is the capital of Indiana?", "Indianapolis"],
        ["What is the capital of Iowa?", "Des Moines"],
        ["What is the capital of Kansas?", "Topeka"],
        ["What is the capital of Kentucky?", "Frankfort"],
        ["What is the capital of Louisiana?", "Baton Rouge"],
        ["What is the capital of Maine?", "Augusta"],
        ["What is the capital of Maryland?", "Annapolis"],
        ["What is the capital of Massachusetts?", "Boston"],
        ["What is the capital of Michigan?", "Lansing"],
        ["What is the capital of Minnesota?", "Saint Paul"],
        ["What is the capital of Mississippi?", "Annapolis"],
        ["What is the capital of Missouri?", "Jefferson City"],
        ["What is the capital of Montana?", "Helena"],
        ["What is the capital of Nebraska?", "Lincoln"],
        ["What is the capital of Nevada?", "Carson City"],
        ["What is the capital of New Hampshire?", "Concord"],
        ["What is the capital of New Jersey?", "Trenton"],
        ["What is the capital of New Mexico?", "Santa Fe"],
        ["What is the capital of New York?", "Albany"],
        ["What is the capital of North Carolina?", "Raleigh"],
        ["What is the capital of North Dakota?", "Bismark"],
        ["What is the capital of Ohio?", "Columbus"],
        ["What is the capital of Oklahoma?", "Oklahoma City"],
        ["What is the capital of Oregon?", "Salem"],
        ["What is the capital of Pennsylvania?", "Harrisburg"],
        ["What is the capital of Rhode Island?", "Providence"],
        ["What is the capital of South Carolina?", "Columbia"],
        ["What is the capital of South Dakota?", "Pierre"],
        ["What is the capital of Tennessee?", "Nashville"],
        ["What is the capital of Texas?", "Austin"],
        ["What is the capital of Utah?", "Salt Lake City"],
        ["What is the capital of Vermont?", "Montpelier"],
        ["What is the capital of Virginia?", "Richmond"],
        ["What is the capital of Washington?", "Olympia"],
        ["What is the capital of West Virginia?", "Charleston"],
        ["What is the capital of Wisconsin?", "Madison"],
        ["What is the capital of Wyoming?", "Chenyenne"]
    ],
    "State Nicknames": [
        ["Which state is known as the \"Aloha State?\"", "Hawaii"],
        ["Which state is known as the \"Beaver State?\"", "Oregon"],
        ["Which state is known as the \"Beehive State?\"", "Utah"],
        ["Which state is known as the \"Bluegrass State?\"", "Kentucky"],
        ["Which state is known as the \"Constitution State?\"", "Connecticut"],
        ["Which state is known as the \"Empire State?\"", "New York"],
        ["Which state is known as the \"Evergreen State?\"", "Washington"],
        ["Which state is known as the \"First State?\"", "Delaware"],
        ["Which state is known as the \"Garden State?\"", "New Jersey"],
        ["Which state is known as the \"Golden State?\"", "California"],
        ["Which state is known as the \"Great Lakes State?\"", "Michigan"],
        ["Which state is known as the \"Lone Star State?\"", "Texas"],
        ["Which state is known as the \"Magnolia State?\"", "Mississippi"],
        ["Which state is known as the \"Ocean State?\"", "Rhode Island"],
        ["Which state is known as the \"Pelican State?\"", "Louisiana"],
        ["Which state is known as the \"Pine Tree State?\"", "Maine"],
        ["Which state is known as the \"Prairie State?\"", "Illinois"],
        ["Which state is known as the \"Silver State?\"", "Nevada"],
        ["Which state is known as the \"Sunflower State?\"", "Kansas"],
        ["Which state is known as the \"Volunteer State?\"", "Tennessee"]
    ],
    "Tenth Grade Vocabulary": [
        ["Adjunct", "something attached to but holding an inferior position"],
        ["Congregate", "To come together in a group, assemble."],
        ["Dialogue", "a conversation between two persons"],
        ["Eloquent", "expressing yourself readily, clearly, effectively"],
        ["Gregarious", "seeking and enjoying the company of others"],
        ["Injunction", "a formal command or admonition"],
        ["Junction", "an act of joining or adjoining things"],
        ["Juncture", "a joining together; the point at which two things are joined; any important point in time"],
        ["Malady", "a sickness, illness, disease, disorder"],
        ["Malcontent", "person dissatisfied with existing state of affairs"],
        ["Malevolent", "wishing or appearing to wish evil to others"],
        ["Malicious", "wishing evil or harm upon others"],
        ["Phonetic", "related to the sounds in a language"],
        ["Segregate", "separating into different groups"],
        ["Soliloquy", "the act of talking to oneself or a dramatic monologue"]
    ],
    "Twelfth Grade Vocabulary": [
        ["Antithesis", "the direct opposite or contrast to a previously given assertion"],
        ["Benevolent", "showing or motivated by sympathy and understanding and generosity"],
        ["Brazen", "unrestrained by convention or propriety"],
        ["Chicanery", "deceiving someone, scam"],
        ["Conundrum", "a difficult problem"],
        ["Deleterious", "harmful to living things"],
        ["Enervate", "to weaken, or to take energy from"],
        ["Evanescent", "tending to vanish like vapor"],
        ["Fortuitous", "occurring by happy chance"],
        ["Guru", "religious teacher"],
        ["Hegemony", "one country/group has leadership over another"],
        ["Impetuous", "characterized by undue haste and lack of thought or deliberation"],
        ["Jovial", "happy, cheery"],
        ["Loquacious", "talkative, chatty"],
        ["Peruse", "reading with careful attention"],
        ["Sensuous", "all senses, dealing w/ all senses"]
    ],
    "Weather": [
        ["A waterspout is actually a weak ______ that forms over water.", "Tornado"],
        ["How fast do raindrops fall?", "7-18 miles per hour"],
        ["How is snow formed?", "Water vapor changes directly to ice high in the atmosphere"],
        ["In which two seasons are thunderstorms most likely to occur?", "Spring & Summer"],
        ["The ______ is the center of a hurricane and also the calmest part of the storm.", "Eye"],
        ["Tornado are rated on what kind of scale?", "F Scale"],
        ["What causes the electric current that result in lightning?", "Ice particles bumping into each other"],
        ["What does a Tornado Watch mean?", "Tornadoes are possible in your area."],
        ["What is a monsoon?", "Seasonal wind that often brings rain"],
        ["What is a tornado called before it hits the ground?", "Funnel Cloud"],
        ["What is sleet?", "Rain that freezes into ice before it hits ground"],
        ["What is the name of the strong radar that helps predict weather?", "Doppler"],
        ["What type of cloud is above 18,000 feet in the atmosphere?", "Cirrus"],
        ["What type of cloud is below 6,500 feet in the atmosphere?", "Stratus"],
        ["What type of cloud is between 6,500 feet to 18,000 feet in the atmosphere?", "Alto"],
        ["What type of cloud usually looks white and puffy?", "Cumulus"],
        ["Where do tornadoes come from?", "Thunderstorms"],
        ["Which of the following is not a characteristic of a hurricane?", "Forms over mountains"],
        ["Which of the following is NOT needed to cause a blizzard?", "Rotating storm clouds"]
    ],
    "World Capitals": [
        ["What is the capital of Argentina?", "Buenos Aires"],
        ["What is the capital of Australia?", "Canberra"],
        ["What is the capital of Austria?", "Vienna"],
        ["What is the capital of Belgium?", "Brussels"],
        ["What is the capital of Brazil?", "Brasilia"],
        ["What is the capital of Canada?", "Ottawa"],
        ["What is the capital of China?", "Beijing"],
        ["What is the capital of Cuba?", "Havana"],
        ["What is the capital of Czech Republic?", "Prague"],
        ["What is the capital of Denmark?", "Copenhagen"],
        ["What is the capital of Egypt?", "Cairo"],
        ["What is the capital of Finland?", "Helsinki"],
        ["What is the capital of France?", "Paris"],
        ["What is the capital of Germany?", "Berlin"],
        ["What is the capital of Greece?", "Athens"],
        ["What is the capital of Hungary?", "Budapest"],
        ["What is the capital of India?", "New Delhi"],
        ["What is the capital of Italy?", "Rome"],
        ["What is the capital of Japan?", "Tokyo"],
        ["What is the capital of Mexico?", "Mexico City"],
        ["What is the capital of The Bahamas?", "Nassau"]
    ]
}

def getSelectedText():
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.01)
    return pyperclip.paste()

class mainWindowWidget(QMainWindow):
    updateSignal = pyqtSignal(str)
    
    def __init__(self, *args, **kwargs):
        super(mainWindowWidget, self).__init__(*args, **kwargs)
        self.setWindowTitle("Trivia!")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        
        self.auto_copy = QCheckBox("Auto Spam Ctrl+C", self, objectName = "auto_copy")
        self.auto_copy.move(4, 0)
        self.auto_copy.setFixedSize(200, 20)
        self.auto_copy.setFont(FONT)
        
        self.searching = QLabel("searching for: \"\"", self, objectName = "searching")
        self.searching.move(0, 20)
        self.searching.setFixedSize(200, 20)
        self.searching.setFont(FONT) 
        
        self.count = QLabel("possible matches: 0", self, objectName = "count")
        self.count.move(0, 40)
        self.count.setFixedSize(200, 20)
        self.count.setFont(FONT) 
        
        self.quiz = QLabel("most likely quiz: idk", self, objectName = "quiz")
        self.quiz.move(0, 60)
        self.quiz.setFixedSize(200, 20)
        self.quiz.setFont(FONT)
        
        self.answer_label = QLabel("possible answers:", self, objectName = "answer_label")
        self.answer_label.move(0, 80)
        self.answer_label.setFixedSize(200, 20)
        self.answer_label.setFont(FONT)
        
        self.answer = QPlainTextEdit("idk", self, objectName = "answer")
        self.answer.move(0, 100)
        self.answer.setFixedSize(200, 20)
        self.answer.setFont(FONT)
        
        
        minx = 200
        miny = 20 * 5 + 15
        self.setMinimumSize(minx, miny)
        self.resize(1000, miny + 40)
        
        self.updateSignal.connect(self.update)
    
    def resizeEvent(self, event):
        self.searching.setFixedSize(self.width(), 20)
        self.count.setFixedSize(self.width(), 20)
        self.quiz.setFixedSize(self.width(), 20)
        self.answer_label.setFixedSize(self.width(), 20)
        self.answer.setFixedSize(self.width(), self.height() - 80)
    
    def update(self, txt):
        txt = ' '.join(txt.rstrip().split())
        self.searching.setText("searching for: \"%s\"" % txt)
        
        answers = []
        quizzes = []
        for quiz, questions in QUIZ_ANSWERS.items():
            c = 0
            for [question, answer] in questions:
                if txt.lower() in question.lower():
                    c += 1
                    answers.append(answer)
            if c > 0:
                quizzes.append(quiz)
            
        self.count.setText("possible matches: %d" % len(answers))
        self.quiz.setText("most likely quiz: %s" % (quizzes[0] if len(quizzes) > 0 else "idk"))
        
        out = "idk"
        if len(answers) == 1:
            out = answers[0]
        elif len(answers) > 1:
            out = ",\n".join(answers)

        self.answer.setPlainText(out)


if __name__ == "__main__":
    app = QApplication([])
    
    window = mainWindowWidget()
    window.show()
    dead = False
    
    def q():
        global dead
        while not dead:
            try:
                if window.auto_copy.isChecked():
                    window.updateSignal.emit(getSelectedText())
                else:
                    window.updateSignal.emit(pyperclip.paste())
            except:
                pass
            time.sleep(0.1)
        app.quit()
        
    threading.Thread(target = q).start()
    try:
        app.exec_()
    except:
        pass
    dead = True
