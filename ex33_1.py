i = 0
j = 12
increment = 3
numbers = []

def function(i, j, increment, numbers):
    if i < j:
        numbers.append(i)
        i+= increment
        function(i, j, increment, numbers)
    return numbers

function(i, j, increment, numbers)   

print("\nThe numbers:")

for num in numbers:
    print(num)
