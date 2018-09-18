from geopy import distance
from geopy.geocoders import Nominatim


def get_dist(l1, l2):
	dist = distance.distance(l1, l2).miles
	return str(dist) + ' miles'


if __name__ == '__main__':
	geolocater = Nominatim(user_agent = "westbergg_hw02.py", timeout = 3)
	
	print('Enter Starting Location: ')
	l1 = geolocater.geocode(input())#'2609 7th St, Las Vegas, NM 87701'
	
	print('Enter Ending Location: ')
	l2 = geolocater.geocode(input())#'1005 Diamond St, Las Vegas, NM 87701'
	
	print(get_dist((l1.latitude, l1.longitude), (l2.latitude, l1.longitude)))

