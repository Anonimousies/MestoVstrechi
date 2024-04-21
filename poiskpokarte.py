from flask import Flask,render_template, request
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def render_map():
    if request.method == 'POST':
        user_name = request.form['name']
        
    geolocator = Nominatim(user_agent="coordinates_finder")
    location = geolocator.geocode(user_name)
    return render_template('map.html', a=location.latitude, b=location.longitude)

if __name__ == '__main__':
    app.run(debug = True)
