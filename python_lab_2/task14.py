n = int(input())
summ = 0
for _ in range(n):
    num = float(input())
    summ += num
avg = summ / n
print(f'Сумма: {summ} | Среднее арифметическое: {avg}')