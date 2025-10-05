#1
'''
#a
def greet(name):
    print('Привет,',name)
greet('Арсений')
greet('Андрей')
print('----')
#b
def square(number):
    print(number**2)
square(12)
square(9)
print('----')
#c
def max_of_two(x,y):
    print(max(x,y))
max_of_two(14,78)
max_of_two(75,2)
'''
#2
'''
def describe_person(name,age=30):
    if age==30:
        print(f'Имя:',name,'Возраст:',age,'лет(значение по умолчанию)')
    else:
        print(f'Имя:',name,'Возраст:',age)
describe_person('Арсений',18)
describe_person('Андрей')
'''
#3
def is_prime(number):
    if number==1:
        return False
    for j in range(2,int(number**0.5)+1):
        if number%j==0:
            return False
    return True
for n in {4,7}:
    if is_prime(n)==1:
        print(n,'- простое')
    else:
        print(n,'- не простое')