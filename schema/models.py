from django.db import models

# Create your models here.
class Manufacturer(models.Model):
  name = models.CharField('Name of the manufacturer', max_length=45, unique=True)
  city = models.CharField('City in which the manufacturer is based', max_length=45, blank=True)
  country = models.CharField('Country in which the manufacturer is based', max_length=45, blank=True)
  url = models.URLField('URL to the manufacturers main website', max_length=45, blank=True)
  founded = models.DateField('Year in which the manufacturer was founded', blank=True)
  dissolved = models.DateField('Year in which the manufacturer was dissolved', blank=True)

# Table to list types of accessories
class AccessoryType(models.Model):
  type = models.CharField('Type of accessory', max_length=45, unique=True)
  
# Table to catalog accessories that are not tracked in more specific tables
class Accessory(models.Model):
  type = models.ForeignKey(AccessoryType, on_delete=models.CASCADE)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  model = models.CharField('Model of the accessory', max_length=45)
  acquired = models.DateField('Date that this accessory was acquired', blank=True)
  cost = models.DecimalField('Purchase cost of the accessory', max_digits=6, decimal_places=2, blank=True)
  lost = models.DateField('Date that this accessory was lost', blank=True)
  lost_price = models.DecimalField('Sale price of the accessory', max_digits=6, decimal_places=2, blank=True)

# Table to list the different types of material that can be archived
class ArchiveType(models.Model):
  type = models.CharField('Name of this type of archive', max_length=45, unique=True)

# Table to list all archives that exist for storing physical media
class Archive(models.Model):
  type = models.ForeignKey(ArchiveType, on_delete=models.CASCADE)
  name = models.CharField('Name of this archive', max_length=45, unique=True)
  max_width = models.IntegerField('Maximum width of media that this archive can store', blank=True)
  max_height = models.IntegerField('Maximum height of media that this archive can store', blank=True)
  location = models.CharField('Location of this archive', max_length=45, blank=True)
  storage = models.CharField('The type of storage used for this archive, e.g. box, folder, ringbinder, etc', max_length=45, blank=True)
  sealed = models.BooleanField('Whether or not this archive is sealed (closed to new additions)', default=0)

# Table to catalog of types of battery
class Battery(models.Model):
  name = models.CharField('Common name of the battery', max_length=45, unique=True)
  voltage = models.DecimalField('Nominal voltage of the battery', max_digits=5, decimal_places=2, blank=True)
  chemistry = models.CharField('Battery chemistry (e.g. Alkaline, Lithium, etc)', max_length=45, blank=True)
  other_names = models.CharField('Alternative names for this kind of battery', max_length=45, blank=True)

# Table to catalog types of camera body style
class BodyType(models.Model):
  type = models.CharField('Name of camera body type (e.g. SLR, compact, etc)', max_length=45, unique=True)

# Table to list of physical condition descriptions that can be used to evaluate equipment
class Condition(models.Model):
   code = models.CharField('Condition shortcode (e.g. EXC)', max_length = 6, primary_key=True)
   name = models.CharField('Full name of condition (e.g. Excellent)', max_length=45)
   min_rating = models.IntegerField('The lowest percentage rating that encompasses this condition')
   max_rating = models.IntegerField('The highest percentage rating that encompasses this condition')
   description = models.CharField('Longer description of condition', max_length=300)
  
# Exposure programs as defined by EXIF tag ExposureProgram
class ExposureProgram(models.Model):
  name = models.CharField('Name of exposure program as defined by EXIF tag ExposureProgram', max_length=45, primary_key=True) 

# Table to catalog different protocols used to communicate with flashes
class FlashProtocol(models.Model):
  name = models.CharField('Name of the flash protocol', max_length=45) 
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)

# Table to catalog filters
class Filter(models.Model):
  type = models.CharField('Filter type (e.g. Red, CPL, UV)', max_length=45) 
  thread = models.DecimalField('Diameter of screw thread in mm', max_digits=4, decimal_places=1, blank=True)
  attenuation = models.DecimalField('Attenuation of this filter in decimal stops', max_digits=3, decimal_places=1, blank=True)
  qty = models.IntegerField('Quantity of these filters available', default=1, blank=True)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)

# Table to catalog different focusing methods
class FocusType(models.Model):
  name = models.CharField('Name of focus type', max_length=45, primary_key=True)

