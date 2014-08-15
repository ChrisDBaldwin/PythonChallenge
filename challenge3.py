# Python Challenge 3
# Chris Baldwin
# Completed
# Strategy: regular expressions to find all instances of exactly 3 upper case surrounding 1 lowercase
# the middle characters spell out the answer
# answer: linkedlist

import re

# Open file
f = open('dump3.txt', 'r')

def main():
	searchObj = re.findall(r'[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', f.read())
	
	if searchObj:
		print searchObj
	else:
		print "nothing found :<"

if __name__ == '__main__':
	main()