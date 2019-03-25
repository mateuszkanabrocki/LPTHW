# from the system module import the argv feature
from sys import argv

# assign given input values to the variables
script, filename = argv 

# assign the file to the variable
txt = open(filename) 


print(f"Here is your file {filename}: \n\n")
# read the content of the file and print it
print(txt.read())
# closing the opened file after using it
txt.close() 

# ask again for the filename
print("type the filename again: \n")
# assign the given filename to the variable
file_again = input(">  ")
# assign the file (file object) to the variable
text_again = open(file_again) 

# read the content of the file and print it
print(text_again.read())
# closing the opened file after using it
text_again.close() 

# print((open(input("> "))).read())