# Table to catalog different negative sizes available. Negtives sizes are distinct from film formats.
class NegativeSize(models.Model):
  name = models.CharField('Common name of the negative size (e.g. 35mm, 6x7, etc)', max_length=45, unique=True)
  width = models.DecimalField('Width of the negative size in mm' ,max_digits=4, decimal_places=1, blank=True)
  height = models.DecimalField('Height of the negative size in mm', max_digits=4, decimal_places=1, blank=True)
  crop_factor = models.DecimalField('Crop factor of this negative size', max_digits=4, decimal_places=2, blank=True)
  area = models.IntegerField('Area of this negative size in sq. mm', blank=True)
  aspect_ratio = models.DecimalField('Aspect ratio of this negative size, expressed as a single decimal (e.g. 3:2 is expressed as 1.5)',max_digits=4, decimal_places=2, blank=True)

# Table to catalogue different film formats. These are distinct from negative sizes.
class Format(models.Model):
  format = models.CharField('The name of this film/sensor format', max_length=45, unique=True)
  digital = models.BooleanField('Whether this is a digital format', blank=True)
  negative_size = models.ManyToManyField(NegativeSize, blank=True)

# Table to list all series of cameras and lenses
class Series(models.Model):
  name = models.CharField('Name of this collection, e.g. Canon FD SLRs', max_length=45, unique=True)

