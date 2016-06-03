# Demonstrates implicit inheritance in python. The child class will have a
# method which overrides the method of the Parent class. This is done by simply
# defining a method in the child class with the same name as a method in the
# Parent class

class Parent(object) :

    def override(self) :
        print "PARENT override()"

class Child(Parent) :

    def override(self) :
        print "CHILD override"

dad = Parent()
son = Child()

dad.override()
son.override()


