from flask import Flask,render_template, request
import sqlite3
from geopy.geocoders import Nominatim



geolocator = Nominatim(user_agent="coordinates_finder")


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.execute('SELECT username, event, descriptions, howpeople, illustration, location FROM Users')
results = cursor.fetchall()
a =[]
for i in renge(results):
    print(i[5])

for i in range(len(results)):
    location = geolocator.geocode(results[i][5])

    a.append([results[i][0:5], [location.latitude, location.longitude]])


connection.commit()
