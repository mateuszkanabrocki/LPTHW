import sys
script, input_encoding, error = sys.argv 

# print the byte string file line by line in a loop
def main(language_file, encoding, errors):
    # assign a single line of the input file to the variable "line"
    line = language_file.readline()

    # if there is a line print it
    # if the file is finished the readline function returns the empty string -> value 0
    if line:
        # prints the encoded line and the decoded bytes string
        print_line(line, encoding, errors)
        # runs the main function again (in a loop) - caret changes its position in every step
        return main(language_file, encoding, errors)

# gets line of bytes strings, type of encoding, prints the decoded and decoded+encoded line
def print_line(line, encoding, errors):
    # get a copy of the line of bytes strings strings with no leading and trailing characters (actually there are no leading characters)(SHOULD JUST CONVERTS STING OF STRING BYTES INTO STRING OF BYTES WITH, AND THEN DECODE IT WITH NO ENCODING)
    next_lang = line.strip()
    #next_lang = next_lang.strip("'")
    #next_lang = next_lang.strip("b'")
    #next_lang = next_lang.strip()
    #next_lang = next_lang.strip("b'")
    #print(">>>> ", next_lang) # get a string of bytes
    next_lang = next_lang.replace("b'", "")
    next_lang = next_lang.strip("'")
    next_lang = next_lang.replace("\\x", "0x")
    print(">>>> ", next_lang)
    # decode the string bytes into bytes
    next_lang_bytes = 
    cooked_string_bytes = next_lang_bytes.decode(encoding, errors=errors) # I GUESS I DOESN'T CONVERT STRINGS INTO BYTES STRINGS BUT INTO SOMETHING MESSY, BUT GOOD TRY THOUGH ^^
    print(f"<<<<<<<<<<{cooked_string_bytes}")
    #cooked_string = cooked_string_bytes.decode(encoding, errors=errors)
    # encode the line
    #raw_bytes = cooked_string.encode(encoding, errors=errors)
    #print(raw_bytes, "<===>", cooked_string)

# open the .txt file encoded in utf-8 using utf-8 encoding (after opening the text we have a file with bytes strings)
languages = open("languages_short_bytes.txt", encoding="utf-8")
#languages = open("languages_ansi.txt", encoding="ansi")
#print(">>>>>>>>>>", languages.read())
# run main function on the opened .txt file, with specified encoding, and dealing with errors method
main(languages, input_encoding, error)