from sys import argv

# assign the input file name to the variable
script, input_file = argv

# function taking object file and printing the file
def print_all(f):
    print(f.read())

# function taking an object file and moving the cursor back to the begining of the file
def rewind(f):
    # offset the cursor by 0 from teh begining of the file (begining of the file - default 0 value of the second parameter)
    f.seek(0)

# function taking the number and an object file, printing the number and the next line of a text
def print_a_line(line_count, f):
    # print the number, the next line of a text and finish printing with no "\n" sign
    print(line_count, f.readline(), end = "")

# open the file
current_file = open(input_file)

print("\nFirst let's print the whole file:\n")

# print the whole file
print_all(current_file)

print("\nNow let's rewind it kind of like a tape.")

# rewind the file
rewind(current_file)

print("Let's print three lines:\n")

# print the first line
current_line = 1
print_a_line(current_line, current_file)

# print the second line
current_line += 1
print_a_line(current_line, current_file)

# print the third line
current_line += 1
print_a_line(current_line, current_file)

# rewind the file again
rewind(current_file
