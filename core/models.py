from django.db import models
from django.core.urlresolvers import reverse
import os
import uuid
from django.contrib.auth.models import User
from django.db.models import Avg
from geoposition.fields import GeopositionField

RATING_CHOICES = (
	(0, 'None'),
	(1, '*'),
	(2, '**'),
	(3, '***'),
	(4, '****'),
	(5, '*****'),
	)
YESNO_CHOICES = (
 (0, 'No'),
 (1, 'Yes')
 )

PLURAL_CHOICES = (
 (0, 'None'),
 (1, 'Minimal'),
 (2, 'Some'),
 (3, 'Ample')
 )

WIFI_CHOICES = (
 (0, 'None'),
 (1, 'Spotty'),
 (2, 'Strong')
 )

COFFEE_CHOICES = (
 (0, 'None'),
 (1, 'Basic'),
 (2, 'Good'),
 (3, 'Really Good'),
 (4, 'Great'),
 )

PINT_CHOICES = (
 (0, 'None'),
 (1, 'Just Pints'),
 (2, 'Pints and Sleeves'),
 )

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)
# Create your models here.'


class Location(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(null=True, blank=True,max_length=300)
    neighbourhood = models.CharField(null=True, blank=True,max_length=300)
    address = models.CharField(null=True, blank=True,max_length=300)
    hours = models.CharField(null=True, blank=True,max_length=300)
    website = models.CharField(null=True, blank=True,max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to='photos', null=True, blank=True)
    pints = models.IntegerField(choices=PINT_CHOICES, null=True, blank=True)
    wifi = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    selection = models.IntegerField(choices=COFFEE_CHOICES, null=True, blank=True)
    outdoor = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    food = models.IntegerField(choices=COFFEE_CHOICES, null=True, blank=True)
    position = GeopositionField(null=True, blank=True)

    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse(viewname="location_list", args=[self.id])

     #def get_absolute_url(self):
     #	return reverse(viewname="location_list", args=[self.id])

    def get_average_rating(self):
    	average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
        if average == None:
            return average
        else:
            return int(average)

    def get_reviews(self):
        return self.review_set.all()


class Review(models.Model):
    location = models.ForeignKey(Location)
    user = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)