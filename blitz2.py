from bb2map import keyWordToToken
import sys

def saveBlitz(data):
	out = str()
	lines = data.split('\n')
	for line in lines:
		newLine = line
		words = line.split(' ')
		for word in words:
			if word in keyWordToToken.keys():
				newLine = newLine.replace(word, keyWordToToken[word])
		out += newLine + '\n'
	print out

if __name__ == '__main__':
	if sys.argv[1] == '-s':
		saveBlitz(open(sys.argv[2], "r").read())