from django.shortcuts import render
from ermanager.models import Paitent, Location
from django.http import HttpResponse
# Create your views here.

def big_board(request):
	rooms = Location.objects.order_by('name')
	fnames = Paitent.objects.first_name
	lnames = Paitent.objects.last_name
	wait = Paitent.objects.isWaiting
	return HttpResponse(rooms)
	
