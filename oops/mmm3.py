# Class = blueprint
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("Hello, ", self.name)

p = Person("Alice", 22)
p2 = Person("Rahul", 30)

p.greet()
p2.greet()