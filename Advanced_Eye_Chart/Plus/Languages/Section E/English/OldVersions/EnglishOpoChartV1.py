# Start of script
import random # Needed for randomizing IDs for letters, numbers, and other symbols for the eye chart to render

'''
This is the English only version of the chart
English only version (only contains the English chart)
'''

# English chart (language)

# This is extremely inefficient. If anyone knows a better way, let me know
letter1ID = random.randint(0, 85) # First letter on the chart, top left, largest (200/20)
if (letter1ID == 0):
	letter1 = str("a")
if (letter1ID == 1):
	letter1 = str("A")
if (letter1ID == 2):
	letter1 = str("b")
if (letter1ID == 3):
	letter1 = str("B")
if (letter1ID == 4):
	letter1 = str("c")
if (letter1ID == 5):
	letter1 = str("C")
if (letter1ID == 6):
	letter1 = str("d")
if (letter1ID == 7):
	letter1 = str("D")
if (letter1ID == 8):
	letter1 = str("e")
if (letter1ID == 9):
	letter1 = str("E")
if (letter1ID == 10):
	letter1 = str("f")
if (letter1ID == 11):
	letter1 = str("F")
if (letter1ID == 12):
	letter1 = str("g")
if (letter1ID == 13):
	letter1 = str("G")
if (letter1ID == 14):
	letter1 = str("h")
if (letter1ID == 15):
	letter1 = str("H")
if (letter1ID == 16):
	letter1 = str("i")
if (letter1ID == 17):
	letter1 = str("I")
if (letter1ID == 18):
	letter1 = str("j")
if (letter1ID == 19):
	letter1 = str("J")
if (letter1ID == 20):
	letter1 = str("k")
if (letter1ID == 21):
	letter1 = str("K")
if (letter1ID == 22):
	letter1 = str("l")
if (letter1ID == 23):
	letter1 = str("L")
if (letter1ID == 24):
	letter1 = str("m")
if (letter1ID == 25):
	letter1 = str("M")
if (letter1ID == 26):
	letter1 = str("n")
if (letter1ID == 27):
	letter1 = str("N")
if (letter1ID == 28):
	letter1 = str("o")
if (letter1ID == 29):
	letter1 = str("O")
if (letter1ID == 30):
	letter1 = str("p")
if (letter1ID == 31):
	letter1 = str("P")
if (letter1ID == 32):
	letter1 = str("q")
if (letter1ID == 33):
	letter1 = str("Q")
if (letter1ID == 34):
	letter1 = str("r")
if (letter1ID == 35):
	letter1 = str("R")
if (letter1ID == 36):
	letter1 = str("s")
if (letter1ID == 37):
	letter1 = str("S")
if (letter1ID == 38):
	letter1 = str("T")
if (letter1ID == 39):
	letter1 = str("t")
if (letter1ID == 40):
	letter1 = str("u")
if (letter1ID == 41):
	letter1 = str("U")
if (letter1ID == 42):
	letter1 = str("v")
if (letter1ID == 43):
	letter1 = str("V")
if (letter1ID == 44):
	letter1 = str("w")
if (letter1ID == 45):
	letter1 = str("W")
if (letter1ID == 46):
	letter1 = str("x")
if (letter1ID == 47):
	letter1 = str("X")
if (letter1ID == 48):
	letter1 = str("y")
if (letter1ID == 49):
	letter1 = str("Y")
if (letter1ID == 50):
	letter1 = str("z")
if (letter1ID == 51):
	letter1 = str("Z")
if (letter1ID == 52):
	letter1 = str("0")
if (letter1ID == 53):
	letter1 = str("1")
if (letter1ID == 54):
	letter1 = str("2")
if (letter1ID == 55):
	letter1 = str("3")
if (letter1ID == 56):
	letter1 = str("4")
if (letter1ID == 57):
	letter1 = str("5")
if (letter1ID == 58):
	letter1 = str("6")
if (letter1ID == 59):
	letter1 = str("7")
if (letter1ID == 60):
	letter1 = str("8")
