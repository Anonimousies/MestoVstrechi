from flask import Flask,render_template, request
import sqlite3
from geopy.geocoders import Nominatim



app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def render_map():
    user_name=''
    if request.method == 'POST':
        user_name = request.form['name']
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT username, event, descriptions, howpeople, illustration, location FROM Users WHERE event = ?', (user_name, ))
    results = cursor.fetchall()
    geolocator = Nominatim(user_agent="coordinates_finder")
    a =[]
    for i in range(len(results)):
        location = geolocator.geocode(results[i][5])
        a.append([results[i][0:5], [location.latitude, location.longitude]])
    return render_template('map.html', b = a)
    
	
if __name__ == '__main__':
    app.run(debug = True)
connection.close()
