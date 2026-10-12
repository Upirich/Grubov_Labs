def calculate_average(measurements):
    summa = 0
    for num in measurements:
        summa += num
    return summa / len(measurements)

def find_minimum(measurements):
        return sorted(measurements)[0]

def find_maximum(measurements):
    return sorted(measurements)[-1]