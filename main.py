import csv
import os
import tempfile
import shutil

import termcolor

welcome_text = """\
こんにちは!私はRobokoです。あなたの名前は何ですか?
"""
recommend_text = """\
私のオススメのレストランは、{0}です。
このレストランは好きですか？ [Yes/No]
"""

question_text = """\
{0}さん。どこのレストランが好きですか?
"""

goodbye_text = """\
{0}さん。ありがとうございました。
良い一日を!さようなら。
"""

ranking_file = 'ranking.csv'
ranking_header = ['NAME', 'COUNT']


def green_print(text: str):
    print(termcolor.colored(text, color='green'))


def read_ranking(csv_file_name):
    ranking = {}
    try:
        with open(csv_file_name, 'r', newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                ranking.update(line.items())
                print(ranking)
    except Exception:
        print('There is not {0} file.'.format(csv_file_name))
    finally:
        return ranking


def get_recommend_restaurants(ranking):
    return ranking.get('NAME') #Todo yieldする。


def write_ranking(csv_file_name, ranking, restaurant_name):
    with tempfile.NamedTemporaryFile('w', delete=False, newline="") as new_file:

        writer = csv.DictWriter(new_file, fieldnames=ranking_header)
        writer.writeheader()
        update_count = False

        if ranking:
            for dic in ranking.items():
                if dic['NAME'] == restaurant_name:
                    count = dic.get('COUNT')
                    count = int(count) + 1
                    writer.writerow({'NAME': restaurant_name, 'COUNT': count})
                    update_count = True
                else:
                    writer.writerow({'NAME': dic.get('NAME'), 'COUNT': dic.get('COUNT')})

        if not update_count:
            # 新規のレストランはレコードを追加
            writer.writerow({'NAME': restaurant_name, 'COUNT': 1})

    if os.path.isfile(csv_file_name):
        os.remove(csv_file_name)
    shutil.copy(new_file.name, csv_file_name)


def main():
    while True:
        green_print(welcome_text)
        user_name = input()
        if len(user_name) != 0:
            break

    ranking = read_ranking(ranking_file)

    if ranking:
        while True:
            green_print(recommend_text.format(get_recommend_restaurants(ranking)))
            answer = input().capitalize()
            if (answer == 'Yes' or answer == 'Y'):
                break
            elif (answer == 'No' or answer == 'N'):
                pass  # Todo 次のおすすめを実装する。

    while True:
        green_print(question_text.format(user_name))
        favorite_restaurant_name = input().capitalize()
        if len(favorite_restaurant_name) != 0:
            break

    write_ranking(ranking_file, ranking, favorite_restaurant_name)
    green_print(goodbye_text.format(user_name))


if __name__ == '__main__':
    main()
