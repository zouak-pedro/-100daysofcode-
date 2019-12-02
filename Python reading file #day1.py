'''
it is my first day in challenge. i jest reading file from python, i use python the hard way .ex15 
'''
from sys import argv 

ex15_sample = argv

txt = open("ex15_sample.txt","r")
print("Here's youre file",(txt.name)" :")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
text_again = open(file_again,"r+") 
#with open(file_again,"r") as text_again:
#	print(text_again.read())

print(text_again.read())
text_again.close()
