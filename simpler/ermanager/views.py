from django.shortcuts import render
from ermanager.models import Patient, Location

from django.http import HttpResponse
from django.template import RequestContext, loader

from ermanager.models import Patient

def doctor_page(request):
  patient_list = Patient.objects.order_by('-last_name')
  template= loader.get_template('ermanager/doctor_view.html')
  context = RequestContext(request, {
      'patient_list':patient_list,
    })
  return HttpResponse(template.render(context))

def patient_edit(request,paitent_id):
  try:
    patient = Patient.objects.get(id=patient_id)
  except Patient.DoesNotExist:
    raise Http404
  return render(request, 'ermanager/patient_edit.html', {'patient':patient})

# Create your views here.

def patient_mod(request,patient_id):
  try:
    patient = Patient.objects.get(id=patient_id)
  except Patient.DoesNotExist:
    raise Http404
  return render(request, 'ermanager/patient_mod.html', {'patient':patient})

def big_board(request):
    rooms = Location.objects.order_by('number')
    dict1 = dict()
    for room in rooms:
        num = room.number
        try:
          person = Patient.objects.get(loc=room)
          dict1[num] = (person.first_name, person.last_name, person.priority)
        except Patient.DoesNotExist:
          dict1[num] = "Empty"
    template = loader.get_template('ermanager/big_board.html')
    context = RequestContext(request, {
          'dict1':dict1,
    })
    return HttpResponse(template.render(context))
