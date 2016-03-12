class MyClass(object) :

    class_var = "original message"

    def __init__(self, instance_var) :
        self.instance_var = instance_var #particular to the object

my_object = MyClass("my instance variable")
untouched_object = MyClass("another instance_var")

# Values of class_var and instance_var upon creation
print my_object.class_var
print my_object.instance_var

print untouched_object.class_var
print untouched_object.instance_var

MyClass.class_var = "changed message"

# Values of class_var and instance_var after change (both objects change)
print my_object.class_var
print my_object.instance_var

print untouched_object.class_var
print untouched_object.instance_var

# This is what I dont get
my_object.class_var = "I am my_object"
MyClass.class_var = "Last message"

print my_object.class_var
print my_object.instance_var

print untouched_object.class_var
print untouched_object.instance_var


