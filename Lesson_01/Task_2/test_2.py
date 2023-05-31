import requests


def get(token):
    g = requests.get('https://test-stand.gb.ru/api/posts',
                     headers={'X-Auth-Token': token})  # , 'page': 17, params={'owner': 'notMe'
    listcont = [i['content'] for i in g.json()['data']]
    return listcont


def createpost(token):
    p = requests.post('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token},
                      data={'title': 'Новый пост для тестирования',
                            'description': 'Тестируем при помощи requests и pytest',
                            'content': 'Добавить в задание с REST API еще один тест, в котором создается новый пост,'
                                       'а потом проверяется его наличие на сервере по полю “описание”.'})
    return p.json()


def findpost(token):
    d = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    listdescript = [i['description'] for i in d.json()['data']]
    return listdescript


def test_2(login, text1):
    assert text1 in get(login)


def test_3(login, text2):
    assert text2 in get(login)
    