if (letter1ID == 61):
	letter1 = str("9")
if (letter1ID == 62):
	letter1 = str(",")
if (letter1ID == 63):
	letter1 = str(".")
if (letter1ID == 64):
	letter1 = str("!")
if (letter1ID == 65):
	letter1 = str("@")
if (letter1ID == 66):
	letter1 = str("#")
if (letter1ID == 67):
	letter1 = str("$")
if (letter1ID == 68):
	letter1 = str("!")
if (letter1ID == 69):
	letter1 = str("%")
if (letter1ID == 70):
	letter1 = str("^")
if (letter1ID == 71):
	letter1 = str("&")
if (letter1ID == 72):
	letter1 = str("*")
if (letter1ID == 73):
	letter1 = str("=")
if (letter1ID == 74):
	letter1 = str("-")
if (letter1ID == 75):
	letter1 = str("+")
if (letter1ID == 76):
	letter1 = str("_")
if (letter1ID == 77):
	letter1 = str("?")
if (letter1ID == 78):
	letter1 = str("<")
if (letter1ID == 79):
	letter1 = str(">")
if (letter1ID == 80):
	letter1 = str("~")
if (letter1ID == 81):
	letter1 = str("`")
if (letter1ID == 82):
	letter1 = str("\"")
if (letter1ID == 83):
	letter1 = str("/")
if (letter1ID == 84):
	letter1 = str(":")
if (letter1ID == 85):
	letter1 = str(";")
letter2ID = random.randint(0, 85)
if (letter2ID == 0 and letter2ID != letter1ID):
	letter2 = str("a")
if (letter2ID == 1 and letter2ID != letter1ID):
	letter2 = str("A")
if (letter2ID == 2 and letter2ID != letter1ID):
	letter2 = str("b")
if (letter1ID == 3 and letter2ID != letter1ID):
	letter1 = str("B")
if (letter1ID == 4 and letter2ID != letter1ID):
	letter1 = str("c")
if (letter1ID == 5 and letter2ID != letter1ID):
	letter1 = str("C")
if (letter1ID == 6 and letter2ID != letter1ID):
	letter1 = str("d")
if (letter1ID == 7 and letter2ID != letter1ID):
	letter1 = str("D")
if (letter1ID == 8 and letter2ID != letter1ID):
	letter1 = str("e")
if (letter1ID == 9 and letter2ID != letter1ID):
	letter1 = str("E")
if (letter1ID == 10 and letter2ID != letter1ID):
	letter1 = str("f")
if (letter1ID == 11 and letter2ID != letter1ID):
	letter1 = str("F")
if (letter1ID == 12 and letter2ID != letter1ID):
	letter1 = str("g")
if (letter1ID == 13 and letter2ID != letter1ID):
	letter1 = str("G")
if (letter1ID == 14 and letter2ID != letter1ID):
	letter1 = str("h")
if (letter1ID == 15 and letter2ID != letter1ID):
	letter1 = str("H")
if (letter1ID == 16 and letter2ID != letter1ID):
	letter1 = str("i")
if (letter1ID == 17 and letter2ID != letter1ID):
	letter1 = str("I")
if (letter1ID == 18 and letter2ID != letter1ID):
	letter1 = str("j")
if (letter1ID == 19 and letter2ID != letter1ID):
	letter1 = str("J")
if (letter1ID == 20 and letter2ID != letter1ID):
	letter1 = str("k")
if (letter1ID == 21 and letter2ID != letter1ID):
	letter1 = str("K")
if (letter1ID == 22 and letter2ID != letter1ID):
	letter1 = str("l")
if (letter1ID == 23 and letter2ID != letter1ID):
	letter1 = str("L")
if (letter1ID == 24 and letter2ID != letter1ID):
	letter1 = str("m")
if (letter1ID == 25 and letter2ID != letter1ID):
	letter1 = str("M")
if (letter1ID == 26 and letter2ID != letter1ID):
	letter1 = str("n")
