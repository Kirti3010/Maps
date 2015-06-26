from django.shortcuts import render
#4th step to import the lib it will automatically close the lib too
import urllib.request
#8th step
import json
from django.http import HttpResponse
#Create your views here.
#1st step
def maps(request):
# 3rd step copy the url from the browser and paste it here
	map_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=nri%20college%20bhopal&key=AIzaSyBNC8VAz5E6Mn5DE4czzShdnNylUqQKVrY'
# opening the server u need to use urllib to open it	
	map_url_open =  urllib.request.Request(map_url)
#5th step read the data from the server
	map_url_read = urllib.request.urlopen(map_url_open)
	map_url_read = map_url_read.read()
#load the data coz it is in json format the data in byte format so now we have to decode into json format i.e utf8
	map_url_load = json.loads(map_url_read.decode("utf-8"))
#displaying the load data
	maps_db = map_url_load
#how to get the value of longitude and latitude
#jason object we have to call the key value i.e results. 
#now it is a json array to get the 1st element we have to get 0
#now in 0th element there is a geometry and inside this location is there and inside that there is lat and long
	maps_data_latitude = maps_db['results'][0]['geometry']['location']['lat']

	maps_data_longitude = maps_db['results'][0]['geometry']['location']['lng']
#1st step
	return render(request, 'maps_display.html',{'maps_db':maps_data_longitude})
