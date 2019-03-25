# connect string with a variable
formatter = "{} {} {} {}" 

# formatting the formatter string using function format -> using int, strings, true/false, formatter strings and another string at the end.
print(formatter.format(1, 2, 3, 4)) 
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Just", 
    "typing", 
    "something", 
    "here."
))