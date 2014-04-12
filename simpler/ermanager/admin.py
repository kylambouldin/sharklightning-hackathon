from django.contrib import admin
from ermanager.models import Location, LastMoved, LastCheckup

# Register your models here.
# register location
admin.site.register(Location)

admin.site.register(LastMoved)

admin.site.register(LastCheckup)
