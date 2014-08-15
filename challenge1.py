# Python Challenge 1
# Chris Baldwin
# Completed
# The easy way to do this is with string maketrans()
# Strategy: set up the alphabet and the cipher key
# for each character in the string, if the character is a letter, find its location in the alphabet
# then print the letter from the key at that location
# the STRING says:
# "i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient
# and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
# the url was map.html
# answer: ocr

ALPHA = "abcdefghijklmnopqrstuvwxyz"
KEY = "cdefghijklmnopqrstuvwxyzab"
STRING = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
URL = "map"

def main():
	translation = ""
	for char in STRING:
		if char in ALPHA:
			index = ALPHA.find(char)
			translation += KEY[index]
		else:
			translation += char
	print translation

if __name__ == '__main__':
	main() 