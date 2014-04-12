from django.shortcuts import render

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