if (letter1ID == 27 and letter2ID != letter1ID):
	letter1 = str("N")
if (letter1ID == 28 and letter2ID != letter1ID):
	letter1 = str("o")
if (letter1ID == 29 and letter2ID != letter1ID):
	letter1 = str("O")
if (letter1ID == 30 and letter2ID != letter1ID):
	letter1 = str("p")
if (letter1ID == 31 and letter2ID != letter1ID):
	letter1 = str("P")
if (letter1ID == 32 and letter2ID != letter1ID):
	letter1 = str("q")
if (letter1ID == 33 and letter2ID != letter1ID):
	letter1 = str("Q")
if (letter1ID == 34 and letter2ID != letter1ID):
	letter1 = str("r")
if (letter1ID == 35 and letter2ID != letter1ID):
	letter1 = str("R")
if (letter1ID == 36 and letter2ID != letter1ID):
	letter1 = str("s")
if (letter1ID == 37 and letter2ID != letter1ID):
	letter1 = str("S")
if (letter1ID == 38 and letter2ID != letter1ID):
	letter1 = str("T")
if (letter1ID == 39 and letter2ID != letter1ID):
	letter1 = str("t")
if (letter1ID == 40 and letter2ID != letter1ID):
	letter1 = str("u")
if (letter1ID == 41 and letter2ID != letter1ID):
	letter1 = str("U")
if (letter1ID == 42 and letter2ID != letter1ID):
	letter1 = str("v")
if (letter1ID == 43 and letter2ID != letter1ID):
	letter1 = str("V")
if (letter1ID == 44 and letter2ID != letter1ID):
	letter1 = str("w")
if (letter1ID == 45 and letter2ID != letter1ID):
	letter1 = str("W")
if (letter1ID == 46 and letter2ID != letter1ID):
	letter1 = str("x")
if (letter1ID == 47 and letter2ID != letter1ID):
	letter1 = str("X")
if (letter1ID == 48 and letter2ID != letter1ID):
	letter1 = str("y")
if (letter1ID == 49 and letter2ID != letter1ID):
	letter1 = str("Y")
if (letter1ID == 50 and letter2ID != letter1ID):
	letter1 = str("z")
if (letter1ID == 51 and letter2ID != letter1ID):
	letter1 = str("Z")
if (letter1ID == 52 and letter2ID != letter1ID):
	letter1 = str("0")
if (letter1ID == 53 and letter2ID != letter1ID):
	letter1 = str("1")
if (letter1ID == 54 and letter2ID != letter1ID):
	letter1 = str("2")
if (letter1ID == 55 and letter2ID != letter1ID):
	letter1 = str("3")
if (letter1ID == 56 and letter2ID != letter1ID):
	letter1 = str("4")
if (letter1ID == 57 and letter2ID != letter1ID):
	letter1 = str("5")
if (letter1ID == 58 and letter2ID != letter1ID):
	letter1 = str("6")
if (letter1ID == 59 and letter2ID != letter1ID):
	letter1 = str("7")
if (letter1ID == 60 and letter2ID != letter1ID):
	letter1 = str("8")
if (letter1ID == 61 and letter2ID != letter1ID):
	letter1 = str("9")
if (letter1ID == 62 and letter2ID != letter1ID):
	letter1 = str(",")
if (letter1ID == 63 and letter2ID != letter1ID):
	letter1 = str(".")
if (letter1ID == 64 and letter2ID != letter1ID):
	letter1 = str("!")
if (letter1ID == 65 and letter2ID != letter1ID):
	letter1 = str("@")
if (letter1ID == 66 and letter2ID != letter1ID):
	letter1 = str("#")
if (letter1ID == 67 and letter2ID != letter1ID):
	letter1 = str("$")
if (letter1ID == 68 and letter2ID != letter1ID):
	letter1 = str("!")
if (letter1ID == 69 and letter2ID != letter1ID):
	letter1 = str("%")
if (letter1ID == 70 and letter2ID != letter1ID):
	letter1 = str("^")
