class animal:
    def sound(self):
        return "MmmMmm"
class lion(animal):
    def sound(self):
        return "Grrrr!"
        
class elephant(animal):
    def sound(self):
        return super().sound()

ani =[lion(),elephant()]
for a in ani:
    print(a.sound())