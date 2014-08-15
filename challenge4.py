# Python Challenege 4
# Chris Baldwin
# Completed
# Strategy: 
# open each ?nothing= and extract the last word from the string on the page
# the last word is a new number to the next nothing
# around 400 iterations reveals the answer
# Answer: peak.html


import urllib

def main():
	nothing = '12345'
	baseURL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
	nextURL = baseURL + nothing
	
	i = 0
	for i in xrange(400):
		f = urllib.urlopen(nextURL)
		nothing = f.read(400).split()[-1]
		print nothing
		nextURL = baseURL + nothing


if __name__ == '__main__':
	main()