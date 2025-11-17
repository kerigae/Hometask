class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return f'Сотрудник: {self.name}, ID: {self.id}'

class Manager:
    def __init__(self, department):
        self.department = department
        self.team = []
    
    def manage_project(self):
        return f'Управление проектами в отделе {self.department}'
    
    def add_employee(self, employee):
        self.team.append(employee)
        return f'Сотрудник {employee.name} добавлен в команду'
    
    def get_team_info(self):
        if not self.team:
            return 'В команде нет сотрудников'
        team_info = 'Команда сотрудников:\n'
        for employee in self.team:
            team_info += f'- {employee.get_info()}\n'
        return team_info

class Technician:
    def __init__(self, specialization):
        self.specialization = specialization
    
    def perform_maintenance(self):
        return f'Выполнение технического обслуживания по специализации: {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id)
        Manager.__init__(self, department)
        Technician.__init__(self, specialization)
    
    def get_info(self):
        return f'Технический менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}, Специализация: {self.specialization}'

employee1 = Employee('Адрей Петровский', 'E001')
print(employee1.get_info())

manager1 = Manager('Разработка')
print(manager1.manage_project())

technician1 = Technician('Сетевое оборудование')
print(technician1.perform_maintenance())

tech_manager = TechManager('Роман Полански', 'TM001', 'IT', 'Системное администрирование')
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())

tech_manager.add_employee(employee1)
tech_manager.add_employee(Employee('Анна Хуберт', 'E002'))
print(tech_manager.get_team_info())
