from abc import ABC,abstractmethod
class login_system(ABC):
    @abstractmethod
    def login(self):
       pass

class app_login(login_system):
    def login(self):
        self.__verify_user()
        self.__check_password()
    def __check_password(self):
        print('checked')
    def __verify_user(self):
        print("verified")

log = app_login()
log.login()