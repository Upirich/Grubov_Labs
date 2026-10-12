from utils.statistics import *
from utils.reader import *
from pathlib import Path
import logging
import json


def main():
    logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
    )
    logging.info('Program START')


    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
    
    file_path = Path(config["input_file"])


    try:
        sp = read_numbers(f'{file_path}')
        validate_numbers(sp)
        print(calculate_average(sp), find_maximum(sp), find_minimum(sp))
        logging.info('Program END')

    except FileNotFoundError:
        logging.error('File not found')
        print('File does not exist')

    except ValueError:
        logging.error('ValueError, incorrect values')
        print(f'Incorrect values in {file_path}')

def validate_numbers(numbers):
    if not numbers:
        logging.error(f'ValueError, list is NULL')
        raise ValueError('Список измерений пуст!')


if __name__ == '__main__':
    main()
