import os
import sys

def spam(devideby):
	try:
		return 42 / devideby
	except ZeroDivisionError:
		print("Invalid argument")
		sys.exit()

devideby = int(input("enter a numvber to divide 42:"))

print(spam(devideby))
