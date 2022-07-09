import random
a = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку')
def is_valid(n):
    if n.isdigit():
        if 1 <= int(n) <= 100:
            return True
    return False
b = input('Введите целое число от 1 до 100')
def guess_me(b):
    while True:
        if is_valid(b):
            b = int(b)
            break
        else:
            b = input('А может все таки введете целое число от 1 до 100')
while True:
    if a > b:
        guess_me(input


