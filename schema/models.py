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

# Table to list the different types of material that can be archived
class ArchiveType(models.Model):
  type = models.CharField('Name of this type of archive', max_length=45)

# Table to list all archives that exist for storing physical media
class Archive(models.Model):
  type = models.ForeignKey(ArchiveType, on_delete=models.CASCADE)
  name = models.CharField('Name of this archive', max_length=45)
  max_width = models.IntegerField('Maximum width of media that this archive can store')
  max_height = models.IntegerField('Maximum height of media that this archive can store')
  location = models.CharField('Location of this archive', max_length=45)
  storage = models.CharField('The type of storage used for this archive, e.g. box, folder, ringbinder, etc', max_length=45)
  sealed = models.BooleanField('Whether or not this archive is sealed (closed to new additions)', default=0)

# Table to catalog of types of battery
class Battery(models.Model):
  name = models.CharField('Common name of the battery', max_length=45)
  voltage = models.DecimalField('Nominal voltage of the battery', max_digits=5, decimal_places=2)
  chemistry = models.CharField('Battery chemistry (e.g. Alkaline, Lithium, etc)', max_length=45)
  other_names = models.CharField('Alternative names for this kind of battery', max_length=45)
 
# Table to catalog types of camera body style
class BodyType(models.Model):
   type = models.CharField('Name of camera body type (e.g. SLR, compact, etc)', max_length=45, unique=True)

