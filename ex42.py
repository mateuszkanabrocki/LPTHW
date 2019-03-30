## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is-an Animal
class Dog(Animal):

    def __init__(self, name, gender):
        # Dog has-a name and gender
        self.name = name
        self.gender = gender
    
    def voice(self):
        print("łufłuf!")

#Cat is-an Animal
class Cat(Animal):

    def __init__(self, name, color):
        # Cat has-a name and color
        self.name = name
        self.color = color

# Person is-an object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee inherits name from superclass
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is-an object (basic type of thing)
class Fish(object):
    pass

# Salmon is a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# Create łuf which is-a Dog
łuf = Dog('Joe', 'male')


# rover is-a Dog
rover = Dog("Rover", 'male')
print(">>>", łuf.name)
# satan is a Cat
satan = Cat("Satan", 'black')

# Mary is a Person
mary = Person("Mary")

# Mary has a pet called satan
mary.pet = satan

# frank is-an Employee
frank = Employee("Frank", 120000)

# frank's pet is called rover
frank.pet = rover

# fliper is an instance of FIsh
flipper = Fish()

# crouse is an instance of Salmon
crouse = Salmon()

# haryy is an instance of Halibut
harry = Halibut()
