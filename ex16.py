# import the argv feature from system module
from sys import argv

# assign the input values to the variables (strings)
script, filename = argv

print(f"We're going to erase {filename}.") 
print("If you don't want that hit Ctrl-C (^C).")
print("If you do want that hit RETURN.")

input("?")

print("Opening the file...")
# open the file "filename" for writing (assign the file - it's coordinates in file object - to "target" variable
target = open(filename, "w")

print("Truncating the file. Goodbye!")
# removing the contents of the file
# target.truncate() # don't have to do it, already truncated the file by opening it in "w" mode

print("Now I'm going to ask you for three lines.")

# assign 3 input lines to 3 variables
line1 = input("line1:\n")
line2 = input("line2:\n")
line3 = input("line3:\n")

print("I'm going to write these to the file.")

# write these inputs to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# close the file
target.close()