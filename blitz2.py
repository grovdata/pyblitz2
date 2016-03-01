import sys
import StringIO

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

def save(data, outfile):
	data = data.replace('\n', '\x00')

	inf = StringIO.StringIO(data)
	of  = open(outfile, "wb")
	word = ''
	eow = [' ', '(', '\x00']

	while True:
		c = inf.read(1)

		if not c:
			break

		if c not in eow:
			word += c
		else:
			if word in kwToToken.keys():
				of.write(kwToToken[word])
			else:
				of.write(word)
			word = ''
			of.write(c)

	of.write('\x00')
	inf.close()
	of.close()

if __name__ == '__main__':
	# Usage: blitz.py mapfile infile outfile
	load_mapfile(sys.argv[1])
	save(open(sys.argv[2], "r").read(), sys.argv[3])