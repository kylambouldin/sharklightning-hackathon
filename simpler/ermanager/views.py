from django.shortcuts import render
from ermanager.models import Patient, Location
from django import forms
import datetime

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

def patient_edit(request,patient_id):
  try:
    patient = Patient.objects.get(id=patient_id)
  except Patient.DoesNotExist:
    raise Http404
  return render(request, 'ermanager/patient_edit.html', {'patient':patient})

# Create your views here.

def submit_edit(request):
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
      patient = Patient()
      patient.last_name = form.cleaned_data['last_name']
      patient.first_name = form.cleaned_data['first_name']
      patient.needs_review = form.cleaned_data['needs_review']
      patient.is_waiting = False
      loc_temp = Location(number=12)
      loc_temp.save()
      patient.loc = loc_temp
      patient.last_moved = "2010-10-11 10:56"
      patient.last_checkup = "2010-10-11 10:56"
      patient.priority = "LOW"
      patient.nurse_notes = "Notes"
      patient.doctor_notes = "Dummy notes"
      patient.save()
  patient_list = Patient.objects.order_by('-last_name')
  template= loader.get_template('ermanager/doctor_view.html')
  context = RequestContext(request, {
      'patient_list':patient_list,
    })
  return HttpResponse(template.render(context))

def patient_mod(request,patient_id):
  try:
    patient = Patient.objects.get(id=patient_id)
    form = PatientForm(initial={'last_name':patient.last_name})
  except Patient.DoesNotExist:
    raise Http404
  return render(request, 'ermanager/patient_mod.html', {'patient':patient,'form':form})

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



#Form definition

class PatientForm(forms.Form):
  last_name = forms.CharField()
  first_name = forms.CharField()
  needs_review = forms.BooleanField()
#  is_waiting = forms.BooleanField()
#  last_moved = forms.DateTimeField("last moved")
#  last_checkup = forms.DateTimeField("last checkup")
#  PRIORITY_CHOICES = (
#          ('CR', 'Critical'),
#          ('HI', 'High'),
#          ('MED', 'Medium'),
#          ('LOW', 'Low'),
#  )
#  priority = forms.CharField(max_length=3, choices=PRIORITY_CHOICES)
#  nurse_notes = forms.TextField()
#  doctor_notes = forms.TextField()
