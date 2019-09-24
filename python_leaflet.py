import geopy
import pandas
from geopy.geocoders import Nominatim,GoogleV3

def main():
    io = pandas.read_csv('census.csv', index_col=None, header=0, sep=",")

    def get_latitude(x):
        return x.latitude

    def get_longitude(x):
        return x.longitude

    geolocator = Nominatim(user_agent="test")
    #geolocator = GoogleV3()
    geolocate_column = io['Area_Name'].apply(geolocator.geocode)
    io['latitude'] = geolocate_column.apply(get_latitude)
    io['longitude'] = geolocate_column.apply(get_longitude)
    print("Final")
    io.to_csv('geocoding_output.csv')

if __name__ == '__main__':
    main()
