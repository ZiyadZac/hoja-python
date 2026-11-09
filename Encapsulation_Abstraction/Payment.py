from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        print("how much to deposit")

class Card(Payment):
    def pay(self):
        print("card")

class UPI(Payment):
    def pay(self):
        print("UPI")

card1= Card()
card1.pay()
upi1=UPI()
upi1.pay()