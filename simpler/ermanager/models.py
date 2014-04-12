from django.db import models
import datetime

# Create your models here.
class Location(models.Model):
    # Str nameornumber
    name = models.CharField(max_length=50)
    def __unicode__(self):
      return self.name

class Paitent(models.Model):
    #bool needsReview
    needs_review = models.BooleanField()

    # Location loc
    loc = models.ForeignKey(Location)

    # Datetime LastMoved
    last_moved = models.DateTimeField('last moved')

    # Datetime LastCheckup
    last_checkup = models.DateTimeField('last checkup')
