from sys import argv
from os.path import exists

script, from_file, to_file = argv

# copy from_file to to_file

# get the text of the from_file
# first open the file for reading, read it and assign to indata variable
# indata = open(from_file).read()
# open(to_file, "w").write(indata)

# shorter way
# heard python closes the files after this operation - don't need to close them
# not sure though, maybe it works only in e.g CPython?
open(to_file, "w").write(open(from_file).read())
