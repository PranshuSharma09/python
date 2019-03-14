#! /usr/bin/python3
num = int(input("Enter number:"))
for i in range (2, 20):
	if num == i:
		for e in range(1, 11):
			print("%d X %d = %d" %(num, e, num*e))

