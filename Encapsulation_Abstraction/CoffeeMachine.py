from abc import ABC,abstractmethod
class CoffeeMachine(ABC):
    @abstractmethod
    def make_coffee(self):
        print("making....")
