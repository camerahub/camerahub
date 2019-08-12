from django.db import models

# Create your models here.
class Manufacturer(models.Model):
  name = models.CharField('Name of the manufacturer', max_length=45, unique=True)
  city = models.CharField('City in which the manufacturer is based', max_length=45)
  country = models.CharField('Country in which the manufacturer is based', max_length=45)
  url = models.URLField('URL to the manufacturers main website', max_length=45)
  founded = models.DateField('Year in which the manufacturer was founded')
  dissolved = models.DateField('Year in which the manufacturer was dissolved')

# Table to list types of accessories
class AccessoryType(models.Model):
  type = models.CharField('Type of accessory', max_length=45, unique=True)

# Table to catalog accessories that are not tracked in more specific tables
class Accessory(models.Model):
  type = models.ForeignKey(AccessoryType, on_delete=models.CASCADE)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  model = models.CharField('Model of the accessory', max_length=45)
  acquired = models.DateField('Date that this accessory was acquired')
  cost = models.DecimalField('Purchase cost of the accessory', max_digits=6, decimal_places=2)
  lost = models.DateField('Date that this accessory was lost')
  lost_price = models.DecimalField('Sale price of the accessory', max_digits=6, decimal_places=2)

