from django.shortcuts import render
from ermanager.models import Paitent, Location

from django.http import HttpResponse
from django.template import RequestContext, loader

from ermanager.models import Paitent

def doctor_page(request):
  paitent_list = Paitent.objects.order_by('-last_name')
  template= loader.get_template('ermanager/doctor_view.html')
  context = RequestContext(request, {
      'paitent_list':paitent_list,
    })
  return HttpResponse(template.render(context))

def paitent_edit(request,paitent_id):
  try:
    paitent = Paitent.objects.get(id=paitent_id)
  except Paitent.DoesNotExist:
    raise Http404
  return render(request, 'ermanager/paitent_edit.html', {'paitent':paitent})

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
    
