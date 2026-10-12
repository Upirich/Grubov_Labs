def read_numbers(file_path):
    sp = []
    with open(file_path) as f:
        sp = f.readlines()
        sp = [float(num) for num in sp]
    return sp