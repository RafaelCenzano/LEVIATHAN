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

message_to_change = input ('What message would you like to encrypt  ')
time.sleep(0.5)
a = G

print(rot13(message_to_change))
print('Key: {}').format(a)

#This code allows you to see the original untoched message
#print(rot13(rot13(message_to_change)))
#This code can be used to decypher messages
