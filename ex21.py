# addition with printing the operation
def add(a, b):
    #print(">>>ADD(a, b)=", a, b)
    print(f"Adding {a} + {b}")
    #print("<<<ADD", a + b)
    return a + b
   

# subtraction with printing the operation
def subtract(a, b):
    #print(">>>SUB(a, b)=", a, b)
    print(f"Subtracting {a} - {b}")
    #print("<<<SUB", a - b)
    return a - b

# multiplication with printing the operation
def multiply(a, b):
    #print(">>>MUL(a, b)=", a, b)    
    print(f"Multiplying {a} * {b}")
    #print("<<<MUL", a * b)
    return a * b

# division with printing the operation
def divide(a, b):
    #print("DIV(a, b)=", a, b)    
    print(f"Dividing {a} / {b}")
    #print("<<<DIV", a / b)
    return a / b

print("\nLet's do some moth with just functions.")

# do the operations on numers using functions above
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# print the results
print(f"\nage: {age}, height: {height}, weight: {weight}, IQ: {iq}")

print("\nHere is a puzzle")

# solve the equation using the functions
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# the same thing below
div = divide(iq, 2)
mul = multiply(weight, div)
sub = subtract(height, mul)
ad = add(age, sub)
print(f"\nThe result:", ad, "\n")

# printing the result
print("\nThat becomes", what, "Can you do it by hand?")

# inne równanie poniżej
print("\nAnother operation : (3 +(61*4))/(8-1).")

print(f"\nResult: ", add(float(input("Give me the number: ")), divide(multiply(61, 4), subtract(8, 1))), "\n")


