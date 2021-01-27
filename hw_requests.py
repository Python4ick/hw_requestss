import requests

hero_list = ['Captain America', 'Hulk', 'Thanos', 'Batman', 'Spider-Man', 'Harry Potter']


# получаем id героя
def get_id(hero_name):
    response = requests.get('https://superheroapi.com/api/2619421814940190/search/{}'.format(hero_name))
    response.raise_for_status()
    hero_id = response.json()['results'][0]['id']
    print(f'Получаю id героя {hero_name},', end=" ")
    return hero_id


# получаем intelligence героя
def get_intelligence(hero_id):
    response = requests.get('https://superheroapi.com/api/2619421814940190/{}/powerstats'.format(hero_id))
    response.raise_for_status()
    intelligence = response.json()['intelligence']
    print(f'получаю характеристику его разума = {intelligence}...')
    return intelligence


# заполняем словарь вида {'Герой': 'разум'}
def fill_hero_intelligence(heroes_list):
    hero_intelligence = {}
    for hero in heroes_list:
        hero_intelligence.setdefault(hero, get_intelligence(get_id(hero)))
    return hero_intelligence


# проходимся по словарю, отсортированному по значениям, первый элемент будет с максималным разумом, остальные для вида
def print_result(characters_dict):
    for i, hero in enumerate(sorted(characters_dict.items(), key=lambda x: int(x[1]), reverse=True), 1):
        if i == 1:
            print(f'\n{hero[0].upper()} имеет MAX разум = {hero[1]}')
            print('============================')
        else:
            print(f'{hero[0]} имеет разум = {hero[1]}')
    return


# запускаем функцию печати, с вложеными функциями заполнения словаря, взятия id. исходные данные - список героев
print_result(fill_hero_intelligence(hero_list))
