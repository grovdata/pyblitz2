import sys
from sets import Set

keywords = open(sys.argv[1], "r").readlines()

keywords = map(lambda x: x.strip(), keywords)
keywords = map(lambda x: x.replace("()", ""), keywords)

unique = Set(keywords)
sortedList = sorted(list(unique))

for kw in sortedList:
	print kw