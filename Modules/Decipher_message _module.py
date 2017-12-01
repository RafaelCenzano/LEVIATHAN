#!/usr/local/bin/python3
import time

def rot13(s):
	result = ""
	for v in s:
		c = ord(v)

		if c >= ord('a') and c <= ord('z'):
			if c > ord('m'):
				c -= 13
			else:
				c += 13
		elif c >= ord('A') and c <= ord('Z'):
			if c > ord('M'):
				c -= 13
			else:
				c += 13

		result += chr(c)

	return result

message_to_change = input ('What message would you like to decipher  ')
message_key = input ('Key:  ')
time.sleep(0.5)
if message_key = G
    print(rot13(message_to_change))

else:
    print("I don't know the key you typed")
    exit()
#This code allows you to see the encrypted message
#print(rot13(rot13(message_to_change)))
#This code can be used to encode and decipher any message.
