import sys
import pprint

# Tokens
#
# The Blitz 2 editor stores all the BASIC keywords as tokens, these
# tokens are 16 bit numbers encoding which library the BASIC keyword
# comes from and an offset detailing where in the library the keyword's
# ASCII name, help information and compile time code can be found.
#
# Because the user can configure Blitz 2 to use some libraries and not
# others problems can arise when a program's source code includes tokens
# that are not available in the libraries that Blitz 2 loaded when it
# was run. The error Token Not Found $xxxx signals the token code it
# was unable to locate.
#
# Each library can include 128 statements and functions. The token
# code uses the lower 7 bits for which function/ statement it is
# and the upper 9 bits to signify which library the token came from.

def isNotCrap(b):
	return b not in ['\x00', '\x20']

def isTokenOrLib(b):
	return ord(b) & 128 == 128

kwfile  = open(sys.argv[1], "r")
bb2file = open(sys.argv[2], "rb")

kwToToken = dict()
tokenToKw = dict()

kwLines = kwfile.readlines()
kwLines = map(lambda x: x.strip(), kwLines)
kwLines = map(lambda x: x.replace("()", ""), kwLines)

temp = bb2file.read()
bbdata = str()

for x in temp:
	if isNotCrap(x):
		bbdata = bbdata + x
bbdata = list(bbdata)

try:
	i = 0
	#word = bb2file.read(2)
	while True:
		b1 = bbdata.pop(0)
		if isTokenOrLib(b1):
			b2 = bbdata.pop(0)
			kwToToken[kwLines[i]] = b1 + b2
			i += 1

except Exception, e:
	print e
finally:
	kwfile.close()
	bb2file.close()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(kwToToken)
