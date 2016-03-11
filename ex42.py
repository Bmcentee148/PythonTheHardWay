# Animal is an object (yes kind of confusing) 
class Animal(object) :
    pass

# Class dog is-a Animal
class Dog(Animal) :
    
    def __init__(self, name) :
        # Dog has-a name
        self.name = name

# Class cat is-a Animal
class Cat(Animal) :
    
    def __init__(self,name) :
        #Cat has-a name
        self.name = name

# class Person is-a object
class Person(object) :

    def __init__(self, name) :
        # Person has-a name
        self.name = name
        # Person has-a pet of some kind
        self.pet = None

# class Employee is-a Person
class Employee(Person) :

    def __init__(self, name, salary) :
        # call constructor of parent class Person and pass it parameters self, name
        super(Employee, self).__init__(name)
        # Person has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object) :
    pass

#Salmon is-a Fish
class Salmon(Fish) :
    pass

#Halibut is-a Fish
class Halibut(Fish) :
    pass

# rover is-a Dog
rover = Dog("Rover")
#satan is-a Cat
satan = Cat("Satan")
# mary is a person
mary = Person('Mary')
 
#from mary get the pet attribute and set it to satan
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 100000)

# frank has-a pet 
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a Halibut
harry = Halibut()












