#1
'''
def read_file(mtd):
        with open('example.txt','r') as file:
            if mtd=='full':
                print(file.read())
            elif mtd=='line':
                for line in file:
                    print(line.strip())
read_file('full')
print('----')
read_file('line')
'''
#2
'''
#запись текст
text=input('введите текст:')
with open('user_input.txt','w') as file:
    file.write(text)
print('текст записан')
with open('user_input.txt', 'r') as file:
    print(file.read())

#редакт. файла
add=input('введите текст:')
with open('user_input.txt','a') as file:
    file.write('\n'+add)
print('текст добавлен')
with open('user_input.txt', 'r') as file:
    print(file.read())
    '''
#3
'''
def read_file(mtd):
        try:
            with open('example.txt','r') as file:
                if mtd=='full':
                    print(file.read())
                elif mtd=='line':
                    for line in file:
                        print(line.strip())
        except FileNotFoundError:
            print("файл example.txt не найден")
read_file('full')
print('----')
read_file('line')
'''