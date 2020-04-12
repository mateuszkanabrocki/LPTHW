age = input("How old are you?\n")
# printing a question using the previous input -> age and taking the another input
height = input(f"You are {age} years old? Nice. How tall are you?\n") 
weight = input("How much do you weight?\n")

# printing the f-string using all the variables previously collected from the input
print(f"So, you're {age} years old, {height} tall and {weight} heavy.") 

# won't get the input - unfortunately doesn't work like that
# well it seems to work now :)
print("Input?" , input("hehe")) 
