class Parent(object):

    def  function1(self):
        print("It's a parent function")

class Child(Parent):

    def function1(self, name):
        print("It's a child function")
    
    def function1(self):
        print("It's a second child function")

dad = Parent()
son = Child()
son = Child()

dad.function1()
son.function1('name')