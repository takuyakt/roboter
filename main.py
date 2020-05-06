import csv
import os
import tempfile

import termcolor

welcome_text = """\
こんにちは!私はRobokoです。あなたの名前は何ですか?
"""

question_text = """\
{0}さん。どこのレストランが好きですか?
"""

goodbye_text = """\
{0}さん。ありがとうございました。
良い一日を!さようなら。
"""


def green_print(text: str):
    print(termcolor.colored(text, color='green'))


def write_csv_ranking(csv_file_name: str, restaurant_name: str):
    header = ["NAME", "COUNT"]

#    if not os.path.isfile(csv_file_name):
#        with open(csv_file_name, 'w', newline="") as template_file:
#            writer = csv.DictWriter(template_file, fieldnames=header)
#            writer.writeheader()

    try:
        with open(csv_file_name, 'r+', newline="") as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=header)
    except:
        pass

    with tempfile.NamedTemporaryFile(delete=False) as new_file:
        writer = csv.DictWriter(new_file, fieldnames=header)
        writer.writeheader()
        for row in reader:
            if row["NAME"] == restaurant_name:
                pass
#            writer.writerow({"NAME": restaurant_name, "COUNT": 1})  # Todo カウントアップする。


def main():
    while True:
        green_print(welcome_text)
        user_name = input()
        if len(user_name) != 0:
            break

    while True:
        green_print(question_text.format(user_name))
        favorite_restaurant_name = input()
        if len(favorite_restaurant_name) != 0:
            break

    write_csv_ranking('ranking.csv', favorite_restaurant_name)
    green_print(goodbye_text.format(user_name))


if __name__ == '__main__':
    main()
