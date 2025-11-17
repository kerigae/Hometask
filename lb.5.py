#1
'''
class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author 
        self.year = year
        
    def get_info(self):
        info_string = f'Название книги: {self.title},  Автор: {self.author},  Год издания: {self.year}'
        return info_string

book1 = book('Преступление и наказание', 'Достоевский', 1866)
result = book1.get_info()
print(result)
'''

#2
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        current = self.radius
        return current
    
    def set_radius(self, new_radius):
        self.radius = new_radius

circle = Circle(10)
circle.set_radius(15)
current_radius = circle.get_radius()
print(f'Текущий радиус окружности: {current_radius}')
'''
