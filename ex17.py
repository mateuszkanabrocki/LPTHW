from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"\nCoping from {from_file} to {to_file}.\n")

# we can do this 2 lines on 1, how?
# open the from file file and save it to in_file variable
in_file = open(from_file)
# read the contents of the file and save it to indata variable
indata = in_file.read()

# print the lenght of the indata (text) - number of bytes/letters?
print(f"The input file in {len(indata)} bytes long.\n")

# check if the output file exists
print(f"Does the output file exist? {exists(to_file)}\n")
print("Ready. Press RETURN to continue or CTRL-C to abort.\n")
input()

# open the to_file and save it to open_file variable
out_file = open(to_file, "w")
# copy the indata to the out_file
out_file.write(indata)

print("Allright, all done.")

# close the files
out_file.close()
in_file.close()