def greet(name):
    print(f'Hello, {name}')

def square(number):
    return number**2

def max_of_two(a, b):
    return a if a > b else b

def calculate_rectangle(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def describe_rectangle(width, height, unit="см"):
    print(f'Прямоугольник с шириной: {width} {unit} и длиной {height} {unit}')

def task3():
    value = 10

    def example():
        value = 20
        smth = 10
        print(value)

    example()
    print(value)
    print(smth)

def task4():
    sp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sp[0], sp[2], sp[-1])
    sp[1] = 99
    sp.append(16)
    sp.remove(7)
    print(sp)

def task5():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers[:3])
    print(numbers[-3:])
    print(numbers[2:7])
    print(numbers[1::2])
    print(numbers[::-1])

def task6():
    measurements = (1, 2, 3, 4, 5, 6, 7, 8)
    print(measurements[0], measurements[1], measurements[:6])
    first, second = measurements[0], measurements[1]
    sp = list(measurements)
    sp[0] = 100
    result = tuple(sp)
    print(result)

def task7():
    sp = [1, 2, 3, 4, 5, 6, 7, 8]
    print(len(sp), sum(sp), min(sp), max(sp), sum(sp) / len(sp))
    sp1 = sorted(sp)
    sp.sort()

def task8():
    def calculate_sum(nums):
        res = 0
        for num in nums:
            res += num
        return res

    def calculate_min(nums):
        return sorted(nums)[0]

    def calculate_max(nums):
        return sorted(nums)[-1]

    print(calculate_min([3, 1, 5, 2]))

def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return "Number not Found"

def task10():
    def analyze(numbers):
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    x, y, z = analyze([1, 2, 4, 8, 3, 7, 1])
    print(x, y, z)

def task11():
    numbers = [-10, 3, -2, 8, -5]
    sp = sorted(numbers)
    sp1 = sorted(numbers, key=lambda x: abs(x))
    print(sp, sp1, sep='\n')

def task12():
    def calculate_average(measurements):
        summa = 0
        for num in measurements:
            summa += num
        return summa / len(measurements)

    def find_minimum(measurements):
        return sorted(measurements)[0]

    def find_maximum(measurements):
        return sorted(measurements)[-1]

    def count_above_average(measurements):
        avg = calculate_average(measurements)
        result = 0
        for num in measurements:
            if num > avg:
                result += 1
        return result

    def find_value(numbers, target):
        for i in range(len(numbers)):
            if numbers[i] == target:
                return i
        return "Number not Found"

    def analyze_measurements(measurements):
        return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)

    sp = [2, 6, 1, 8, 3, 5, 9, 0, 1, 4, 7]
    print(len(sp))
    print(find_minimum(sp))
    print(find_maximum(sp))
    print(calculate_average(sp))
    print(count_above_average(sp))
    print(find_value(sp, 0))
    x, y, z = analyze_measurements(sp)

task12()