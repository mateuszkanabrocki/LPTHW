# create a class named Parent - base class of class
class Parent(object):

    def override(self):
        print("PARENT override()", self)

    def implicit(self):
        print("PARENT implicit()", self)

    def altered(self):
        print("PARENT altered()", self)

# create a class named Child which is-a (inherits form) Parent class
class Child(Parent):

    # create a function with the same name as in parent class
    # this function overrides the parent function
    def override(self):
        print("CHILD override()", self)

    def altered(self):
        print("CHILD, BEFORE PARENT altered()", self)
        # call super-class (parent-class)
        # with Child and self parameters and call it's altered function
        print(">>>", self)
        super(Child, self).altered()
        print("<<<", self)
        # after calling this function it continue to execude Child's altered function 
        print("CHILD, AFTER PARENT altered()", self)

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()



#class Child(Parent):

    # initialize Child attributes
    #def __init__(self, stuff):
        # assign input data called stuff to self.stuff
        #self.stuff = stuff
        # get other attributes by calling the super-class
        #super(Child, self).__init__()
    
    #def override(self):
        #print("CHILD overriiiiiiide()")

