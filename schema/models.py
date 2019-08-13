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
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

# Table to catalog filters
class Filter(models.Model):
  type = models.CharField('Filter type (e.g. Red, CPL, UV)', max_length=45) 
  thread = models.DecimalField('Diameter of screw thread in mm', max_digits=4, decimal_places=1)
  attenuation = models.DecimalField('Attenuation of this filter in decimal stops', max_digits=3, decimal_places=1)
  qty = models.IntegerField('Quantity of these filters available')
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

# Table to catalog different focusing methods
class FocusType(models.Model):
  name = models.CharField('Name of focus type', max_length=45)

# Table to catalog different negative sizes available. Negtives sizes are distinct from film formats.
class NegativeSize(models.Model):
  name = models.CharField('Common name of the negative size (e.g. 35mm, 6x7, etc)', max_length=45)
  width = models.DecimalField('Width of the negative size in mm' ,max_digits=4, decimal_places=1)
  height = models.DecimalField('Height of the negative size in mm', max_digits=4, decimal_places=1)
  crop_factor = models.DecimalField('Crop factor of this negative size', max_digits=4, decimal_places=2)
  area = models.IntegerField('Area of this negative size in sq. mm')
  aspect_ratio = models.DecimalField('Aspect ratio of this negative size, expressed as a single decimal (e.g. 3:2 is expressed as 1.5)',max_digits=4, decimal_places=2)

# Table to catalogue different film formats. These are distinct from negative sizes.
class Format(models.Model):
  format = models.CharField('The name of this film/sensor format', max_length=45)
  digital = models.BooleanField('Whether this is a digital format')

