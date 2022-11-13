import json

FILENAME = 'setting_save.json'

def save(dic):
    with open('setting_save.json', 'w') as f:
        json.dump(dic, f)

def load():
    with open(FILENAME, 'r', encoding='utf-8') as f:
        setting = json.load(f)
    return setting