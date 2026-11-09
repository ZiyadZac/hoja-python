class dog:
    def speak(self):
        return ("bow,bow")

class cat:
    def speak(self):
        return ("meow,meow")

def animal(ani):
    print(ani.speak())

d=dog()
c=cat()
animal(d)
animal(c)              