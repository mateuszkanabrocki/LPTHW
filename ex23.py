# importing the whole system module
import sys
# assign the script input arguments to the variables - encoding type and dealing with errors method
script, input_encoding, error = sys.argv

# print the text file line by line in a loop
def main(language_file, encoding, errors):
    # assign a single line of the input file to the variable "line"
    line = language_file.readline()

    # if there is a line print it
    # if the text is finished the readline function returns the empty string -> value 0
    if line:
        # prints the encoded line and the decoded bytes string
        print_line(line, encoding, errors)
        # runs the main function again (in a loop) - caret changes its position in every step
        return main(language_file, encoding, errors)

# gets line of a text, type of encoding, prints the encoded and encoded+decoded line
def print_line(line, encoding, errors):
    print(">>>>>>", line, "<<<<", repr(line))
    # get a copy of the line with no leading and trailing characters
    next_lang = line.strip()
    # encode the line
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # decode the line of bytes (it's not a string)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

# open the .txt file encoded in utf-8 using utf-8 encoding (after opening the text we have a file with symbols)
languages = open("languages_short.txt", encoding="utf-8")
#languages = open("languages_ansi.txt", encoding="ansi")

# run main function on the opened .txt file, with specified encoding, and dealing with errors method
main(languages, input_encoding, error)
