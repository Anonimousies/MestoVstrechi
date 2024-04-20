from flask import Flask,render_template, request
from geopy.geocoders import Nominatim
app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def render_map():
    a = ['Невский проспект', 'метро Петроградская', 'Дворцовая площадь']
  #  if request.method == 'POST':
  #      user_name = request.form['name']
    geolocator = Nominatim(user_agent="coordinates_finder")
    b = []
    for i in a:
        location = geolocator.geocode(i)
        c = [location.latitude, location.longitude]
        b.append(c)
    return render_template('map.html', b = b)	
	
if __name__ == '__main__':
    app.run(debug = True)
