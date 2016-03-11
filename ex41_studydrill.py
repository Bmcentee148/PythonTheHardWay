class Animal :

    similarity = "Have hair"
    animal_noises = {"Cat" : "Meow", "Dog" : "Woof", "Bird" : "Tweet"}

    def __init__(self, animal_type, name) :
        self.animal_type = animal_type
        self.name = name

    def print_name(self) :
        print self.name

    def print_animal_type(self) :
        print self.animal_type

    def make_noise(self) :
        print Animal.animal_noises[self.animal_type]

my_dog = Animal("Dog", "Molly")
caseys_cat = Animal("Cat","Midnight")

my_dog.print_name()
caseys_cat.print_name()

my_dog.print_animal_type()
caseys_cat.print_animal_type()

my_dog.make_noise()
caseys_cat.make_noise()

