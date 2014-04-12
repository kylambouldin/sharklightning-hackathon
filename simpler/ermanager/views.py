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
    print form.errors
    pat_id = request.session.get('patient_id')
    print str(pat_id)+"LETS SEE"
    if form.is_valid():
      patient = Patient.objects.get(id=pat_id)
      patient.last_name = form.cleaned_data['last_name']
      patient.first_name = form.cleaned_data['first_name']
      patient.needs_review = form.cleaned_data['needs_review']
      patient.is_waiting = form.cleaned_data['is_waiting']
      var = form.cleaned_data['loc']
      loc_temp = Location.objects.get(id=var)
      loc_temp.save()
      patient.loc = loc_temp
      patient.last_moved = form.cleaned_data['last_moved']
      patient.last_checkup = form.cleaned_data['last_checkup']
      patient.priority = form.cleaned_data['priority']
      patient.nurse_notes = form.cleaned_data['nurse_notes']
      patient.doctor_notes = form.cleaned_data['doctor_notes']
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
    form = PatientForm(initial={'last_name':patient.last_name,'first_name':patient.first_name,'needs_review':patient.needs_review,'is_waiting':patient.is_waiting ,'loc':patient.loc, 'last_moved':patient.last_moved ,'last_checkup': patient.last_checkup ,'priority': patient.priority ,'nurse_notes': patient.nurse_notes , 'doctor_notes':patient.doctor_notes})
  except Patient.DoesNotExist:
    raise Http404
  request.session['patient_id'] = patient_id
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
          dict1[num] = ("", "", "",)
    template = loader.get_template('ermanager/big_board.html')
    context = RequestContext(request, {
          'dict1':dict1,
    })
    return HttpResponse(template.render(context))



#Form definition

class PatientForm(forms.Form):
  last_name = forms.CharField()
  first_name = forms.CharField()
  needs_review = forms.BooleanField(required=False)
  is_waiting = forms.BooleanField(required=False)
  loc = forms.CharField()
  last_moved = forms.DateTimeField()
  last_checkup = forms.DateTimeField()
  priority = forms.CharField(max_length=3)
  nurse_notes = forms.CharField()
  doctor_notes = forms.CharField()
