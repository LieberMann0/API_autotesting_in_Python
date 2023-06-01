import pytest
import requests
import yaml

with open('logpass.yaml') as f:
    data = yaml.safe_load(f)

name = data['user']
passwd = data['pass']
title = data['title']
description = data['description']
content = data['content']


@pytest.fixture()
def login():
    r = requests.post('https://test-stand.gb.ru/gateway/login',
                      data={'username': name, 'password': passwd})
    return r.json()['token']


@pytest.fixture()
def create_post():
    createpost = requests.post('https://test-stand.gb.ru/gateway/posts',
                                data={'title': title,
                                      'description': description,
                                      'content': content})
    return createpost.json()['data']


@pytest.fixture()
def text1():
    return 'Сдесь могла бы быть ваша реклама)'


@pytest.fixture()
def text2():
    return 'Содержание поста'
    