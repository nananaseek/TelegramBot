import requests
from config import URL_AUTH, URL_TRANS, KEY
from googletrans import Translator

hauth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=hauth)


def go_UAtoEN(word):
    if auth.status_code == 200:
        token = auth.text
        if word:
            htrans = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1058,
                'dstLang': 1033
            }
            r = requests.get(URL_TRANS, headers=htrans, params=params)
            res = r.json()
            try:
                return res['Translation']['Translation']
            except:
                return 'нема такого слова'
    else:
        print('щось голова кружиться')


def go_ENtoUA(word):
    if auth.status_code == 200:
        token = auth.text
        if word:
            htrans = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1058
            }
            r = requests.get(URL_TRANS, headers=htrans, params=params)
            res = r.json()
            try:
                return res['Translation']['Translation']
            except:
                return 'нема такого слова'
    else:
        print('щось голова кружиться')
