from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="coordinates_finder")
location = geolocator.geocode(" Санкт-Петербург ул. Малая Садовая 2/27")
print(location.address)

print((location.latitude, location.longitude))