# Table to catalog flashes, flashguns and speedlights
class Flash(models.Model):
  model = models.CharField('Model name/number of the flash', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  guide_number = models.IntegerField('Guide number of the flash')
  gn_info = models.CharField('Extra freeform info about how the guide number was measured', max_length=45)
  battery_powered = models.BooleanField('Whether this flash takes batteries')
  pc_sync = models.BooleanField('Whether the flash has a PC sync socket')
  hot_shoe = models.BooleanField('Whether the flash has a hot shoe connection')
  light_stand = models.BooleanField('Whether the flash can be used on a light stand')
  battery_type = models.ForeignKey(Battery, on_delete=models.CASCADE)
  battery_qty = models.IntegerField('Quantity of batteries needed in this flash')
  manual_control = models.BooleanField('Whether this flash offers manual power control')
  swivel_head = models.BooleanField('Whether this flash has a horizontal swivel head')
  tilt_head = models.BooleanField('Whether this flash has a vertical tilt head')
  zoom = models.BooleanField('Whether this flash can zoom')
  dslr_safe = models.BooleanField('Whether this flash is safe to use with a digital camera')
  ttl = models.BooleanField('Whether this flash supports TTL metering')
  flash_protocol = models.ForeignKey(FlashProtocol, on_delete=models.CASCADE)
  trigger_voltage = models.DecimalField('Trigger voltage of the flash, in Volts', max_digits=5, decimal_places=1)
  own = models.BooleanField('Whether we currently own this flash')
  acquired = models.DateField('Date this flash was acquired')
  cost = models.DecimalField('Purchase cost of this flash', max_digits=6, decimal_places=2)

# Table to list enlargers
class Enlarger(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  model = models.CharField('Name/model of the enlarger', max_length=45)
  negative_size_id = models.ForeignKey(NegativeSize, on_delete=models.CASCADE)
  acquired = models.DateField('Date on which the enlarger was acquired')
  lost = models.DateField('Date on which the enlarger was lost/sold')
  introduced = models.IntegerField('Year in which the enlarger was introduced')
  discontinued = models.IntegerField('Year in which the enlarger was discontinued')
  cost = models.DecimalField('Purchase cost of the enlarger', max_digits=6, decimal_places=1)
  lost_price = models.DecimalField('Sale price of the enlarger', max_digits=6, decimal_places=1)
  
# Metering modes as defined by EXIF tag MeteringMode
class MeteringMode(models.Model):
  name = models.CharField('Name of metering mode as defined by EXIF tag MeteringMode', max_length=45, primary_key=True)

# Table to catalog different metering technologies and cell types
class MeteringType(models.Model):
  name = models.CharField('Name of the metering technology (e.g. Selenium)', max_length=45, primary_key=True)

# Table to catalog different lens mount standards. This is mostly used for camera lens mounts, but can also be used for enlarger and projector lenses.
class Mount(models.Model):
  mount = models.CharField('Name of this lens mount (e.g. Canon FD)', max_length=45)
  fixed = models.BooleanField('Whether this is a fixed (non-interchangable) lens mount')
  shutter_in_lens = models.BooleanField('Whether this lens mount system incorporates the shutter models.IntegerFieldo the lens')
  type = models.CharField('The physical mount type of this lens mount (e.g. Screw, Bayonet, etc)', max_length=25)
  purpose = models.CharField('The intended purpose of this lens mount (e.g. camera, enlarger, projector)', max_length=25)
  notes = models.CharField('Freeform notes field', max_length=100)
  digital_only = models.BooleanField('Whether this mount is models.intended only for digital cameras')
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

# Table to catalog light meters
class LightMeter(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  model = models.CharField('Model name or number of the light meter', max_length=45)
  metering_type = models.ForeignKey(MeteringType, on_delete=models.CASCADE)
  reflected = models.BooleanField('Whether the meter is capable of reflected-light metering')
  incident = models.BooleanField('Whether the meter is capable of incident-light metering')
  flash = models.BooleanField('Whether the meter is capable of flash metering')
  spot = models.BooleanField('Whether the meter is capable of spot metering')
  min_asa = models.IntegerField('Minimum ISO/ASA that this meter is capable of handling')
  max_asa = models.IntegerField('Maximum ISO/ASA that this meter is capable of handling')
  min_lv = models.IntegerField('Minimum light value (LV/EV) that this meter is capable of handling')
  max_lv = models.IntegerField('Maximum light value (LV/EV) that this meter is capable of handling')

# Table to catalog different paper stocks available
class PaperStock(models.Model):
  name = models.CharField('Name of this paper stock', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  resin_coated = models.BooleanField('Whether the paper is resin-coated')
  tonable = models.BooleanField('Whether this paper accepts chemical toning')
  colour = models.BooleanField('Whether this is a colour paper')
  finish = models.CharField('The finish of the paper surface', max_length=25)

# Table to catalog photographers
class Person(models.Model):
  name = models.CharField('Name of the photographer', max_length=45)

# Table to catalog chemical processes that can be used to develop film and paper
class Process(models.Model):
  name = models.CharField('Name of this developmenmt process (e.g. C-41, E-6)', max_length=25)
  colour = models.BooleanField('Whether this is a colour process')
  positive = models.BooleanField('Whether this is a positive/reversal process')

# Table to catalog teleconverters (multipliers)
class Teleconverter(models.Model):
  model = models.CharField('Model name of this teleconverter', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  mount = models.ForeignKey(Mount, on_delete=models.CASCADE)
  factor = models.DecimalField('Magnification factor of this teleconverter (numerical part only, e.g. 1.4)', max_digits=4, decimal_places=2)
  elements = models.IntegerField('Number of optical elements used in this teleconverter')
  groups = models.IntegerField('Number of optical groups used in this teleconverter')
  multicoated = models.BooleanField('Whether this teleconverter is multi-coated')

# Table to catalog paper toners that can be used during the printing process
class Toner(models.Model):
  name = models.CharField('Name of the toner', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  formulation = models.CharField('Chemical formulation of the toner', max_length=45)
  stock_dilution = models.CharField('Stock dilution of the toner', max_length=10)

# Table to list different brands of film stock
class FilmStock(models.Model):
  name = models.CharField('Name of the filmstock', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  iso = models.IntegerField('Nominal ISO speed of the film')
  colour = models.BooleanField('Whether the film is colour')
  panchromatic = models.BooleanField('Whether this film is panchromatic')
  process_id = models.ForeignKey(Process, on_delete=models.CASCADE)

# Table to catalog projectors (still and movie)
class Projector(models.Model):
  model = models.CharField('Model name of this projector', max_length=45)
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  mount = models.ForeignKey(Mount, on_delete=models.CASCADE)
  negative_size = models.ForeignKey(NegativeSize, on_delete=models.CASCADE)
  own = models.BooleanField('Whether we currently own this projector')
  cine = models.BooleanField('Whether this is a cine (movie) projector')

# Table to record bulk film stock, from which individual films can be cut
class BulkFilm(models.Model):
  format = models.ForeignKey(Format, on_delete=models.CASCADE)
  filmstock = models.ForeignKey(FilmStock, on_delete=models.CASCADE)
  purchase_date = models.DateField('Purchase date of this bulk roll')
  cost = models.DecimalField('Purchase cost of this bulk roll', max_digits=6, decimal_places=2)
  source = models.CharField('Place where this bulk roll was bought from', max_length=45)
  batch = models.CharField('Batch code of this bulk roll', max_length=45)
  expiry = models.DateField('Expiry date of this bulk roll')

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
  type = models.CharField('Name of the shutter type (e.g. Focal plane, Leaf, etc)', max_length=45)

# Table to list film and paper developers
class Developer(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  name = models.CharField('Name of the developer', max_length=45)
  for_paper = models.BooleanField('Whether this developer can be used with paper')
  for_film = models.BooleanField('Whether this developer can be used with film')
  chemistry = models.CharField('The key chemistry on which this developer is based (e.g. phenidone)', max_length=45)

# Table to catalog lens models
class LensModel(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  model = models.CharField('Model name of this lens', max_length=45)
  mount = models.ForeignKey(Mount, on_delete=models.CASCADE)
  zoom = models.BooleanField('Whether this is a zoom lens')
  min_focal_length = models.IntegerField('Shortest focal length of this lens, in mm')
  max_focal_length = models.IntegerField('Longest focal length of this lens, in mm')
  closest_focus = models.IntegerField('The closest focus possible with this lens, in cm')
  max_aperture = models.DecimalField('Maximum (widest) aperture available on this lens (numerical part only, e.g. 2.8)', max_digits=4, decimal_places=1)
  min_aperture = models.DecimalField('Minimum (narrowest) aperture available on this lens (numerical part only, e.g. 22)', max_digits=4, decimal_places=1)
  elements = models.IntegerField('Number of optical lens elements')
  groups = models.IntegerField('Number of optical groups')
  weight = models.IntegerField('Weight of this lens, in grammes (g)')
  nominal_min_angle_diag = models.IntegerField('Nominal minimum diagonal field of view from manufacturer specs')
  nominal_max_angle_diag = models.IntegerField('Nominal maximum diagonal field of view from manufacturer specs')
  aperture_blades = models.IntegerField('Number of aperture blades')
  autofocus = models.BooleanField('Whether this lens has autofocus capability')
  filter_thread = models.DecimalField('Diameter of lens filter thread, in mm', max_digits=4, decimal_places=1)
  magnification = models.DecimalField('Maximum magnification ratio of the lens, expressed like 0.765', max_digits=5, decimal_places=3)
  url = models.URLField('URL to more information about this lens')
  introduced = models.IntegerField('Year in which this lens model was introduced')
  discontinued = models.IntegerField('Year in which this lens model was discontinued')
  negative_size = models.ForeignKey(NegativeSize, on_delete=models.CASCADE)
  fixed_mount = models.BooleanField('Whether this is a fixed lens (i.e. on a compact camera)')
  notes = models.CharField('Freeform notes field', max_length=100)
  coating = models.CharField('Notes about the lens coating type', max_length=45)
  hood = models.CharField('Model number of the compatible lens hood', max_length=45)
  exif_lenstype = models.CharField('EXIF LensID number, if this lens has one officially registered. See documentation at http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/', max_length=45)
  rectilinear = models.BooleanField('Whether this is a rectilinear lens')
  length = models.IntegerField('Length of lens in mm')
  diameter = models.IntegerField('Width of lens in mm')
  image_circle = models.IntegerField('Diameter of image circle projected by lens, in mm')
  formula = models.CharField('Name of the type of lens formula (e.g. Tessar)', max_length=45)
  shutter_model = models.CharField('Name of the integrated shutter, if any', max_length=45)

# Table to catalog camera models - both cameras with fixed and interchangeable lenses
class CameraModel(models.Model):
  manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
  model = models.CharField('The model name of the camera', max_length=45)
  mount = models.ForeignKey(Mount, on_delete=models.CASCADE)
  format = models.ForeignKey(Format, on_delete=models.CASCADE)
  focus_type = models.ForeignKey(FocusType, on_delete=models.CASCADE)
  metering = models.BooleanField('Whether the camera has built-in metering')
  coupled_metering = models.BooleanField('Whether the camera''s meter is coupled automatically')
  metering_type = models.ForeignKey(MeteringType, on_delete=models.CASCADE)
  body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
  weight = models.IntegerField('Weight of the camera body (without lens or batteries) in grammes (g)')
  introduced = models.IntegerField('Year in which the camera model was introduced')
  discontinued = models.IntegerField('Year in which the camera model was discontinued')
  negative_size = models.ForeignKey(NegativeSize, on_delete=models.CASCADE)
  shutter_type = models.ForeignKey(ShutterType, on_delete=models.CASCADE)
  shutter_model = models.CharField('Model of shutter', max_length=45)
  cable_release = models.BooleanField('Whether the camera has the facility for a remote cable release')
  viewfinder_coverage = models.IntegerField('Percentage coverage of the viewfinder. Mostly applicable to SLRs.')
  power_drive = models.BooleanField('Whether the camera has models.IntegerFieldegrated motor drive')
  continuous_fps = models.DecimalField('The maximum rate at which the camera can shoot, in frames per second', max_digits=4, decimal_places=1)
  video = models.BooleanField('Whether the camera can take video/movie')
  digital = models.BooleanField('Whether this is a digital camera')
  fixed_mount = models.BooleanField('Whether the camera has a fixed lens')
  lensmodel = models.ForeignKey(LensModel, on_delete=models.CASCADE)
  battery_qty = models.IntegerField('Quantity of batteries needed')
  battery_type = models.ForeignKey(Battery, on_delete=models.CASCADE)
  notes = models.CharField('Freeform text field for extra notes', max_length=100)
  bulb = models.BooleanField('Whether the camera supports bulb (B) exposure')
  time = models.BooleanField('Whether the camera supports time (T) exposure')
  min_iso = models.IntegerField('Minimum ISO the camera will accept for metering')
  max_iso = models.IntegerField('Maximum ISO the camera will accept for metering')
  af_points = models.IntegerField('Number of autofocus points')
  int_flash = models.BooleanField('Whether the camera has an integrated flash')
  int_flash_gn = models.IntegerField('Guide number of internal flash')
  ext_flash = models.BooleanField(' Whether the camera supports an external flash')
  flash_metering = models.ForeignKey(FlashProtocol, on_delete=models.CASCADE)
  pc_sync = models.BooleanField('Whether the camera has a PC sync socket for flash')
  hotshoe = models.BooleanField('Whether the camera has a hotshoe')
  coldshoe = models.BooleanField('Whether the camera has a coldshoe or accessory shoe')
  #x_sync = models.ForeignKey(ShutterSpeed, on_delete=models.CASCADE)
  meter_min_ev = models.IntegerField('Lowest EV/LV the built-in meter supports')
  meter_max_ev = models.IntegerField('Highest EV/LV the built-in meter supports')
  dof_preview = models.BooleanField('Whether the camera has depth of field preview')
  tripod = models.BooleanField('Whether the camera has a tripod bush')
  shutter_speeds = models.ManyToManyField(ShutterSpeed)
  metering_modes = models.ManyToManyField(MeteringMode)
  exposure_programs = models.ManyToManyField(ExposureProgram)

# Table to catalog lenses
class Lens(models.Model):
  lensmodel_id = models.ForeignKey(LensModel, on_delete=models.CASCADE)
  serial = models.CharField('Serial number of this lens', max_length=45)
  date_code = models.CharField('Date code of this lens, if different from the serial number', max_length=45)
  manufactured = models.IntegerField('Year in which this specific lens was manufactured')
  acquired = models.DateField('Date on which this lens was acquired')
  cost = models.DecimalField('Price paid for this lens', max_digits=6, decimal_places=2)
  notes = models.CharField('Freeform notes field', max_length=45)
  own = models.BooleanField('Whether we currently own this lens')
  lost = models.DateField('Date on which lens was lost/sold/disposed')
  lost_price = models.DecimalField('Price for which the lens was sold', max_digits=6, decimal_places=2)
  source = models.CharField('Place where the lens was acquired from', max_length=150)
  condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
  condition_notes = models.CharField('Description of condition', max_length=150)

# Table to catalog cameras - both cameras with fixed lenses and cameras with interchangeable lenses
class Camera(models.Model):
  cameramodel = models.ForeignKey(CameraModel, on_delete=models.CASCADE)
  acquired = models.DateField('Date on which the camera was acquired')
  cost = models.DecimalField('Price paid for this camera', max_digits=6, decimal_places=2)
  serial = models.CharField('Serial number of the camera', max_length=45)
  datecode = models.CharField('Date code of the camera, if different from the serial number', max_length=45)
  manufactured = models.IntegerField('Year of manufacture of the camera')
  own = models.BooleanField('Whether the camera is currently owned')
  lens = models.ForeignKey(Lens, on_delete=models.CASCADE)
  notes = models.CharField('Freeform text field for extra notes', max_length=100)
  lost = models.DateField('Date on which the camera was lost/sold/etc')
  lost_price = models.DecimalField('Price at which the camera was sold', max_digits=6, decimal_places=2)
  source = models.CharField('Where the camera was acquired from', max_length=150)
  condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
  condition_notes = models.CharField('Description of condition', max_length=150)
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
  archive_id = models.ForeignKey(Archive, on_delete=models.CASCADE)

# Table to catalog negatives (including positives/slides). Negatives are created by cameras, belong to films and can be used to create scans or prints.
class Negative(models.Model):
  film = models.ForeignKey(Film, on_delete=models.CASCADE)
  frame = models.CharField('Frame number or code of this negative', max_length=8)
  caption = models.CharField('Caption of this picture', max_length=150)
  date = models.DateTimeField('Date & time on which this picture was taken')
  lens = models.ForeignKey(Lens, on_delete=models.CASCADE)
  shutter_speed = models.ForeignKey(ShutterSpeed, on_delete=models.CASCADE)
  aperture = models.DecimalField('Aperture used to take this picture (numerical part only)', max_digits=4, decimal_places=1)
  filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
  teleconverter = models.ForeignKey(Teleconverter, on_delete=models.CASCADE)
  notes = models.CharField('Extra freeform notes about this exposure', max_length=200)
  # mount_adapter = models.ForeignKey(MountAdapter, on_delete=models.CASCADE)
  focal_length = models.IntegerField('If a zoom lens was used, specify the focal length of the lens')
  latitude = models.DecimalField('Latitude of the location where the picture was taken', max_digits=9, decimal_places=6)
  longitude = models.DecimalField('Longitude of the location where the picture was taken', max_digits=9, decimal_places=6)
  flash = models.BooleanField('Whether flash was used')
  metering_mode = models.ForeignKey(MeteringMode, on_delete=models.CASCADE)
  exposure_program = models.ForeignKey(ExposureProgram, on_delete=models.CASCADE)
  photographer_id = models.ForeignKey(Person, on_delete=models.CASCADE)
  # copy_of = models.ForeignKey(Negative, on_delete=models.CASCADE)

# Table to catalog prints made from negatives
class Print(models.Model):
  negative = models.ForeignKey(Negative, on_delete=models.CASCADE)
  date = models.DateField('The date that the print was made')
  paper_stock = models.ForeignKey(PaperStock, on_delete=models.CASCADE)
  height = models.DecimalField('Height of the print in inches', max_digits=4, decimal_places=1)
  width = models.DecimalField('Width of the print in inches', max_digits=4, decimal_places=1)
  aperture = models.DecimalField('Aperture used to make this print (numerical part only, e.g. 5.6)', max_digits=3, decimal_places=1)
  exposure_time = models.DurationField('Exposure time of this print')
  filtration_grade = models.DecimalField('Contrast grade of paper used', max_digits=2, decimal_places=1)
  development_time = models.DurationField('Development time of this print')
  bleach_time = models.DurationField('Duration of bleaching')
  toner_id = models.ForeignKey(Toner, on_delete=models.CASCADE)
  toner_dilution = models.CharField('Dilution of the first toner used to make this print', max_length=8)
  toner_time = models.DurationField('Duration of first toning')
  #second_toner_id = models.ForeignKey(Toner, on_delete=models.CASCADE)
  #second_toner_dilution = models.CharField('Dilution of the first toner used to make this print', max_length=8)
  #second_toner_time = models.DurationField('Duration of second toning')
  own = models.BooleanField('Whether we currently own this print')
  location = models.CharField('The place where this print is currently', max_length=100)
  sold_price = models.DecimalField('Sale price of the print', max_digits=6, decimal_places=2)
  enlarger_id = models.ForeignKey(Enlarger, on_delete=models.CASCADE)
  lens_id = models.ForeignKey(Lens, on_delete=models.CASCADE)
  developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
  fine = models.BooleanField('Whether this is a fine print')
  notes = models.CharField('Freeform notes about this print, e.g. dodging, burning & complex toning', max_length=200)
  archive_id = models.ForeignKey(Archive, on_delete=models.CASCADE)
  printer_id = models.ForeignKey(Person, on_delete=models.CASCADE)

# Table to catalog motion picture films (movies)
class Movie(models.Model):
  title = models.CharField('Title of this movie', max_length=45)
  description = models.CharField('Description of this movie', max_length=200)
  camera_id = models.ForeignKey(Camera, on_delete=models.CASCADE)
  lens_id = models.ForeignKey(Lens, on_delete=models.CASCADE)
  format_id = models.ForeignKey(Format, on_delete=models.CASCADE)
  sound = models.BooleanField('Whether this movie has sound')
  fps = models.IntegerField('Frame rate of this movie, in fps')
  filmstock_id = models.ForeignKey(FilmStock, on_delete=models.CASCADE)
  feet = models.IntegerField('Length of this movie in feet')
  duration = models.DurationField('Duration of this movie')
  date_loaded = models.DateField('Date that the filmstock was loaded into a camera')
  date_shot = models.DateField('Date on which this movie was shot')
  date_processed = models.DateField('Date on which this movie was processed')
  process_id = models.ForeignKey(Process, on_delete=models.CASCADE)
  
# Table to catalog all repairs and servicing undertaken on cameras and lenses in the collection
class Repair(models.Model):
  camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
  lens = models.ForeignKey(Lens, on_delete=models.CASCADE)
  date = models.DateField('The date of the repair')
  summary = models.CharField('Brief summary of the repair', max_length=100)
  description = models.CharField('Longer description of the repair', max_length=500)

# Table to record all the images that have been scanned digitally
class Scan(models.Model):
  negative_id = models.ForeignKey(Negative, on_delete=models.CASCADE)
  print_id = models.ForeignKey(Print, on_delete=models.CASCADE)
  filename = models.CharField('Filename of the scan', max_length=128)
  date = models.DateField('Date that this scan was made')
  colour = models.BooleanField('Whether this is a colour image')
  width = models.IntegerField('Width of the scanned image in pixels')
  height = models.IntegerField('Height of the scanned image in pixels')

# Table to record orders for prints
class Order(models.Model):
  negative_id = models.ForeignKey(Negative, on_delete=models.CASCADE)
  width = models.IntegerField('Width of print to be made')
  height = models.IntegerField('Height of print to be made')
  added = models.DateField('Date that the order was placed')
  printed = models.BooleanField('Whether the print has been made')
  print_id = models.ForeignKey(Print, on_delete=models.CASCADE)
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

#class (NEGATIVEFORMAT_COMPAT = (
#   format_id = models.IntegerField(11) NOT NULL COMMENT 'ID of the film format',
#   negative_size_id = models.IntegerField(11) NOT NULL COMMENT 'ID of the negative size',
#   PRIMARY KEY (`format_id`,`negative_size_id`),
#   CONSTRAINT `format_id = FOREIGN KEY (`format_id`) REFERENCES `FORMAT = (`format_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `negative_size_id = FOREIGN KEY (`negative_size_id`) REFERENCES `NEGATIVE_SIZE = (`negative_size_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Table to record compatibility between film formats and negative sizes';

#class (SERIES_MEMBER = (
#   series_member_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this series membership',
#   series_id = models.IntegerField(11) 'ID of the series to which this camera model or lens model belongs',
#   cameramodel_id = models.IntegerField(11) 'ID of the camera model',
#   lensmodel_id = models.IntegerField(11) 'ID of the lens model',
#   PRIMARY KEY (`series_member_id`),
#   CONSTRAINT `fk_SERIES_MEMBER_1 = FOREIGN KEY (`series_id`) REFERENCES `SERIES = (`series_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_SERIES_MEMBER_2 = FOREIGN KEY (`cameramodel_id`) REFERENCES `CAMERAMODEL = (`cameramodel_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_SERIES_MEMBER_3 = FOREIGN KEY (`lensmodel_id`) REFERENCES `LENSMODEL = (`lensmodel_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to record which cameras and lenses belong to which series';

#class (SERIES = (
#   series_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this series',
#   name = models.CharField(45) 'Name of this collection, e.g. Canon FD SLRs',
#   PRIMARY KEY (`series_id`)
# ) 'Table to list all series of cameras and lenses';