import csv
import os
import tempfile
import shutil

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
    header = ['NAME', 'COUNT']
    csv_file = None
    try:
        csv_file = open(csv_file_name, 'r', newline="")
        reader = csv.DictReader(csv_file, fieldnames=header)
        next(reader)
    except Exception:
        print('There is not {0} file.'.format(csv_file_name))

    with tempfile.NamedTemporaryFile('w', delete=False, newline="") as new_file:

        writer = csv.DictWriter(new_file, fieldnames=header)
        writer.writeheader()

        update_count = False

        if csv_file is None:
            writer.writerow({'NAME': restaurant_name, 'COUNT': 1})
        else:
            for row in reader:
                # 対象のレストランはCOUNTを更新して移送
                if row['NAME'] == restaurant_name:
                    row['COUNT'] = int(row['COUNT']) + 1
                    writer.writerow({'NAME': restaurant_name, 'COUNT': row['COUNT']})
                    update_count = True
                else:
                    # 対象外のレストランはそのままレコードを移送
                    writer.writerow({'NAME': row['NAME'], 'COUNT': row['COUNT']})
            if not update_count:
                # 新規のレストランはレコードを追加
                writer.writerow({'NAME': restaurant_name, 'COUNT': 1})

    if csv_file is not None:
        csv_file.close()

    if os.path.isfile(csv_file_name):
        os.remove(csv_file_name)
    shutil.copy(new_file.name, csv_file_name)


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
