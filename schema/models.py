from django.db import models

# Create your models here.
class Manufacturer(models.Model):
  manufacturer = models.CharField('Name of the manufacturer', max_length=45, unique=True)
  city = models.CharField('City in which the manufacturer is based', max_length=45)
  country = models.CharField('Country in which the manufacturer is based', max_length=45)
  url = models.URLField('URL to the manufacturers main website', max_length=45)
  founded = models.DateField('Year in which the manufacturer was founded')
  dissolved = models.DateField('Year in which the manufacturer was dissolved')

