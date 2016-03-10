class Dog : 

    kind = 'canine'
    # tricks = []  #mistake to use class variable

    def __init__(self, name) :
        self.name = name
        self.tricks = [] # create new empty list for each dog object

    def add_trick(self,trick) :
        self.tricks.append(trick)

my_dog = Dog("Molly")

caseys_dog = Dog("Otis")

# Each are the same kind but have different names
print my_dog.kind
print caseys_dog.kind

print my_dog.name
print caseys_dog.name

my_dog.add_trick("Lay Down")
caseys_dog.add_trick("Bark")

print my_dog.tricks
print caseys_dog.tricks