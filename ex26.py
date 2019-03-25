from sys import argv
# assign a filename to a variable
script, filename = argv

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


# ask for age, height and weight
age = input("\nHow old are you?\n>")
height = input("\nHow tall are you?\n>")
weight = input("\nHow much do you weigh?\n>")

print(f"\nSo, you're {age} old, {height} tall and {weight} heavy.\n")


# print text from the file
print(f"Here's your file {filename}:\n")
print(open(filename).read())

# ask for another filename
file_again = input("\nType the filename again:\n>")
print("/n")
print(open(file_again).read())


print("""
Let's practice everything.
You\'d need to know \'bout escapes
with \\ that do \nnewlines and \t tabs.
""")

poem = ("""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
""")

# print a poem
print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# calculation formula
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.\n".format(*formula))


people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people > dogs:
   print("People are greater than dogs.")

if people < dogs:
   print("People are less than dogs.")

if people == dogs:
   print("People are dogs.")