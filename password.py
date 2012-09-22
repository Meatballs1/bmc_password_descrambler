#!/usr/bin/python
from array import *
import sys

if len(sys.argv) != 2:
	print "# BMC Remedy Password Descrambler"
	print "# Author: Meatballs"
	print "# Usage: ./password.py ciphertext"
else:
	cipherText = sys.argv[1]
	print "CipherText: " + cipherText

	cipher = array('c', 'kszhxbpjvcgfqntm')
	plainText = "PlainText: "
	i = 0

	while i < len(cipherText):
		x = cipher.index(cipherText[i]) * 16
		i += 1
		y = cipher.index(cipherText[i]) % 16
		x = x + y 
		plainText += chr(x)
		i += 1

	print plainText
	
