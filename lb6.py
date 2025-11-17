#1
'''
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    
    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            print('Пароль изменен')
        else:
            print('Пароль слишком короткий')
    
    def check_password(self, password):
        return password == self.__password

user1 = UserAccount('user_suser', 'user@mail.ru', 'old_password123')
print(user1.check_password('old_password123'))

user1.set_password('new_secure_password')
print(user1.check_password('new_secure_password'))
print(user1.check_password('wrong_password'))
'''

#2
'''
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f'Марка: {self.make}, Модель: {self.model}'

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        return f'Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}'

vehicle1 = Vehicle('Toyota', 'Camry')
print(vehicle1.get_info())

car1 = Car('BMW', 'X5', 'бензин')
print(car1.get_info())
'''
