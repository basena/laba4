import json
import csv
# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    # TODO считать содержимое csv файла

    json_string = json.dumps(data, indent=4)
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_file:  # запись в файл
        output_file.write(json_string)
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
