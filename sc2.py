import io

# this is called shadowcaste

a = io.open("shadow2text.txt", "r")
filetext = a.read()
charlist = []

for x in filetext:
	if not x in charlist:
		charlist.append(x)

length = len(charlist)

def index(listchars, char):
	return len(listchars) - (listchars.index(char) + 1)

out = ""
for character in filetext:
	newchar = charlist[index(charlist, character)]
	out += newchar

print(out)
