# This features all aspects of inheritance between a Parent and child class.
# It shows implicitly inherited functionality, how to override the functionality
# of a parent class, and also how to alter the functionality of a parent class

# Define new class Parent that is an object
class Parent(object) :

    # define a method named implicit which will print text (not overridden)
    def implicit(self) :
        print "PARENT implicit()"

    # define a method named overriden which prints text (overriden by child)
    def overriden(self) :
        print "PARENT overriden()"

    # define a method named altered which prints text (not overriden)
    def altered(self) :
        print "PARENT altered()"

# Define a new class Child that is a Parent (inherits its attributed and methods)
class Child(Parent) :

    # Override the method of the Parent class to print different text
    def overriden(self) :
        print "CHILD overriden()"

    # Alter the method of the Parent class by adding functionality (not overriden)
    def altered(self) :
        print "CHILD BEFORE PARENT altered()" 
        super(Child, self).altered() # calls the altered() method of the Parent
        print "CHILD AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.overriden()
son.overriden()

dad.altered()
son.altered()