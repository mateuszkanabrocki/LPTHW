# break
def break_test():

    for i in "abcdefghijklmnopqrstuvwxyz":
        if i == "j":
            break
        print(i, end="")
    print("!")

# with-as
# open file and close it automatically
def with_as_file_test():

    # "file" is a local variable
    with open("with_as_test.txt") as file:
        print(file.readline(), end="")
    print(file.closed)

# open, close, use file, hm
def file_op1():
    files = []
    for x in range(10000):
        f = open('foo.txt', 'w')
        f.close()
        files.append(f)

# pass
def pass_test():
    for letter in 'Python': 
        if letter == 'h':
            pass
            print('This is pass block')
        print("Current Letter :", letter)

# assert
def assert_test():

    for i in "Python":
        assert i != "o", "There is an 'o' in 'Python'!"
        print(i, end="")

    for i in "Python":
        assert i != "o"
        print(i, end="")

# continue
def continue_test():

    tuple = [1, 3, -2, -5, 7]
    sum = 0
    # sum of the positive numbers only
    for i in tuple:
        if i > 0:
            sum = sum + i
        else:
            #continue to the next for iteration
            continue
        print(f"Found a positive number!: {i}")
    print("sum: {}".format(sum))

#try, except, finally
def except_finally_test():

    # x = 1
    try:
        print(x)
    except NameError as error:
        print(f"Watch out! {error}")
    finally:
        print("\nException or not I'll print it. Don't matter what.\n")

    print("Something")

#exec
def exec_test():

    program = 'a = 5\nb=10\nprint("Sum =", a+b)'
    #execute program written as a string
    exec(program)

# lambda
def lambda_test():

    y = lambda a, b : 2*a + 9*b +3
    print(y(2, 3))

# raise
def raise_test():

    x = -1

    if x < 0:
        # raise Expetion error or other chosen + a written comment
        raise Exception("Sorry, this number is below zero.") 

# yield
def yield_test():

    def make_generator():
        for i in range(4):
            # create a generator as a return - not  a simple tuple
            yield i*i

    # get the return - a generator
    mygenerator = make_generator()

    # print generator elements one by one
    print(mygenerator)
    for i in mygenerator:
        print(i)


except_finally_test()