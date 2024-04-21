import requests
import json
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


def get_all_posts():
    url = 'https://spb-classif.gate.petersburg.ru/api/v2/datasets/139/versions/latest/data/569/'
    response = requests.get(url).json()
    a = []
    photo = 'https://i.pinimg.com/originals/77/59/4c/77594c17dd3f88af3b8c42c6e44b11bf.jpg'
    for i in response["results"]:
        print(''.join(i['address_manual'].split(',')[1:4]))
        #cursor.execute('INSERT INTO Users (username, event, location, descriptions, howpeople, illustration) VALUES (?, ?, ?, ?, ?, ?)', (i['name'], 'Музей', ''.join(i['address_manual'].split(', ')[1:4]), i['description'], 100, photo))        

        
        
get_all_posts()
connection.commit()
connection.close()

