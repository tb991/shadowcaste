import io
import sys

# this is called shadowcaste

filetext = sys.argv[1:]
filetext = filetext[0][:]
charlist = []

# create a set of the unique symbols in filetext
for x in filetext:
	if not x in charlist:
		charlist.append(x)

length = len(charlist)

# return the reversed/mirrored index of the char in the set listchars
def index(listchars, char):
	return len(listchars) - (listchars.index(char) + 1)

out = ""
# for every character you find in the text, swap it with a mirrored one
# from the set of unique symbols
for character in filetext:
	newchar = charlist[index(charlist, character)]
	out += newchar

print(out, end="")
