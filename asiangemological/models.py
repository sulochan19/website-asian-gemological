from django.db import models
from datetime import datetime
class Stone(models.Model):
    ITEM_CHOICES = (
   ('Gemstone', 'Gemstone'),
   ('Jewelry', 'Jewelry'),
   ('Rudrakshya', 'Rudrakshya')
   )
    item_type = models.CharField(choices=ITEM_CHOICES, max_length=128)
    verification_number = models.CharField(max_length=50,unique=True)
    date = models.DateField()
    item_described = models.CharField(max_length=50,blank=True)
    shape = models.CharField(max_length=50,blank=True)
    weight = models.CharField(max_length=50,blank=True)
    dimension = models.CharField(max_length=50,blank=True)
    color = models.CharField(max_length=50,blank=True)
    other = models.CharField(max_length=50,blank=True)
    #fields for gemstone
    transparency = models.CharField(max_length=50,blank=True)
    specific_gravity = models.CharField(max_length=50,blank=True)
    refractive_index = models.CharField(max_length=50,blank=True)
    identified_as = models.CharField(max_length=50,blank=True)
    
    #fields for jewelry
    metal_type = models.CharField(max_length=50,blank=True)
    clarity = models.CharField(max_length=50,blank=True)
    
    # fields for rudrakshya
    natural_faces = models.CharField(max_length=50,blank=True)
    artificial_faces = models.CharField(max_length=50,blank=True)
    indication_of_tampering = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.verification_number