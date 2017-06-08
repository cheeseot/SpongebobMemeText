try:
	from Tkinter import Tk
except ImportError:
	from tkinter import Tk
import random
import time

memeInput = input("Text to memeify: ")
print(memeInput)
random.seed(time.time())
memeOutput = list(memeInput)
for count in range(0,len(memeInput)):
	

	x = random.randrange(0,100000001)%2
	#print(x)
	if(memeInput[count] != " "):
		if x == 0:
			#print("0")
			memeOutput[count] = memeInput[count].upper()
			x = 1
		elif x == 1:
			#print("1")
			memeOutput[count] = memeInput[count].lower()
			x = 0
	#print(memeOutput[count])

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append("".join(memeOutput))
print("".join(memeOutput))
pause = input("Meme Text copied to clipboard... Press enter to exit...")