from abc import ABC,abstractmethod

class device(ABC):
    @abstractmethod
    def boot(self):
     pass

class phone(device):
    def boot(self):
      self.load_os()
      self.check_hardware()
      print("Completed")

    def load_os(self):
       print("loading...")

    def check_hardware(self):
         print("hardware loading...")
        
iphone=phone()
iphone.boot()    
   