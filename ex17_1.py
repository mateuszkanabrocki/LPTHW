from sys import argv
from os.path import exists

script, from_file, to_file = argv

# get the text of the from_file # first open the file for writing, read it and assign to indata variable
#indata = open(from_file).read()
# copy from_file to in_file # first open to_file for writing # heard python closes the files after this operation - don't need to close them
open(to_file, "w").write(open(from_file).read())

