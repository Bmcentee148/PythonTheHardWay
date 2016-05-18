# Demonstration of implicit inheritance in Python. Methods and attributes of the
# parent class are implicitly inherited by the child class.

class Parent(object) :
    name = "John"
    def implicit(self) :
        print "PARENT implicit()"

class Child(Parent) :
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print dad.name
print son.name