if (letter1ID == 71 and letter2ID != letter1ID):
	letter1 = str("&")
if (letter1ID == 72 and letter2ID != letter1ID):
	letter1 = str("*")
if (letter1ID == 73 and letter2ID != letter1ID):
	letter1 = str("=")
if (letter1ID == 74 and letter2ID != letter1ID):
	letter1 = str("-")
if (letter1ID == 75 and letter2ID != letter1ID):
	letter1 = str("+")
if (letter1ID == 76 and letter2ID != letter1ID):
	letter1 = str("_")
if (letter1ID == 77 and letter2ID != letter1ID):
	letter1 = str("?")
if (letter1ID == 78 and letter2ID != letter1ID):
	letter1 = str("<")
if (letter1ID == 79 and letter2ID != letter1ID):
	letter1 = str(">")
if (letter1ID == 80 and letter2ID != letter1ID):
	letter1 = str("~")
if (letter1ID == 81 and letter2ID != letter1ID):
	letter1 = str("`")
if (letter1ID == 82 and letter2ID != letter1ID):
	letter1 = str("\"")
if (letter1ID == 83 and letter2ID != letter1ID):
	letter1 = str("/")
if (letter1ID == 84 and letter2ID != letter1ID):
	letter1 = str(":")
if (letter1ID == 85 and letter2ID != letter1ID):
	letter1 = str(";")
letter3ID = random.randint(0, 512)
if (letter3ID == 0 and letter3ID != letter2ID):
	letter3 = str("a")
if (letter3ID == 1 and letter3ID != letter2ID):
	letter3 = str("A")
if (letter3ID == 2 and letter3ID != letter2ID):
	letter3 = str("b")
# Stopping here for now until I find a more efficient method. There HAS to be a better way to do this.
# Row 1-12
print (str(letter1) + " " + str(letter2) + " " + str(letter3) + " " + str(letter4) + " " + str(letter5)) # Each one of these should print smaller than the previous one. I don't currently know how to do this in Python
print (str(letter6) + " " + str(letter7) + " " + str(letter8) + " " + str(letter9) + " " + str(letter10))
print (str(letter11) + " " + str(letter12) + " " + str(letter13) + " " + str(letter14) + " " + str(letter15))
print (str(letter16) + " " + str(letter17) + " " + str(letter18) + " " + str(letter19) + " " + str(letter20))
print (str(letter21) + " " + str(letter22) + " " + str(letter23) + " " + str(letter24) + " " + str(letter25))
print (str(letter26) + " " + str(letter27) + " " + str(letter28) + " " + str(letter29) + " " + str(letter30))
print (str(letter31) + " " + str(letter32) + " " + str(letter33) + " " + str(letter34) + " " + str(letter35))
print (str(letter36) + " " + str(letter37) + " " + str(letter38) + " " + str(letter39) + " " + str(letter40))
print (str(letter41) + " " + str(letter42) + " " + str(letter43) + " " + str(letter44) + " " + str(letter45))
print (str(letter46) + " " + str(letter47) + " " + str(letter48) + " " + str(letter49) + " " + str(letter50))
print (str(letter51) + " " + str(letter52) + " " + str(letter53) + " " + str(letter54) + " " + str(letter55))
print (str(letter56) + " " + str(letter57) + " " + str(letter58) + " " + str(letter59) + " " + str(letter60))
print ("Eye chart (Opochart) - Advanced Eye Chart plus (early Alpha build 1.00)")
def export():
	print ("Export command is coming soon")
print ("Export?")
print ("The eye chart has finished rendering. Use it for as long as you want, then you can quit")
noMore = input("Press [ENTER] key to quit"))
print ("The program should now be closed. If the program is still open, press the close button. If this doesn't work, use a process manager/task manager and end the task/process")
"""

[file:///markdown/fileinfo.md](file:///markdown/fileinfo.md])

# File info

File version: 1 (Tuesday, December 29th 2020 at 8:29 pm)

File type: Python script file (*.py)

Line count (including blank lines and compiler line): 400

"""
# End of script
