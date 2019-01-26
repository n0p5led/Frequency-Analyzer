import sys

def countBytes(encrypted):
	# We create a list that saves 256 zeroes. Each one represents a different byte
	chars = []
	for i in range(0,256):
		chars.append([i,0])

	# We save the decimal value of each byte in a list
	content = []
	for byte in encrypted:
		content.append(ord(byte))

	# We count each byte and we apply +1 to the cell that represents that byte
	for byte in content:
		chars[byte][1] += 1

	# Now we return the repetition of a byte
	return chars

def sortBytesByFrequency(countedBytes):
	for i in reversed(range(1,256)):
		for j in reversed(range(256)):
			if countedBytes[j][1] == i:
				print "Char :" + str(countedBytes[j][0]) + " (" + chr(countedBytes[j][0]) + "): " + str(countedBytes[j][1]) + " times."


encrypted = open(sys.argv[1],"r").read()
sortBytesByFrequency(countBytes(encrypted))
