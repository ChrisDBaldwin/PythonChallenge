# Python Challenege 5
# Chris Baldwin
# Completed
# Strategy: 
# Use pickle module to unpickle the data from the banner in the html source
# Got an array of arrays of tuples
# The tuples are # or ' ' and a number
# print the character number times
# get an old school unix banner
# banner says: channel

import pickle

# Open file containing pickled text
f = open('pickle.txt', 'r')

banner = []

def main():	
	data = pickle.load(f)
	for item in data:
		for tup in item:
			x, y = tup
			banner.append(x*y)
		banner.append('\n')

	print "".join(banner)

if __name__ == '__main__':
	main()