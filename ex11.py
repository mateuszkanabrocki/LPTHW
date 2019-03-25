print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weight?", end=" ")
weight = input()

print(f"So you're {age} years old, {height} tall and {weight} heavy.")

before_age = int(age) - 10
print("10 years ago you were {}".format(before_age))
print(f"10 years ago you were {repr(before_age)}")