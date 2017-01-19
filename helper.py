def parseCSV(s):
	retarray = []
	insidequote = False
	curvalue = ""
	for ch in s:
		if ch == ',':
			if insidequote:
				curvalue += ch
			else:
				retarray.append(curvalue)
				curvalue = ""
		elif ch == '"':
			insidequote = not insidequote
		else:
			curvalue += ch
	retarray.append(curvalue)
	return retarray

if __name__ == "__main__":
	y = parseCSV("""this,is, the way of the cat,"and, sadly, my dog",and you!""")
	x = parseCSV(""",,,,!""")
	for j in y:
		print("/" + j + "/")
