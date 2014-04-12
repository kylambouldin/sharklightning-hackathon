from django.contrib import admin
from ermanager.models import Location, Patient

# Register your models here.
# register location
admin.site.register(Location)

admin.site.register(Patient)
