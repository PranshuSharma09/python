#! /usr/bin/python3

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a number between 1-5: "))
if c == 1:
    print("a + b = ", a+b)
elif c == 2:
    print("a - b = ", a-b)
elif c == 3:
    print("a * b = ", a*b)
elif c == 4:
    print("a / b = ", a/b)
elif c == 5:
    for i in range(1,11):
        print("%d X %d = %d" %(a, i, a*i))