# Table to catalog flashes, flashguns and speedlights
class Flash(models.Model):
  model = models.CharField('Model name/number of the flash', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  guide_number = models.IntegerField('Guide number of the flash', blank=True)
  gn_info = models.CharField('Extra freeform info about how the guide number was measured', max_length=45, blank=True)
  battery_powered = models.BooleanField('Whether this flash takes batteries', blank=True)
  pc_sync = models.BooleanField('Whether the flash has a PC sync socket', blank=True)
  hot_shoe = models.BooleanField('Whether the flash has a hot shoe connection', blank=True)
  light_stand = models.BooleanField('Whether the flash can be used on a light stand', blank=True)
  battery_type = models.ForeignKey(Battery, on_delete=models.CASCADE, blank=True)
  battery_qty = models.IntegerField('Quantity of batteries needed in this flash', blank=True)
  manual_control = models.BooleanField('Whether this flash offers manual power control', blank=True)
  swivel_head = models.BooleanField('Whether this flash has a horizontal swivel head', blank=True)
  tilt_head = models.BooleanField('Whether this flash has a vertical tilt head', blank=True)
  zoom = models.BooleanField('Whether this flash can zoom', blank=True)
  dslr_safe = models.BooleanField('Whether this flash is safe to use with a digital camera', blank=True)
  ttl = models.BooleanField('Whether this flash supports TTL metering', blank=True)
  flash_protocol = models.ForeignKey(FlashProtocol, on_delete=models.CASCADE, blank=True)
  trigger_voltage = models.DecimalField('Trigger voltage of the flash, in Volts', max_digits=5, decimal_places=1, blank=True)
  own = models.BooleanField('Whether we currently own this flash', blank=True)
  acquired = models.DateField('Date this flash was acquired', blank=True)
  cost = models.DecimalField('Purchase cost of this flash', max_digits=6, decimal_places=2, blank=True)

# Table to list enlargers
class Enlarger(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  model = models.CharField('Name/model of the enlarger', max_length=45)
  negative_size = models.ForeignKey(NegativeSize, on_delete=models.CASCADE, blank=True)
  acquired = models.DateField('Date on which the enlarger was acquired', blank=True)
  lost = models.DateField('Date on which the enlarger was lost/sold', blank=True)
  introduced = models.IntegerField('Year in which the enlarger was introduced', blank=True)
  discontinued = models.IntegerField('Year in which the enlarger was discontinued', blank=True)
  cost = models.DecimalField('Purchase cost of the enlarger', max_digits=6, decimal_places=1, blank=True)
  lost_price = models.DecimalField('Sale price of the enlarger', max_digits=6, decimal_places=1, blank=True)
  
# Metering modes as defined by EXIF tag MeteringMode
class MeteringMode(models.Model):
  name = models.CharField('Name of metering mode as defined by EXIF tag MeteringMode', max_length=45, primary_key=True)

# Table to catalog different metering technologies and cell types
class MeteringType(models.Model):
  name = models.CharField('Name of the metering technology (e.g. Selenium)', max_length=45, primary_key=True)

# Table to catalog different lens mount standards. This is mostly used for camera lens mounts, but can also be used for enlarger and projector lenses.
class Mount(models.Model):
  mount = models.CharField('Name of this lens mount (e.g. Canon FD)', max_length=45, unique=True)
  fixed = models.BooleanField('Whether this is a fixed (non-interchangable) lens mount', default=0)
  shutter_in_lens = models.BooleanField('Whether this lens mount system incorporates the shutter models.IntegerFieldo the lens', default=0, blank=True)
  type = models.CharField('The physical mount type of this lens mount (e.g. Screw, Bayonet, etc)', max_length=25, blank=True)
  purpose = models.CharField('The intended purpose of this lens mount (e.g. camera, enlarger, projector)', max_length=25, blank=True)
  notes = models.CharField('Freeform notes field', max_length=100, blank=True)
  digital_only = models.BooleanField('Whether this mount is models.intended only for digital cameras', default=0, blank=True)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)

# Table to catalog light meters
class LightMeter(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  model = models.CharField('Model name or number of the light meter', max_length=45)
  metering_type = models.ForeignKey(MeteringType, on_delete=models.CASCADE, blank=True)
  reflected = models.BooleanField('Whether the meter is capable of reflected-light metering', blank=True)
  incident = models.BooleanField('Whether the meter is capable of incident-light metering', blank=True)
  flash = models.BooleanField('Whether the meter is capable of flash metering', blank=True)
  spot = models.BooleanField('Whether the meter is capable of spot metering', blank=True)
  min_asa = models.IntegerField('Minimum ISO/ASA that this meter is capable of handling', blank=True)
  max_asa = models.IntegerField('Maximum ISO/ASA that this meter is capable of handling', blank=True)
  min_lv = models.IntegerField('Minimum light value (LV/EV) that this meter is capable of handling', blank=True)
  max_lv = models.IntegerField('Maximum light value (LV/EV) that this meter is capable of handling', blank=True)

# Table to catalog different paper stocks available
class PaperStock(models.Model):
  name = models.CharField('Name of this paper stock', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  resin_coated = models.BooleanField('Whether the paper is resin-coated', blank=True)
  tonable = models.BooleanField('Whether this paper accepts chemical toning', blank=True)
  colour = models.BooleanField('Whether this is a colour paper', blank=True)
  finish = models.CharField('The finish of the paper surface', max_length=25, blank=True)

# Table to catalog photographers
class Person(models.Model):
  name = models.CharField('Name of the photographer', max_length=45, unique=True)

# Table to catalog chemical processes that can be used to develop film and paper
class Process(models.Model):
  name = models.CharField('Name of this developmenmt process (e.g. C-41, E-6)', max_length=25, unique=True)
  colour = models.BooleanField('Whether this is a colour process', blank=True)
  positive = models.BooleanField('Whether this is a positive/reversal process', blank=True)

# Table to catalog teleconverters (multipliers)
class Teleconverter(models.Model):
  model = models.CharField('Model name of this teleconverter', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  mount = models.ForeignKey(Mount, on_delete=models.CASCADE, blank=True)
  factor = models.DecimalField('Magnification factor of this teleconverter (numerical part only, e.g. 1.4)', max_digits=4, decimal_places=2, blank=True)
  elements = models.IntegerField('Number of optical elements used in this teleconverter', blank=True)
  groups = models.IntegerField('Number of optical groups used in this teleconverter', blank=True)
  multicoated = models.BooleanField('Whether this teleconverter is multi-coated', blank=True)

# Table to catalog paper toners that can be used during the printing process
class Toner(models.Model):
  name = models.CharField('Name of the toner', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  formulation = models.CharField('Chemical formulation of the toner', max_length=45, blank=True)
  stock_dilution = models.CharField('Stock dilution of the toner', max_length=10, blank=True)

# Table to list different brands of film stock
class FilmStock(models.Model):
  name = models.CharField('Name of the filmstock', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  iso = models.IntegerField('Nominal ISO speed of the film', blank=True)
  colour = models.BooleanField('Whether the film is colour', blank=True)
  panchromatic = models.BooleanField('Whether this film is panchromatic', blank=True)
  process = models.ForeignKey(Process, on_delete=models.CASCADE, blank=True)

# Table to catalog projectors (still and movie)
class Projector(models.Model):
  model = models.CharField('Model name of this projector', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  mount = models.ForeignKey(Mount, on_delete=models.CASCADE, blank=True)
  negative_size = models.ForeignKey(NegativeSize, on_delete=models.CASCADE, blank=True)
  own = models.BooleanField('Whether we currently own this projector', blank=True)
  cine = models.BooleanField('Whether this is a cine (movie) projector', blank=True)

# Table to record bulk film stock, from which individual films can be cut
class BulkFilm(models.Model):
  format = models.ForeignKey(Format, on_delete=models.CASCADE)
  filmstock = models.ForeignKey(FilmStock, on_delete=models.CASCADE)
  purchase_date = models.DateField('Purchase date of this bulk roll', blank=True)
  cost = models.DecimalField('Purchase cost of this bulk roll', max_digits=6, decimal_places=2, blank=True)
  source = models.CharField('Place where this bulk roll was bought from', max_length=45, blank=True)
  batch = models.CharField('Batch code of this bulk roll', max_length=45, blank=True)
  expiry = models.DateField('Expiry date of this bulk roll', blank=True)

# Table to catalogue filter adapter rings
class FilterAdapter(models.Model):
  camera_thread = models.DecimalField('Diameter of camera-facing screw thread in mm', max_digits=3, decimal_places=1)
  filter_thread = models.DecimalField('Diameter of filter-facing screw thread in mm', max_digits=3, decimal_places=1)

# Table to catalog adapters to mount lenses on other cameras
# class MountAdapter(models.Model):
#   lens_mount = models.ForeignKey(Mount, on_delete=models.CASCADE)
#   camera_mount = models.ForeignKey(Mount, on_delete=models.CASCADE)
#   has_optics = models.BooleanField('Whether this adapter includes optical elements')
#   infinity_focus = models.BooleanField('Whether this adapter allows infinity focus')
#   notes = models.CharField('Freeform notes', max_length=100)

# Table to list all possible shutter speeds
class ShutterSpeed(models.Model):
  shutter_speed = models.CharField('Shutter speed in fractional notation, e.g. 1/250', max_length=10, primary_key=True)
  duration = models.DecimalField('Shutter speed in models.DecimalField notation, e.g. 0.04', max_digits=9, decimal_places=5)

# Table to catalog the different types of camera shutter
class ShutterType(models.Model):
  type = models.CharField('Name of the shutter type (e.g. Focal plane, Leaf, etc)', max_length=45, unique=True)

# Table to list film and paper developers
class Developer(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  name = models.CharField('Name of the developer', max_length=45)
  for_paper = models.BooleanField('Whether this developer can be used with paper', blank=True)
  for_film = models.BooleanField('Whether this developer can be used with film', blank=True)
  chemistry = models.CharField('The key chemistry on which this developer is based (e.g. phenidone)', max_length=45, blank=True)

# Table to catalog lens models
class LensModel(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  model = models.CharField('Model name of this lens', max_length=45)
  mount = models.ForeignKey(Mount, on_delete=models.CASCADE, blank=True)
  zoom = models.BooleanField('Whether this is a zoom lens', blank=True)
  min_focal_length = models.IntegerField('Shortest focal length of this lens, in mm', blank=True)
  max_focal_length = models.IntegerField('Longest focal length of this lens, in mm', blank=True)
  closest_focus = models.IntegerField('The closest focus possible with this lens, in cm', blank=True)
  max_aperture = models.DecimalField('Maximum (widest) aperture available on this lens (numerical part only, e.g. 2.8)', max_digits=4, decimal_places=1, blank=True)
  min_aperture = models.DecimalField('Minimum (narrowest) aperture available on this lens (numerical part only, e.g. 22)', max_digits=4, decimal_places=1, blank=True)
  elements = models.IntegerField('Number of optical lens elements', blank=True)
  groups = models.IntegerField('Number of optical groups', blank=True)
  weight = models.IntegerField('Weight of this lens, in grammes (g)', blank=True)
  nominal_min_angle_diag = models.IntegerField('Nominal minimum diagonal field of view from manufacturer specs', blank=True)
  nominal_max_angle_diag = models.IntegerField('Nominal maximum diagonal field of view from manufacturer specs', blank=True)
  aperture_blades = models.IntegerField('Number of aperture blades', blank=True)
  autofocus = models.BooleanField('Whether this lens has autofocus capability', blank=True)
  filter_thread = models.DecimalField('Diameter of lens filter thread, in mm', max_digits=4, decimal_places=1, blank=True)
  magnification = models.DecimalField('Maximum magnification ratio of the lens, expressed like 0.765', max_digits=5, decimal_places=3, blank=True)
  url = models.URLField('URL to more information about this lens', blank=True)
  introduced = models.IntegerField('Year in which this lens model was introduced', blank=True)
  discontinued = models.IntegerField('Year in which this lens model was discontinued', blank=True)
  negative_size = models.ForeignKey(NegativeSize, on_delete=models.CASCADE, blank=True)
  fixed_mount = models.BooleanField('Whether this is a fixed lens (i.e. on a compact camera)', blank=True)
  notes = models.CharField('Freeform notes field', max_length=100, blank=True)
  coating = models.CharField('Notes about the lens coating type', max_length=45, blank=True)
  hood = models.CharField('Model number of the compatible lens hood', max_length=45, blank=True)
  exif_lenstype = models.CharField('EXIF LensID number, if this lens has one officially registered. See documentation at http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/', max_length=45, blank=True)
  rectilinear = models.BooleanField('Whether this is a rectilinear lens', default=1, blank=True)
  length = models.IntegerField('Length of lens in mm', blank=True)
  diameter = models.IntegerField('Width of lens in mm', blank=True)
  image_circle = models.IntegerField('Diameter of image circle projected by lens, in mm', blank=True)
  formula = models.CharField('Name of the type of lens formula (e.g. Tessar)', max_length=45, blank=True)
  shutter_model = models.CharField('Name of the integrated shutter, if any', max_length=45, blank=True)
  series = models.ManyToManyField(Series, blank=True)

# Table to catalog camera models - both cameras with fixed and interchangeable lenses
class CameraModel(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True)
  model = models.CharField('The model name of the camera', max_length=45)
  mount = models.ForeignKey(Mount, on_delete=models.CASCADE, blank=True)
  format = models.ForeignKey(Format, on_delete=models.CASCADE, blank=True)
  focus_type = models.ForeignKey(FocusType, on_delete=models.CASCADE, blank=True)
  metering = models.BooleanField('Whether the camera has built-in metering', blank=True)
  coupled_metering = models.BooleanField('Whether the camera''s meter is coupled automatically', blank=True)
  metering_type = models.ForeignKey(MeteringType, on_delete=models.CASCADE, blank=True)
  body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, blank=True)
  weight = models.IntegerField('Weight of the camera body (without lens or batteries) in grammes (g)', blank=True)
  introduced = models.IntegerField('Year in which the camera model was introduced', blank=True)
  discontinued = models.IntegerField('Year in which the camera model was discontinued', blank=True)
  negative_size = models.ForeignKey(NegativeSize, on_delete=models.CASCADE, blank=True)
  shutter_type = models.ForeignKey(ShutterType, on_delete=models.CASCADE, blank=True)
  shutter_model = models.CharField('Model of shutter', max_length=45, blank=True)
  cable_release = models.BooleanField('Whether the camera has the facility for a remote cable release', blank=True)
  viewfinder_coverage = models.IntegerField('Percentage coverage of the viewfinder. Mostly applicable to SLRs.', blank=True)
  power_drive = models.BooleanField('Whether the camera has integrated motor drive', blank=True)
  continuous_fps = models.DecimalField('The maximum rate at which the camera can shoot, in frames per second', max_digits=4, decimal_places=1, blank=True)
  video = models.BooleanField('Whether the camera can take video/movie', blank=True)
  digital = models.BooleanField('Whether this is a digital camera', default=0, blank=True)
  fixed_mount = models.BooleanField('Whether the camera has a fixed lens', blank=True)
  lensmodel = models.ForeignKey(LensModel, on_delete=models.CASCADE, blank=True)
  battery_qty = models.IntegerField('Quantity of batteries needed', blank=True)
  battery_type = models.ForeignKey(Battery, on_delete=models.CASCADE, blank=True)
  notes = models.CharField('Freeform text field for extra notes', max_length=100, blank=True)
  bulb = models.BooleanField('Whether the camera supports bulb (B) exposure', blank=True)
  time = models.BooleanField('Whether the camera supports time (T) exposure', blank=True)
  min_iso = models.IntegerField('Minimum ISO the camera will accept for metering', blank=True)
  max_iso = models.IntegerField('Maximum ISO the camera will accept for metering', blank=True)
  af_points = models.IntegerField('Number of autofocus points', blank=True)
  int_flash = models.BooleanField('Whether the camera has an integrated flash', blank=True)
  int_flash_gn = models.IntegerField('Guide number of internal flash', blank=True)
  ext_flash = models.BooleanField(' Whether the camera supports an external flash', blank=True)
  flash_metering = models.ForeignKey(FlashProtocol, on_delete=models.CASCADE, blank=True)
  pc_sync = models.BooleanField('Whether the camera has a PC sync socket for flash', blank=True)
  hotshoe = models.BooleanField('Whether the camera has a hotshoe', blank=True)
  coldshoe = models.BooleanField('Whether the camera has a coldshoe or accessory shoe', blank=True)
  #x_sync = models.ForeignKey(ShutterSpeed, on_delete=models.CASCADE, blank=True)
  meter_min_ev = models.IntegerField('Lowest EV/LV the built-in meter supports', blank=True)
  meter_max_ev = models.IntegerField('Highest EV/LV the built-in meter supports', blank=True)
  dof_preview = models.BooleanField('Whether the camera has depth of field preview', blank=True)
  tripod = models.BooleanField('Whether the camera has a tripod bush', blank=True)
  shutter_speeds = models.ManyToManyField(ShutterSpeed, blank=True)
  metering_modes = models.ManyToManyField(MeteringMode, blank=True)
  exposure_programs = models.ManyToManyField(ExposureProgram, blank=True)
  series = models.ManyToManyField(Series, blank=True)

# Table to catalog lenses
class Lens(models.Model):
  lensmodel = models.ForeignKey(LensModel, on_delete=models.CASCADE)
  serial = models.CharField('Serial number of this lens', max_length=45, blank=True)
  date_code = models.CharField('Date code of this lens, if different from the serial number', max_length=45, blank=True)
  manufactured = models.IntegerField('Year in which this specific lens was manufactured', blank=True)
  acquired = models.DateField('Date on which this lens was acquired', blank=True)
  cost = models.DecimalField('Price paid for this lens', max_digits=6, decimal_places=2, blank=True)
  notes = models.CharField('Freeform notes field', max_length=45, blank=True)
  own = models.BooleanField('Whether we currently own this lens', blank=True)
  lost = models.DateField('Date on which lens was lost/sold/disposed', blank=True)
  lost_price = models.DecimalField('Price for which the lens was sold', max_digits=6, decimal_places=2, blank=True)
  source = models.CharField('Place where the lens was acquired from', max_length=150, blank=True)
  condition = models.ForeignKey(Condition, on_delete=models.CASCADE, blank=True)
  condition_notes = models.CharField('Description of condition', max_length=150, blank=True)

# Table to catalog cameras - both cameras with fixed lenses and cameras with interchangeable lenses
class Camera(models.Model):
  cameramodel = models.ForeignKey(CameraModel, on_delete=models.CASCADE)
  acquired = models.DateField('Date on which the camera was acquired', blank=True)
  cost = models.DecimalField('Price paid for this camera', max_digits=6, decimal_places=2, blank=True)
  serial = models.CharField('Serial number of the camera', max_length=45, blank=True)
  datecode = models.CharField('Date code of the camera, if different from the serial number', max_length=45, blank=True)
  manufactured = models.IntegerField('Year of manufacture of the camera', blank=True)
  own = models.BooleanField('Whether the camera is currently owned', blank=True)
  lens = models.ForeignKey(Lens, on_delete=models.CASCADE, blank=True)
  notes = models.CharField('Freeform text field for extra notes', max_length=100, blank=True)
  lost = models.DateField('Date on which the camera was lost/sold/etc', blank=True)
  lost_price = models.DecimalField('Price at which the camera was sold', max_digits=6, decimal_places=2, blank=True)
  source = models.CharField('Where the camera was acquired from', max_length=150, blank=True)
  condition = models.ForeignKey(Condition, on_delete=models.CASCADE, blank=True)
  condition_notes = models.CharField('Description of condition', max_length=150, blank=True)
  #display_lens = models.ForeignKey(Lens, on_delete=models.CASCADE)

# Table to list films which consist of one or more negatives. A film can be a roll film, one or more sheets of sheet film, one or more photographic plates, etc.
class Film(models.Model):
  filmstock = models.ForeignKey(FilmStock, on_delete=models.CASCADE)
  exposed_at = models.IntegerField('ISO at which the film was exposed')
  format = models.ForeignKey(Format, on_delete=models.CASCADE)
  date_loaded = models.DateField('Date when the film was loaded into a camera')
  date_processed = models.DateField('Date when the film was processed')
  camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
  title = models.CharField('Title of the film', max_length=150)
  frames = models.IntegerField('Expected (not actual) number of frames from the film')
  developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
  directory = models.CharField('Name of the directory that contains the scanned images from this film', max_length=100)
  dev_uses = models.IntegerField('Number of previous uses of the developer')
  dev_time = models.DurationField('Duration of development')
  dev_temp = models.DecimalField('Temperature of development', max_digits=3, decimal_places=1)
  dev_n = models.IntegerField('Number of the Push/Pull rating of the film, e.g. N+1, N-2')
  development_notes = models.CharField('Extra freeform notes about the development process', max_length=200)
  bulk_film = models.ForeignKey(BulkFilm, on_delete=models.CASCADE)
  bulk_film_loaded = models.DateField('Date that this film was cut from a bulk roll')
  film_batch = models.CharField('Batch number of the film', max_length=45)
  expiry_date = models.DateField('Expiry date of the film')
  purchase_date = models.DateField('Date this film was purchased')
  price = models.DecimalField('Price paid for this film', max_digits=6, decimal_places=2)
  processed_by = models.CharField('Person or place that processed this film', max_length=45)
  archive = models.ForeignKey(Archive, on_delete=models.CASCADE)

# Table to catalog negatives (including positives/slides). Negatives are created by cameras, belong to films and can be used to create scans or prints.
class Negative(models.Model):
  film = models.ForeignKey(Film, on_delete=models.CASCADE)
  frame = models.CharField('Frame number or code of this negative', max_length=8)
  caption = models.CharField('Caption of this picture', max_length=150, blank=True)
  date = models.DateTimeField('Date & time on which this picture was taken', blank=True)
  lens = models.ForeignKey(Lens, on_delete=models.CASCADE, blank=True)
  shutter_speed = models.ForeignKey(ShutterSpeed, on_delete=models.CASCADE, blank=True)
  aperture = models.DecimalField('Aperture used to take this picture (numerical part only)', max_digits=4, decimal_places=1, blank=True)
  filter = models.ForeignKey(Filter, on_delete=models.CASCADE, blank=True)
  teleconverter = models.ForeignKey(Teleconverter, on_delete=models.CASCADE, blank=True)
  notes = models.CharField('Extra freeform notes about this exposure', max_length=200, blank=True)
  # mount_adapter = models.ForeignKey(MountAdapter, on_delete=models.CASCADE, blank=True)
  focal_length = models.IntegerField('If a zoom lens was used, specify the focal length of the lens', blank=True)
  latitude = models.DecimalField('Latitude of the location where the picture was taken', max_digits=9, decimal_places=6, blank=True)
  longitude = models.DecimalField('Longitude of the location where the picture was taken', max_digits=9, decimal_places=6, blank=True)
  flash = models.BooleanField('Whether flash was used', blank=True)
  metering_mode = models.ForeignKey(MeteringMode, on_delete=models.CASCADE, blank=True)
  exposure_program = models.ForeignKey(ExposureProgram, on_delete=models.CASCADE, blank=True)
  photographer = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True)
  # copy_of = models.ForeignKey(Negative, on_delete=models.CASCADE)

# Table to catalog prints made from negatives
class Print(models.Model):
  negative = models.ForeignKey(Negative, on_delete=models.CASCADE)
  date = models.DateField('The date that the print was made', blank=True)
  paper_stock = models.ForeignKey(PaperStock, on_delete=models.CASCADE, blank=True)
  height = models.DecimalField('Height of the print in inches', max_digits=4, decimal_places=1, blank=True)
  width = models.DecimalField('Width of the print in inches', max_digits=4, decimal_places=1, blank=True)
  aperture = models.DecimalField('Aperture used to make this print (numerical part only, e.g. 5.6)', max_digits=3, decimal_places=1, blank=True)
  exposure_time = models.DurationField('Exposure time of this print', blank=True)
  filtration_grade = models.DecimalField('Contrast grade of paper used', max_digits=2, decimal_places=1, blank=True)
  development_time = models.DurationField('Development time of this print', blank=True)
  bleach_time = models.DurationField('Duration of bleaching', blank=True)
  toner = models.ForeignKey(Toner, on_delete=models.CASCADE, blank=True)
  toner_dilution = models.CharField('Dilution of the first toner used to make this print', max_length=8, blank=True)
  toner_time = models.DurationField('Duration of first toning', blank=True)
  #second_toner = models.ForeignKey(Toner, on_delete=models.CASCADE, blank=True)
  #second_toner_dilution = models.CharField('Dilution of the first toner used to make this print', max_length=8, blank=True)
  #second_toner_time = models.DurationField('Duration of second toning', blank=True)
  own = models.BooleanField('Whether we currently own this print', blank=True)
  location = models.CharField('The place where this print is currently', max_length=100, blank=True)
  sold_price = models.DecimalField('Sale price of the print', max_digits=6, decimal_places=2, blank=True)
  enlarger = models.ForeignKey(Enlarger, on_delete=models.CASCADE, blank=True)
  lens = models.ForeignKey(Lens, on_delete=models.CASCADE, blank=True)
  developer = models.ForeignKey(Developer, on_delete=models.CASCADE, blank=True)
  fine = models.BooleanField('Whether this is a fine print', blank=True)
  notes = models.CharField('Freeform notes about this print, e.g. dodging, burning & complex toning', max_length=200, blank=True)
  archive = models.ForeignKey(Archive, on_delete=models.CASCADE, blank=True)
  printer = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True)

# Table to catalog motion picture films (movies)
class Movie(models.Model):
  title = models.CharField('Title of this movie', max_length=45)
  description = models.CharField('Description of this movie', max_length=200, blank=True)
  camera = models.ForeignKey(Camera, on_delete=models.CASCADE, blank=True)
  lens = models.ForeignKey(Lens, on_delete=models.CASCADE, blank=True)
  format = models.ForeignKey(Format, on_delete=models.CASCADE, blank=True)
  sound = models.BooleanField('Whether this movie has sound', blank=True)
  fps = models.IntegerField('Frame rate of this movie, in fps', blank=True)
  filmstock = models.ForeignKey(FilmStock, on_delete=models.CASCADE, blank=True)
  feet = models.IntegerField('Length of this movie in feet', blank=True)
  duration = models.DurationField('Duration of this movie', blank=True)
  date_loaded = models.DateField('Date that the filmstock was loaded into a camera', blank=True)
  date_shot = models.DateField('Date on which this movie was shot', blank=True)
  date_processed = models.DateField('Date on which this movie was processed', blank=True)
  process = models.ForeignKey(Process, on_delete=models.CASCADE, blank=True)
  
# Table to catalog all repairs and servicing undertaken on cameras and lenses in the collection
class Repair(models.Model):
  camera = models.ForeignKey(Camera, on_delete=models.CASCADE, blank=True)
  lens = models.ForeignKey(Lens, on_delete=models.CASCADE, blank=True)
  date = models.DateField('The date of the repair', blank=True)
  summary = models.CharField('Brief summary of the repair', max_length=100)
  description = models.CharField('Longer description of the repair', max_length=500, blank=True)

# Table to record all the images that have been scanned digitally
class Scan(models.Model):
  negative = models.ForeignKey(Negative, on_delete=models.CASCADE, blank=True)
  print = models.ForeignKey(Print, on_delete=models.CASCADE, blank=True)
  filename = models.CharField('Filename of the scan', max_length=128)
  date = models.DateField('Date that this scan was made', blank=True)
  colour = models.BooleanField('Whether this is a colour image', blank=True)
  width = models.IntegerField('Width of the scanned image in pixels', blank=True)
  height = models.IntegerField('Height of the scanned image in pixels', blank=True)

# Table to record orders for prints
class Order(models.Model):
  negative = models.ForeignKey(Negative, on_delete=models.CASCADE)
  width = models.IntegerField('Width of print to be made', blank=True)
  height = models.IntegerField('Height of print to be made', blank=True)
  added = models.DateField('Date that the order was placed', blank=True)
  printed = models.BooleanField('Whether the print has been made', blank=True)
  print = models.ForeignKey(Print, on_delete=models.CASCADE, blank=True)
  recipient = models.ForeignKey(Person, on_delete=models.CASCADE)
  
#class (ACCESSORY_COMPAT = (
#   compat_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for this compatibility',
#   accessory_id = models.IntegerField(11) NOT NULL COMMENT 'ID of the accessory',
#   cameramodel_id = models.IntegerField(11) 'ID of the compatible camera model',
#   lensmodel_id = models.IntegerField(11) 'ID of the compatible lens',
#   PRIMARY KEY (`compat_id`),
#   CONSTRAINT `fk_ACCESSORY_COMPAT_1 = FOREIGN KEY (`accessory_id`) REFERENCES `ACCESSORY = (`accessory_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_ACCESSORY_COMPAT_2 = FOREIGN KEY (`cameramodel_id`) REFERENCES `CAMERAMODEL = (`cameramodel_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_ACCESSORY_COMPAT_3 = FOREIGN KEY (`lensmodel_id`) REFERENCES `LENSMODEL = (`lensmodel_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) 'Table to define compatibility between accessories and cameras or lenses';

#class (LOG = (
#   log_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of the log entry',
#   datetime = datetime 'Timestamp for the log entry',
#   type = models.CharField(45) 'Type of log message, e.g. ADD, EDIT',
#   message = models.CharField(450) 'Log message',
#   PRIMARY KEY (`log_id`)
# ) 'Table to store data modification logs';