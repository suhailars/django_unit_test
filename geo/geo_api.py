import requests
import urllib


def get_address(lat, lon):
    base_url = 'http://nominatim.openstreetmap.org/reverse'
    params = {
        'format': 'json',
        'lat': lat,
        'lon': lon
    }
    params_encode = urllib.parse.urlencode(params)
    full_url = "%s?%s" % (base_url, params_encode)
    response = requests.get(full_url)
    print("response", response.json())
    if response.status_code  == 200:
        return response.json()["display_name"]








