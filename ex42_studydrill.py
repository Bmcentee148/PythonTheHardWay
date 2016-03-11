class Person(object) :
    kingdom = "Animal"
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def get_name(self) :
        return self.name

    def get_age(self) :
        return self.age

    def print_name(self) :
        print self.name

    def print_age(self) :
        print self.age

class Employee(Person) :

    def __init__(self, name, age, salary) :
        super(Employee, self).__init__(name, age)
        self.salary = salary

    def get_salary(self) :
        return self.salary

    def print_salary(self) :
        print self.salary

    def print_kingdom(self) :
        print self.kingdom

brian = Employee("Brian","24",75000)

print brian.get_salary()

print brian.get_name()

brian.print_name()
brian.kingdom = "None"
brian.print_kingdom()