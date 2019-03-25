# defining a function with 2 arguments
def cheese_and_crackers(chesse_count, boxes_of_crackers):
    #print(">>> START chesse_count=:", chesse_count, "boxes_of_crackers:", boxes_of_crackers)
    print(f"You have {chesse_count} cheeses.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")
    #print("<<< END")

print("We can just give the function numbers directly:")
# function with number arguments
cheese_and_crackers(20, 10)

print("OR, we can use variables from our script:")
# defining variables
amount_of_cheese = 24
amount_of_crackers = 31

# function with given 2 arguments - variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too")
# function with given two arguments - mathematic operations
cheese_and_crackers(10+20, 3+13)

print("We can combine the two, variables and math:")
# function with given 2 arguments - math operations on variables and numbers
cheese_and_crackers(amount_of_cheese + 2, amount_of_crackers + 9)
