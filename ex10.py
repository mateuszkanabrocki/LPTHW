tabby_cat = "\n\tI'm tabbed in."
persian_cat = "I'm split\non a line. "
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print(f"Let's print some stuff!\n {'We'} are going to use the sequence escapes\n\t like this and some\n\t\t\r more over here.\a")

print("Let's print some stuff!\n {} are going to use the sequence escapes\n\t like this and some\n\t\t\r more over here.\a".format('we'))