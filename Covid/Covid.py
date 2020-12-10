import json
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

__data = None

def get_coordinates(x) :
    if ',' in x :
        x = x.split(',')
    else :
        try :
            geolocator = Nominatim(user_agent="Your_Name")
            location = geolocator.geocode(x)
            return (location.latitude, location.longitude)
        except :
            print("Can you be more precise")
            return

def get_hospital(hsp) :
    global __data
    low = 0
    x = get_coordinates(hsp)
    for y in __data['LOC'] :
        dist = geodesic(x,__data['LOC'][y]).miles
        if low :
            if dist < low :
                low = dist
                index = y
        else :
            low = dist
            index = y
    return(__data['Hospital'][index],__data['Address'][index])

def load_saved_artifacts() :
    print('Loading Artifacts')
    global __data
    with open('json_hosp.json') as f :
        __data = json.load(f)
    print('Loaded Successfully')

if __name__ == '__main__' :
    load_saved_artifacts()
    hsp = 'kaggadasapura'
    print(get_hospital(hsp))