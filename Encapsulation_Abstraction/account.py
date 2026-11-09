from abc import ABC,abstractmethod
class account(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass
class SavingAccount(account):
    def calculate_interest(self):
        print("interest is 5%")
class CurrentAccound(account):
    def calculate_interest(self):
       print("interest is none")

saav=SavingAccount()
saav.calculate_interest()
cur=CurrentAccound()
cur.calculate_interest()