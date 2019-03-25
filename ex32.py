the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first type of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type {fruit}")

# also we can go through mix lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range funtion to do 0 to 5 counts
for i in range(1, 5, 1):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
#elements.append(range(1, 5, 1))

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

n_list = ["Happy", [2,0,1,5]]
print(n_list[0][1:-2])