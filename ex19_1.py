def my_function(arg1, arg2):
    print(f"""
    Hello, {arg1}.
    You just gave me {repr(arg2)} cookies.
    Nice of you.
    """)

my_function("Mateusz", 4)

name = "Mateusz"
amount_of_cookies = 4
my_function(name, amount_of_cookies)

all_the_cookies = 6
eaten_cookies = 2
my_function("Mateusz"+"Kanabrocki", all_the_cookies - eaten_cookies)

my_function(input("name: "), amount_of_cookies)

my_function(input("name: ") * 2, amount_of_cookies)

my_function(input("name: "), int(input("cookies: ")))

my_function(open("ex1.py").read(), int(input("cookies: ")))