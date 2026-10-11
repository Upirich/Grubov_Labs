def find_element(numbers, target):
    for i in range(len(numbers)):
        print(numbers[i], target)
        if numbers[i] == target:
            return i
        else:
            return -1
print(find_element([42, 38, 51, 35, 57], 35))