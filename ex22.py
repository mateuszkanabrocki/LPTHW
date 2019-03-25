# importing the whole system module
import sys
# assign the script input arguments
script, input_encoding, error = sys.argv

# print the text file line by line in a loop
def main(language_file, encoding, errors):
    # assign a single line of the input file to the variable "line"
    line = language_file.readline()

    # if there is a line print it(?)
    if line:
        print_line(line, encoding, errors)
        #runs the main function again - caret changed its position
        return main(language_file, encoding, errors)

# gets line of a text, type of encoding, prints the encoded and encoded+decoded line
def print_line(line, encoding, errors):
    # get a copy of the line with no leading and trailing characters
    next_lang = line.strip()
    # encode the line
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # decode the line
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

# open the .txt file using utf-8 encoding/decoding
languages = open("languages1.txt", encoding="utf-8")

# run main function on the opened .txt file, with specified encoding
main(languages, input_encoding, error)
