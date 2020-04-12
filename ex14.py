from sys import argv # importing the argv feature from the sys module

script, user_first_name, user_surname = argv # assigning the input for argv to the variables
prompt = 'Your answer: '

print(f"Hi {user_first_name}. Your surname is {user_surname}? Sounds funny to me.\nI'm {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_first_name}?")
likes = input(prompt)

print(f"Where do you live {user_first_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Ok. So you said "{likes}"" about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")