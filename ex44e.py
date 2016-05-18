# This will demonstate how composition works in python and will provide the 
# same type of functionality we had with our use of inheritance.

class Other(object) :

    def implicit(self) :
        print "OTHER implicit()"

    def overriden(self) :
        print "OTHER overriden"

    def altered(self) :
        print "OTHER altered"

class Child(object) :

    def __init__(self) :
        self.other = Other()

    def implicit(self) :
        self.other.implicit()

    def overriden(self) :
        print "CHILD overriden"

    def altered(self) :
        print "CHILD BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD AFTER OTHER altered()"

son = Child()

son.implicit()
son.overriden()
son.altered()