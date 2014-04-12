from django.shortcuts import render
from ermanager.models import Paitent, Location
from django.http import HttpResponse
# Create your views here.

def big_board(request):
	rooms = Location.objects.order_by('number')
	dict1 = dict()
	for room in rooms:
		num = room.number
		person = Paitent.objects.get(loc__exact=num)
		
		
		dict1[num] = (person.first_name, person.last_name, person.priority)




	#dict1 contains the room number as the key, and the values fname,lname,and priority as a tuple 
	
	return HttpResponse(dict1)
	
