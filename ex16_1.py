from sys import argv

# assign the 2nd argv value to the filename variable
script, filename = argv

print(f"Do you want to delete the contents of the {filename} file?")
print("If NOT press CTRL-C.\n")
input()

print("Opening the file...\n")
# open the file for writing and assign it to taget_file variable    
target_file = open(filename, "r+")

print("Deleting the contents of the file...\n")
# truncate the file
target_file.truncate()

print(f"Do you want to write the new contents of the {filename} file?")
print("If NOT press CTRL-C.\n")
input()

# get new file contents from the input
line1 = input("Type the first line of the text file:\n")
line2 = input("Type the second line of the text file:\n")
line3 = input("Type the third line of the text file:\n")

print("\nWriting new contents to the file...\n")

# write new file contents
# target_file.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
#target_file.write(f"{line1}\n{line2}\n{line3}\n")
target_file.write("{}\n{}\n{}\n".format(line1, line2, line3))

#close the file
target_file.close()

print(f"Do you want to read the new {filename} file?")
print("If NOT press CTRL-C.\n")
input()

# open the file again but this time for reading and print it right away
target_file = open(filename, "r")
#target_file = open(filename, "r")
print(target_file.read())
target_file.close()

print("\nHave a nice day.")
