import sys

kwToToken = dict()
tokenToKw = dict()

def load_mapfile(filename):
	mapfile = open(filename, "r")
	lines = mapfile.readlines()

	for line in lines:
		#print line
		if not ("###" in line):
			keyword, tokenStr = line.split(" = ")
			token = tokenStr.strip().decode("hex")
			kwToToken[keyword] = token
			tokenToKw[token] = keyword

def save(data):
	out = str()
	lines = data.split('\n')
	for line in lines:
		newLine = line
		words = line.split(' ')
		for word in words:
			if word in kwToToken.keys():
				newLine = newLine.replace(word, kwToToken[word])
		out += newLine + '\00'
	print '\00\00'
	print out

if __name__ == '__main__':
	# Usage: blitz.py mapfile infile outfile
	load_mapfile(sys.argv[1])
	save(open(sys.argv[2], "r").read())