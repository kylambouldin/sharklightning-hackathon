from django.db import models
import datetime

# Create your models here.
class Location(models.Model):
    # Str nameornumber
    name = models.CharField(max_length=50)
    def __unicode__(self):
      return self.name

class Paitent(models.Model):
    # Paitent first name
    first_name = models.CharField(max_length=250)

    # Paitent last name
    last_name = models.CharField(max_length=250)

    #bool needsReview
    needs_review = models.BooleanField()

    # Location loc
    loc = models.ForeignKey(Location)

    # Datetime LastMoved
    last_moved = models.DateTimeField('last moved')

    # Datetime LastCheckup
    last_checkup = models.DateTimeField('last checkup')
    def __unicode__(self):
      return self.first_name+', '+self.last_name
