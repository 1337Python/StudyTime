
class NonObject:
    None    #This is Python syntax for noop aka no-op or 'no operation'

class Object:
    def __init__(self):
        self.name = "Unamed"
        self.age = "-1"
        print("Constructed Object!")
    
    def __del__(self):
        print("Destructed Object!")


class NamedObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ("Constructed", name, " age ", age)
        
    def __del__(self):
        print ("Destructed", self.name, " age ", self.age)


def CreateNothing():
    nothing = NonObject()
    
def CreateSomething():
    something = Object()

def CreateJon():
    named = NamedObject("Jon", 13)




#Enter Main here!
CreateNothing()
CreateSomething()
CreateJon()

print("----------------------")
print("Now notice the difference in order of constructor/destructor")
nothing = NonObject()
#print(nothing.name)  ERROR!  We never created any attribute on this object

something = Object()
print(something.name, ", ", something.age)

jon = NamedObject("Jon", 13)
brad = NamedObject("Brad", 172)
#jon and brad are the same object but have different member values.  aka they are different instances of the same object.
#which you can see with their constructors/destructors
#Notice that objects are destructed in the order they are constructed.  So Object is first, then Jon, then Brad.
