class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayName(self):
        print("Hello, this is ", self.name)

    def displayAge(self):
        print("I am", self.age, "years old")


p1 = Person("Faizan", 22)
p1.displayName()
p1.displayAge()
