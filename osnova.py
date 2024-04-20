from flask import Flask,render_template, request
import sqlite3
from geopy.geocoders import Nominatim



app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def render_map():
    try:
        if request.method == 'POST':
            user_name = request.form['name']
            connection = sqlite3.connect('my_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT username, age FROM Users WHERE username = ?', (user_name, ))
            results = cursor.fetchall()
            geolocator = Nominatim(user_agent="coordinates_finder")

            a = []
            for i in results:
                location = geolocator.geocode(i[1])
                a.append([location.latitude, location.longitude])
        return render_template('map.html', b = a)
    except:
        return render_template('map.html')
	
if __name__ == '__main__':
    app.run(debug = True)
connection.close()
