#! /usr/bin/python3

marks = int(input("Enter Marks: "))
if marks < 30:
	print("Grade D")
elif marks >= 30 and marks < 50:
	print("Grade C")
elif marks >= 50 and marks < 70:
	print("Grade B")
elif marks >= 70:
	print("Grade A")
