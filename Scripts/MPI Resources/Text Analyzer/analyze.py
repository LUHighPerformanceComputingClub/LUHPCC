# A simple single-core text analyzer to find a given keyword in a text
# Made by Noah Harris for HPCC

import time

file = open("script.txt", "r")
#file = open("bible.txt", "r")

# get entire script to parse
script = file.read()

keyword = "bee"
found = 0

start = time.time()
for i, char in enumerate(script):
	if char == keyword[0]: # if found first char in keyword
		if keyword in script[i:i+len(keyword)]: # if keyword in this section
			found += 1

end = time.time()
print("We found", found, "many", keyword + "\'s in this script!")
print("This script took", end-start, "many seconds to run.")
