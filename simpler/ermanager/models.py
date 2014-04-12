from django.db import models
import datetime

# Create your models here.
class Location(models.Model):

    # Str nameornumber
    number = models.IntegerField()

    def __unicode__(self):
      return u'%d' %(self.number)

class Patient(models.Model):
    # Patient first name
    first_name = models.CharField(max_length=250)

    # Paitent last name
    last_name = models.CharField(max_length=250)

    #bool needsReview
    needs_review = models.BooleanField()

    #bool isWaiting
    is_waiting = models.BooleanField()

    # Location loc
    loc = models.ForeignKey(Location)

    # Datetime LastMoved
    last_moved = models.DateTimeField('last moved')

    # Datetime LastCheckup
    last_checkup = models.DateTimeField('last checkup')

    PRIORITY_CHOICES = (
            ('CR', 'Critical'),
            ('HI', 'High'),
            ('MED', 'Medium'),
            ('LOW', 'Low'),
    )

    priority = models.CharField(max_length=3, choices=PRIORITY_CHOICES)

    nurse_notes = models.TextField(null=True, blank=True)

    doctor_notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
      return self.last_name+', '+self.first_name
