import requests


def login():
    data = requests.post('https://test-stand.gb.ru/gateway/login',
                         data={'username': 'testtest1', 'password': 'c23b2ed66e'})
    return data.json()['token']


def get(token):
    data = requests.get('https://test-stand.gb.ru/api/posts', params={'owner': 'notMe'},
                        headers={'X-Auth-Token': token})
    print(data.json())
    return data.json()


token = login()
get(token)
