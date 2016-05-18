# This will demonstrate how to use inheritance to alter the behavior of a method
# of the parent class. We do this by first overriding the method, and then
# calling the method of the parent class within it using the super keyword.

class Parent(object) :

    def altered(self) :
        print "PARENT altered()"

class Child(Parent) :

    def altered(self) :
        print "CHILD BEFORE PARENT altered"
        super(Child, self).altered()
        print "CHILD AFTER PARENT altered"

dad = Parent()
son = Child()

dad.altered()
son.altered()