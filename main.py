import csv
import os

import termcolor

welcome_text = """\
こんにちは!私はRobokoです。あなたの名前は何ですか?
"""

question_text="""\
{0}さん。どこのレストランが好きですか?
"""

goodbye_text = """\
{0}さん。ありがとうございました。
良い一日を!さようなら。
"""


def green_print(text: str):
    print(termcolor.colored(text, color='green'))


def write_csv_ranking(file_name:str):
     if not os.path.isfile(file_name):
        with open(file_name, 'w') as f:
            csv.DictWriter() #Todo csvに書き込む

def main():
    while True:
        green_print(welcome_text)
        user_name = input()
        if len(user_name) != 0:
            break

    while True:
        green_print(question_text.format(user_name))
        user_favorite_restaurant = input()
        if len(user_favorite_restaurant) != 0:
            break
    green_print(goodbye_text.format(user_name))


if __name__ == '__main__':
    main()
