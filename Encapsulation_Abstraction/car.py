from abc import ABC ,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("Car engine roaring to life! Vroom 🚗")


car1=car()
car1.start()





