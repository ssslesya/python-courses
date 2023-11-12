import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        data = []

        for row in csv_reader:
            data.append({key: value for key, value in row.items()})

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
