from sys import argv

script, day, month, year = argv

this_year = int(input(f"So you were born {day} {month} year {year}. What year do we have now?\n"))

age = this_year - int(year)  

input(f"If we have {this_year} and you were born {day} {month} year {year} you should be {age} years old.\nAm i right?\n")
print(";)\n")
