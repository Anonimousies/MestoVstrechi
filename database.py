import sqlite3


# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
username TEXT NOT NULL,
event TEXT NOT NULL,
location TEXT NOT NULL,
descriptions TEXT NOT NULL,
howpeople INTEGER,
illustration TEXT NOT NULL
)
''')

#cursor.execute('INSERT INTO Users (username, event, location, descriptions, howpeople, illustration) VALUES (?, ?, ?, ?, ?, ?)', ('Александр Рубайло', 'шахматы', 'Санкт Петербург Невский проспект дом 10', 'приглашаю приятного собеседника на партию', 1, 'https://cdn.culture.ru/images/c1b73537-b2dd-52cf-8682-2fea8c2410b6'))
cursor.execute('INSERT INTO Users (username, event, location, descriptions, howpeople, illustration) VALUES (?, ?, ?, ?, ?, ?)', ('Ян Непомнящий', 'шахматы', 'Метро Дыбенко', 'У меня Карлсон пощады просил', 12, 'https://www.bon-cadeau.ru/mdata/gallery/size3/1184/4577.jpg'))

# Сохраняем изменения и закрываем соединение


connection.commit()
connection.close()
