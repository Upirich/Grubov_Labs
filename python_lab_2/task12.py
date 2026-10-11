print('Enter a number:')
num = int(input())
if num > 0:
    print('Положительное')
elif num == 0:
    print('Число является нулем')
else:
    print('Отрицательное')
print('Чётное') if num % 2 == 0 else print('Нечётное')