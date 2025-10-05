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