import requests
import time

TAG = 'python'
DAYS = 1


# не понял как вывести больше 100 вопросов за один раз, если только реализовать через деление отрезками
# за 2 дня их примерно около 1000 должно быть, поэтому оставил макс. параметр 100, жду коментариев

def get_questions(tag, days):
    from_date = int(time.time()) - 86400 * days
    to_date = int(time.time())

    params = {'pagesize': 100,
              'fromdate': from_date,
              'todate': to_date,
              'order': 'desc',
              'sort': 'creation',
              'tagged': tag,
              'site': 'stackoverflow'
              }
    response = requests.get('https://api.stackexchange.com/2.2/questions', params=params)
    response.raise_for_status()
    questions = response.json()['items']

    for question in questions:
        print(time.ctime(question['creation_date']), question['title'])
    return


get_questions(TAG, DAYS)
