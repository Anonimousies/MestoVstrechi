from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="coordinates_finder")
location = geolocator.geocode("Санкт- Петербург Садовая улица 1")
print(location.address)

print((location.latitude, location.longitude))
