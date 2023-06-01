import requests


def get(token):
    g_post = requests.get('https://test-stand.gb.ru/api/posts',
                     headers={'X-Auth-Token': token},
                     params={'owner': 'notMe'})
    listcont = [i['content'] for i in g_post.json()['data']]
    return listcont


def createpost(token):
    c_post = requests.post('https://test-stand.gb.ru/gateway/posts',
                      headers={'X-Auth-Token': token})
    return c_post.json()


def findpost(token):
    f_post = requests.get('https://test-stand.gb.ru/api/posts',
                     headers={'X-Auth-Token': token})
    postdescript = [i['description'] for i in f_post.json()['data']]
    return postdescript


def test_2(login, text1):
    assert text1 in get(login)


def test_3(login, text2):
    assert text2 in findpost(login)    
