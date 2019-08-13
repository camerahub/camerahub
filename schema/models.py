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

# CREATE TABLE `ACCESSORY_COMPAT = (
#   compat_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for this compatibility',
#   accessory_id = models.IntegerField(11) NOT NULL COMMENT 'ID of the accessory',
#   cameramodel_id = models.IntegerField(11) 'ID of the compatible camera model',
#   lensmodel_id = models.IntegerField(11) 'ID of the compatible lens',
#   PRIMARY KEY (`compat_id`),
#   CONSTRAINT `fk_ACCESSORY_COMPAT_1 = FOREIGN KEY (`accessory_id`) REFERENCES `ACCESSORY = (`accessory_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_ACCESSORY_COMPAT_2 = FOREIGN KEY (`cameramodel_id`) REFERENCES `CAMERAMODEL = (`cameramodel_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_ACCESSORY_COMPAT_3 = FOREIGN KEY (`lensmodel_id`) REFERENCES `LENSMODEL = (`lensmodel_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) 'Table to define compatibility between accessories and cameras or lenses';


# CREATE TABLE `CAMERAMODEL = (
#   cameramodel_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Auto-incremented camera model ID',
#   manufacturer_id = models.IntegerField(11) 'Denotes the manufacturer of the camera.',
#   model = models.CharField(45) 'The model name of the camera',
#   mount_id = models.IntegerField(11) 'Denotes the lens mount of the camera if it is an models.IntegerFielderchangeable-lens camera',
#   format_id = models.IntegerField(11) 'Denotes the film format of the camera',
#   focus_type_id = models.IntegerField(11) 'Denotes the focus type of the camera',
#   metering = models.BooleanField('Whether the camera has built-in metering',
#   coupled_metering = models.BooleanField('Whether the camera''s meter is coupled automatically',
#   metering_type_id = models.IntegerField(11) 'Denotes the technology used in the meter',
#   body_type_id = models.IntegerField(11) 'Denotes the style of camera body',
#   weight = models.IntegerField(11) 'Weight of the camera body (without lens or batteries) in grammes (g)',
#   introduced = smallint(6) 'Year in which the camera model was models.IntegerFieldroduced',
#   discontinued = smallint(6) 'Year in which the camera model was discontinued',
#   negative_size_id = models.IntegerField(11) 'Denotes the size of negative made by the camera',
#   shutter_type_id = models.IntegerField(11) 'Denotes type of shutter',
#   shutter_model = models.CharField(45) 'Model of shutter',
#   cable_release = models.BooleanField('Whether the camera has the facility for a remote cable release',
#   viewfinder_coverage = models.IntegerField(11) 'Percentage coverage of the viewfinder. Mostly applicable to SLRs.',
#   power_drive = models.BooleanField('Whether the camera has models.IntegerFieldegrated motor drive',
#   continuous_fps = decimal(3,1) 'The maximum rate at which the camera can shoot, in frames per second',
#   video = models.BooleanField('Whether the camera can take video/movie',
#   digital = models.BooleanField('Whether this is a digital camera',
#   fixed_mount = models.BooleanField('Whether the camera has a fixed lens',
#   lensmodel_id = models.IntegerField(11) 'If fixed_mount is true, specify the lensmodel_id',
#   battery_qty = models.IntegerField(11) 'Quantity of batteries needed',
#   battery_type = models.IntegerField(11) 'Denotes type of battery needed',
#   notes = text 'Freeform text field for extra notes',
#   bulb = models.BooleanField('Whether the camera supports bulb (B) exposure',
#   time = models.BooleanField('Whether the camera supports time (T) exposure',
#   min_iso = models.IntegerField(11) 'Minimum ISO the camera will accept for metering',
#   max_iso = models.IntegerField(11) 'Maximum ISO the camera will accept for metering',
#   af_points = tinyint(4) 'Number of autofocus points',
#   int_flash = models.BooleanField('Whether the camera has an models.IntegerFieldegrated flash',
#   int_flash_gn = tinyint(4) 'Guide number of models.IntegerFieldernal flash',
#   ext_flash = models.BooleanField(' Whether the camera supports an external flash',
#   flash_metering = models.CharField(12) 'Flash metering protocol',
#   pc_sync = models.BooleanField('Whether the camera has a PC sync socket for flash',
#   hotshoe = models.BooleanField('Whether the camera has a hotshoe',
#   coldshoe = models.BooleanField('Whether the camera has a coldshoe or accessory shoe',
#   x_sync = models.CharField(6) 'X-sync shutter speed, expressed like 1/125',
#   meter_min_ev = tinyint(4) 'Lowest EV/LV the built-in meter supports',
#   meter_max_ev = tinyint(4) 'Highest EV/LV the built-in meter supports',
#   dof_preview = models.BooleanField('Whether the camera has depth of field preview',
#   tripod = models.BooleanField('Whether the camera has a tripod bush',
#   PRIMARY KEY (`cameramodel_id`),
#   CONSTRAINT `fk_CAMERAMODEL_1 = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_10 = FOREIGN KEY (`battery_type`) REFERENCES `BATTERY = (`battery_type`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_2 = FOREIGN KEY (`mount_id`) REFERENCES `MOUNT = (`mount_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_3 = FOREIGN KEY (`format_id`) REFERENCES `FORMAT = (`format_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_4 = FOREIGN KEY (`focus_type_id`) REFERENCES `FOCUS_TYPE = (`focus_type_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_5 = FOREIGN KEY (`metering_type_id`) REFERENCES `METERING_TYPE = (`metering_type_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_6 = FOREIGN KEY (`body_type_id`) REFERENCES `BODY_TYPE = (`body_type_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_7 = FOREIGN KEY (`negative_size_id`) REFERENCES `NEGATIVE_SIZE = (`negative_size_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_8 = FOREIGN KEY (`shutter_type_id`) REFERENCES `SHUTTER_TYPE = (`shutter_type_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERAMODEL_9 = FOREIGN KEY (`lensmodel_id`) REFERENCES `LENSMODEL = (`lensmodel_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) COMMENT='Table to catalog camera models - both cameras with fixed lenses and cameras with models.IntegerFielderchangeable lenses';


# CREATE TABLE `CAMERA = (
#   camera_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Auto-incremented camera ID',
#   cameramodel_id = models.IntegerField(11) 'ID which specifies the model of camera',
#   acquired = date 'Date on which the camera was acquired',
#   cost = decimal(6,2) 'Price paid for the camera, in local currency units',
#   serial = models.CharField(45) 'Serial number of the camera',
#   datecode = models.CharField(12) 'Date code of the camera, if different from the serial number',
#   manufactured = smallint(6) 'Year of manufacture of the camera',
#   own = models.BooleanField('Whether the camera is currently owned',
#   lens_id = models.IntegerField(11) 'If fixed_mount is true, specify the lens_id',
#   notes = text 'Freeform text field for extra notes',
#   lost = date 'Date on which the camera was lost/sold/etc',
#   lost_price = decimal(6,2) 'Price at which the camera was sold',
#   source = models.CharField(150) 'Where the camera was acquired from',
#   condition_id = models.IntegerField(11) 'Denotes the cosmetic condition of the camera',
#   condition = text 'Description of condition',
#   display_lens = models.IntegerField(11) 'Lens ID of the lens that this camera should normally be displayed with',
#   PRIMARY KEY (`camera_id`),
#   UNIQUE KEY `display_lens_UNIQUE = (`display_lens`),
#   CONSTRAINT `fk_CAMERA_3 = FOREIGN KEY (`display_lens`) REFERENCES `LENS = (`lens_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERA_5 = FOREIGN KEY (`display_lens`) REFERENCES `LENS = (`lens_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_CAMERA_6 = FOREIGN KEY (`cameramodel_id`) REFERENCES `CAMERAMODEL = (`cameramodel_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_condition = FOREIGN KEY (`condition_id`) REFERENCES `CONDITION = (`condition_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) COMMENT='Table to catalog cameras - both cameras with fixed lenses and cameras with models.IntegerFielderchangeable lenses';


# CREATE TABLE `CONDITION = (
#   condition_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique condition ID',
#   code = models.CharField(6) 'Condition shortcode (e.g. EXC)',
#   name = models.CharField(45) 'Full name of condition (e.g. Excellent)',
#   min_rating = models.IntegerField(11) 'The lowest percentage rating that encompasses this condition',
#   max_rating = models.IntegerField(11) 'The highest percentage rating that encompasses this condition',
#   description = models.CharField(300) 'Longer description of condition',
#   PRIMARY KEY (`condition_id`)
# ) 'Table to list of physical condition descriptions that can be used to evaluate equipment';


# CREATE TABLE `EXPOSURE_PROGRAM_AVAILABLE = (
#   cameramodel_id = models.IntegerField(11) NOT NULL COMMENT 'ID of camera model',
#   exposure_program_id = models.IntegerField(11) NOT NULL COMMENT 'ID of exposure program',
#   PRIMARY KEY (`cameramodel_id`,`exposure_program_id`),
#   CONSTRAINT `fk_EXPOSURE_PROGRAM_AVAILABLE_1 = FOREIGN KEY (`cameramodel_id`) REFERENCES `CAMERAMODEL = (`cameramodel_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_EXPOSURE_PROGRAM_AVAILABLE_2 = FOREIGN KEY (`exposure_program_id`) REFERENCES `EXPOSURE_PROGRAM = (`exposure_program_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) 'Table to associate cameras with available exposure programs';


# CREATE TABLE `EXPOSURE_PROGRAM = (
#   exposure_program_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'ID of exposure program as defined by EXIF tag ExposureProgram',
#   exposure_program = models.CharField(45) 'Name of exposure program as defined by EXIF tag ExposureProgram',
#   PRIMARY KEY (`exposure_program_id`)
# ) 'Exposure programs as defined by EXIF tag ExposureProgram';


# CREATE TABLE `FILM_BULK = (
#   film_bulk_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this bulk roll of film',
#   format_id = models.IntegerField(11) 'ID of the format of this bulk roll',
#   filmstock_id = models.IntegerField(11) 'ID of the filmstock',
#   purchase_date = date 'Purchase date of this bulk roll',
#   cost = decimal(5,2) 'Purchase cost of this bulk roll',
#   source = models.CharField(45) 'Place where this bulk roll was bought from',
#   batch = models.CharField(45) 'Batch code of this bulk roll',
#   expiry = date 'Expiry date of this bulk roll',
#   PRIMARY KEY (`film_bulk_id`),
#   CONSTRAINT `fk_FILM_BULK_1 = FOREIGN KEY (`format_id`) REFERENCES `FORMAT = (`format_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_FILM_BULK_2 = FOREIGN KEY (`filmstock_id`) REFERENCES `FILMSTOCK = (`filmstock_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to record bulk film stock, from which individual films can be cut';


# CREATE TABLE `FILM = (
#   film_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of the film',
#   filmstock_id = models.IntegerField(11) 'ID of the filmstock used',
#   exposed_at = models.IntegerField(11) 'ISO at which the film was exposed',
#   format_id = models.IntegerField(11) 'ID of the film format',
#   date_loaded = date 'Date when the film was loaded models.IntegerFieldo a camera',
#   date = date 'Date when the film was processed',
#   camera_id = models.IntegerField(11) 'ID of the camera that exposed this film',
#   notes = models.CharField(145) 'Title of the film',
#   frames = models.IntegerField(11) 'Expected (not actual) number of frames from the film',
#   developer_id = models.IntegerField(11) 'ID of the developer used to process this film',
#   directory = models.CharField(100) 'Name of the directory that contains the scanned images from this film',
#   dev_uses = models.IntegerField(11) 'Numnber of previous uses of the developer',
#   dev_time = time 'Duration of development',
#   dev_temp = decimal(3,1) 'Temperature of development',
#   dev_n = models.IntegerField(11) 'Number of the Push/Pull rating of the film, e.g. N+1, N-2',
#   development_notes = models.CharField(200) 'Extra freeform notes about the development process',
#   film_bulk_id = models.IntegerField(11) 'ID of bulk film from which this film was cut',
#   film_bulk_loaded = date 'Date that this film was cut from a bulk roll',
#   film_batch = models.CharField(45) 'Batch number of the film',
#   film_expiry = date 'Expiry date of the film',
#   purchase_date = date 'Date this film was purchased',
#   price = decimal(4,2) 'Price paid for this film',
#   processed_by = models.CharField(45) 'Person or place that processed this film',
#   archive_id = models.IntegerField(11) 'ID of the archive to which this film belongs',
#   PRIMARY KEY (`film_id`),
#   CONSTRAINT `fk_FILM_1 = FOREIGN KEY (`developer_id`) REFERENCES `DEVELOPER = (`developer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_FILM_3 = FOREIGN KEY (`archive_id`) REFERENCES `ARCHIVE = (`archive_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_FILM_4 = FOREIGN KEY (`film_bulk_id`) REFERENCES `FILM_BULK = (`film_bulk_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_camera_id = FOREIGN KEY (`camera_id`) REFERENCES `CAMERA = (`camera_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_filmstock_id = FOREIGN KEY (`filmstock_id`) REFERENCES `FILMSTOCK = (`filmstock_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_format_id = FOREIGN KEY (`format_id`) REFERENCES `FORMAT = (`format_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) 'Table to list films which consist of one or more negatives. A film can be a roll film, one or more sheets of sheet film, one or more photographic plates, etc.';


# CREATE TABLE `FILMSTOCK = (
#   filmstock_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of the filmstock',
#   manufacturer_id = models.IntegerField(11) 'ID of the manufacturer of the film',
#   name = models.CharField(45) 'Name of the film',
#   iso = models.IntegerField(11) 'Nominal ISO speed of the film',
#   colour = models.BooleanField('Whether the film is colour',
#   process_id = models.IntegerField(11) 'ID of the normal process for this film',
#   panchromatic = models.BooleanField('Whether this film is panchromatic',
#   PRIMARY KEY (`filmstock_id`),
#   CONSTRAINT `fk_FILMSTOCK_1 = FOREIGN KEY (`process_id`) REFERENCES `PROCESS = (`process_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_manufacturer_id = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) 'Table to list different brands of film stock';


# CREATE TABLE `FILTER_ADAPTER = (
#   filter_adapter_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of filter adapter',
#   camera_thread = decimal(3,1) 'Diameter of camera-facing screw thread in mm',
#   filter_thread = decimal(3,1) 'Diameter of filter-facing screw thread in mm',
#   PRIMARY KEY (`filter_adapter_id`)
# ) 'Table to catalogue filter adapter rings';


# CREATE TABLE `FILTER = (
#   filter_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique filter ID',
#   thread = decimal(4,1) 'Diameter of screw thread in mm',
#   type = models.CharField(45) 'Filter type (e.g. Red, CPL, UV)',
#   attenuation = decimal(2,1) 'Attenuation of this filter in decimal stops',
#   qty = models.IntegerField(11) 'Quantity of these filters available',
#   manufacturer_id = models.IntegerField(11) 'Denotes the manufacturer of the filter.',
#   PRIMARY KEY (`filter_id`),
#   CONSTRAINT `fk_FILTER_1 = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog filters';


# CREATE TABLE `FLASH_PROTOCOL = (
#   flash_protocol_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this flash protocol',
#   manufacturer_id = models.IntegerField(11) 'ID of the manufacturer that models.IntegerFieldroduced this flash protocol',
#   name = models.CharField(45) 'Name of the flash protocol',
#   PRIMARY KEY (`flash_protocol_id`)
# ) 'Table to catalog different protocols used to communicate with flashes';


# CREATE TABLE `FLASH = (
#   flash_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of external flash unit',
#   manufacturer_id = models.IntegerField(11) 'Manufacturer ID of the flash',
#   model = models.CharField(45) 'Model name/number of the flash',
#   guide_number = models.IntegerField(11) 'Guide number of the flash',
#   gn_info = models.CharField(45) 'Extra freeform info about how the guide number was measured',
#   battery_powered = models.BooleanField('Whether this flash takes batteries',
#   pc_sync = models.BooleanField('Whether the flash has a PC sync socket',
#   hot_shoe = models.BooleanField('Whether the flash has a hot shoe connection',
#   light_stand = models.BooleanField('Whether the flash can be used on a light stand',
#   battery_type_id = models.IntegerField(11) 'ID of battery type',
#   battery_qty = models.IntegerField(11) 'Quantity of batteries needed in this flash',
#   manual_control = models.BooleanField('Whether this flash offers manual power control',
#   swivel_head = models.BooleanField('Whether this flash has a horizontal swivel head',
#   tilt_head = models.BooleanField('Whether this flash has a vertical tilt head',
#   zoom = models.BooleanField('Whether this flash can zoom',
#   dslr_safe = models.BooleanField('Whether this flash is safe to use with a digital camera',
#   ttl = models.BooleanField('Whether this flash supports TTL metering',
#   flash_protocol_id = models.IntegerField(11) 'ID of flash TTL metering protocol',
#   trigger_voltage = decimal(4,1) 'Trigger voltage of the flash, in Volts',
#   own = models.BooleanField('Whether we currently own this flash',
#   acquired = date 'Date this flash was acquired',
#   cost = decimal(5,2) 'Purchase cost of this flash',
#   PRIMARY KEY (`flash_id`),
#   CONSTRAINT `fk_FLASH_1 = FOREIGN KEY (`flash_protocol_id`) REFERENCES `FLASH_PROTOCOL = (`flash_protocol_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_FLASH_2 = FOREIGN KEY (`battery_type_id`) REFERENCES `BATTERY = (`battery_type`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catlog flashes, flashguns and speedlights';


# CREATE TABLE `FOCUS_TYPE = (
#   focus_type_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of focus type',
#   focus_type = models.CharField(45) 'Name of focus type',
#   PRIMARY KEY (`focus_type_id`)
# ) 'Table to catalog different focusing methods';


# CREATE TABLE `FORMAT = (
#   format_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for this format',
#   format = models.CharField(45) 'The name of this film/sensor format',
#   digital = models.BooleanField('Whether this is a digital format',
#   PRIMARY KEY (`format_id`)
# ) 'Table to catalogue different film formats. These are distinct from negative sizes.';


# CREATE TABLE `LENSMODEL = (
#   lensmodel_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for this lens model',
#   mount_id = models.IntegerField(11) 'Denotes the ID of the lens mount, if this is an models.IntegerFielderchangeable lens',
#   zoom = models.BooleanField('Whether this is a zoom lens',
#   min_focal_length = models.IntegerField(11) 'Shortest focal length of this lens, in mm',
#   max_focal_length = models.IntegerField(11) 'Longest focal length of this lens, in mm',
#   manufacturer_id = models.IntegerField(11) 'ID of the manufacturer of this lens',
#   model = models.CharField(45) 'Model name of this lens',
#   closest_focus = models.IntegerField(11) 'The closest focus possible with this lens, in cm',
#   max_aperture = decimal(4,1) 'Maximum (widest) aperture available on this lens (numerical part only, e.g. 2.8)',
#   min_aperture = decimal(4,1) 'Minimum (narrowest) aperture available on this lens (numerical part only, e.g. 22)',
#   elements = models.IntegerField(11) 'Number of optical lens elements',
#   groups = models.IntegerField(11) 'Number of optical groups',
#   weight = models.IntegerField(11) 'Weight of this lens, in grammes (g)',
#   nominal_min_angle_diag = models.IntegerField(11) 'Nominal minimum diagonal field of view from manufacturer''s specs',
#   nominal_max_angle_diag = models.IntegerField(11) 'Nominal maximum diagonal field of view from manufacturer''s specs',
#   aperture_blades = models.IntegerField(11) 'Number of aperture blades',
#   autofocus = models.BooleanField('Whether this lens has autofocus capability',
#   filter_thread = decimal(4,1) 'Diameter of lens filter thread, in mm',
#   magnification = decimal(5,3) 'Maximum magnification ratio of the lens, expressed like 0.765',
#   url = models.CharField(145) 'URL to more information about this lens',
#   introduced = smallint(6) 'Year in which this lens model was models.IntegerFieldroduced',
#   discontinued = smallint(6) 'Year in which this lens model was discontinued',
#   negative_size_id = models.IntegerField(11) 'ID of the negative size which this lens is designed for',
#   fixed_mount = models.BooleanField('Whether this is a fixed lens (i.e. on a compact camera)',
#   notes = text 'Freeform notes field',
#   coating = models.CharField(45) 'Notes about the lens coating type',
#   hood = models.CharField(45) 'Model number of the compatible lens hood',
#   exif_lenstype = models.CharField(45) 'EXIF LensID number, if this lens has one officially registered. See documentation at http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/',
#   rectilinear = models.BooleanField('Whether this is a rectilinear lens',
#   length = models.IntegerField(11) 'Length of lens in mm',
#   diameter = models.IntegerField(11) 'Width of lens in mm',
#   image_circle = models.IntegerField(11) 'Diameter of image circle projected by lens, in mm',
#   formula = models.CharField(45) 'Name of the type of lens formula (e.g. Tessar)',
#   shutter_model = models.CharField(45) 'Name of the models.IntegerFieldegrated shutter, if any',
#   PRIMARY KEY (`lensmodel_id`),
#   CONSTRAINT `fk_LENSMODEL_1 = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_LENSMODEL_2 = FOREIGN KEY (`mount_id`) REFERENCES `MOUNT = (`mount_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_LENSMODEL_3 = FOREIGN KEY (`negative_size_id`) REFERENCES `NEGATIVE_SIZE = (`negative_size_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog lens models';


# CREATE TABLE `LENS = (
#   lens_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for this lens',
#   lensmodel_id = models.IntegerField(11) DEFAULT NULL,
#   serial = models.CharField(45) 'Serial number of this lens',
#   date_code = models.CharField(45) 'Date code of this lens, if different from the serial number',
#   manufactured = smallint(6) 'Year in which this specific lens was manufactured',
#   acquired = date 'Date on which this lens was acquired',
#   cost = decimal(6,2) 'Price paid for this lens in local currency units',
#   notes = text 'Freeform notes field',
#   own = models.BooleanField('Whether we currently own this lens',
#   lost = date 'Date on which lens was lost/sold/disposed',
#   lost_price = decimal(6,2) 'Price for which the lens was sold',
#   source = models.CharField(150) 'Place where the lens was acquired from',
#   condition_id = models.IntegerField(11) 'Denotes the cosmetic condition of the camera',
#   condition = text 'Description of condition',
#   PRIMARY KEY (`lens_id`),
#   CONSTRAINT `fk_LENS_1 = FOREIGN KEY (`condition_id`) REFERENCES `CONDITION = (`condition_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_LENS_5 = FOREIGN KEY (`lensmodel_id`) REFERENCES `LENSMODEL = (`lensmodel_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog lenses';


# CREATE TABLE `LIGHT_METER = (
#   light_meter_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for this light meter',
#   manufacturer_id = models.IntegerField(11) 'Denotes ID of manufacturer of the light meter',
#   model = models.CharField(45) 'Model name or number of the light meter',
#   metering_type = models.IntegerField(11) 'ID of metering technology used in this light meter',
#   reflected = models.BooleanField('Whether the meter is capable of reflected-light metering',
#   incident = models.BooleanField('Whether the meter is capable of incident-light metering',
#   flash = models.BooleanField('Whether the meter is capable of flash metering',
#   spot = models.BooleanField('Whether the meter is capable of spot metering',
#   min_asa = models.IntegerField(11) 'Minimum ISO/ASA that this meter is capable of handling',
#   max_asa = models.IntegerField(11) 'Maximum ISO/ASA that this meter is capable of handling',
#   min_lv = models.IntegerField(11) 'Minimum light value (LV/EV) that this meter is capable of handling',
#   max_lv = models.IntegerField(11) 'Maximum light value (LV/EV) that this meter is capable of handling',
#   PRIMARY KEY (`light_meter_id`),
#   CONSTRAINT `fk_LIGHT_METER_1 = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_LIGHT_METER_2 = FOREIGN KEY (`metering_type`) REFERENCES `METERING_TYPE = (`metering_type_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog light meters';


# CREATE TABLE `LOG = (
#   log_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of the log entry',
#   datetime = datetime 'Timestamp for the log entry',
#   type = models.CharField(45) 'Type of log message, e.g. ADD, EDIT',
#   message = models.CharField(450) 'Log message',
#   PRIMARY KEY (`log_id`)
# ) 'Table to store data modification logs';


# CREATE TABLE `METERING_MODE_AVAILABLE = (
#   cameramodel_id = models.IntegerField(11) NOT NULL COMMENT 'ID of camera model',
#   metering_mode_id = models.IntegerField(11) NOT NULL COMMENT 'ID of metering mode',
#   PRIMARY KEY (`cameramodel_id`,`metering_mode_id`),
#   CONSTRAINT `fk_METERING_MODE_AVAILABLE_1 = FOREIGN KEY (`cameramodel_id`) REFERENCES `CAMERAMODEL = (`cameramodel_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_METERING_MODE_AVAILABLE_2 = FOREIGN KEY (`metering_mode_id`) REFERENCES `METERING_MODE = (`metering_mode_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) 'Table to associate cameras with available metering modes';


# CREATE TABLE `METERING_MODE = (
#   metering_mode_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'ID of metering mode as defined by EXIF tag MeteringMode',
#   metering_mode = models.CharField(45) 'Name of metering mode as defined by EXIF tag MeteringMode',
#   PRIMARY KEY (`metering_mode_id`)
# ) 'Metering modes as defined by EXIF tag MeteringMode';


# CREATE TABLE `METERING_TYPE = (
#   metering_type_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of the metering type',
#   metering = models.CharField(45) 'Name of the metering type (e.g. Selenium)',
#   PRIMARY KEY (`metering_type_id`)
# ) 'Table to catalog different metering technologies and cell types';


# CREATE TABLE `MOUNT_ADAPTER = (
#   mount_adapter_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of lens mount adapter',
#   lens_mount = models.IntegerField(11) 'ID of the mount used between the adapter and the lens',
#   camera_mount = models.IntegerField(11) 'ID of the mount used between the adapter and the camera',
#   has_optics = models.BooleanField('Whether this adapter includes optical elements',
#   infinity_focus = models.BooleanField('Whether this adapter allows infinity focus',
#   notes = models.CharField(45) 'Freeform notes',
#   PRIMARY KEY (`mount_adapter_id`),
#   CONSTRAINT `fk_MOUNT_ADAPTER_1 = FOREIGN KEY (`lens_mount`) REFERENCES `MOUNT = (`mount_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_MOUNT_ADAPTER_2 = FOREIGN KEY (`camera_mount`) REFERENCES `MOUNT = (`mount_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog adapters to mount lenses on other cameras';


# CREATE TABLE `MOUNT = (
#   mount_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this lens mount',
#   mount = models.CharField(45) 'Name of this lens mount (e.g. Canon FD)',
#   fixed = models.BooleanField('Whether this is a fixed (non-interchangable) lens mount',
#   shutter_in_lens = models.BooleanField('Whether this lens mount system incorporates the shutter models.IntegerFieldo the lens',
#   type = models.CharField(25) 'The physical mount type of this lens mount (e.g. Screw, Bayonet, etc)',
#   purpose = models.CharField(25) 'The models.IntegerFieldended purpose of this lens mount (e.g. camera, enlarger, projector)',
#   notes = models.CharField(45) 'Freeform notes field',
#   digital_only = models.BooleanField('Whether this mount is models.IntegerFieldended only for digital cameras',
#   manufacturer_id = models.IntegerField(11) 'Manufacturer ID of this lens mount, if applicable',
#   PRIMARY KEY (`mount_id`),
#   CONSTRAINT `fk_MOUNT_1 = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog different lens mount standards. This is mostly used for camera lens mounts, but can also be used for enlarger and projector lenses.';


# CREATE TABLE `MOVIE = (
#   movie_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for this motion picture film / movie',
#   title = models.CharField(45) 'Title of this movie',
#   camera_id = models.IntegerField(11) 'ID of the camera used to shoot this movie',
#   lens_id = models.IntegerField(11) 'ID of the lens used to shoot this movie',
#   format_id = models.IntegerField(11) 'ID of the film format on which this movie was shot',
#   sound = models.BooleanField('Whether this movie has sound',
#   fps = models.IntegerField(11) 'Frame rate of this movie, in fps',
#   filmstock_id = models.IntegerField(11) 'ID of the filmstock used to shoot this movie',
#   feet = models.IntegerField(11) 'Length of this movie in feet',
#   date_loaded = date 'Date that the filmstock was loaded models.IntegerFieldo a camera',
#   date_shot = date 'Date on which this movie was shot',
#   date_processed = date 'Date on which this movie was processed',
#   process_id = models.IntegerField(11) 'ID of the process used to develop this film',
#   description = models.CharField(100) 'Table to catalog motion picture films (movies)',
#   PRIMARY KEY (`movie_id`),
#   CONSTRAINT `fk_MOVIE_1 = FOREIGN KEY (`camera_id`) REFERENCES `CAMERA = (`camera_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_MOVIE_2 = FOREIGN KEY (`lens_id`) REFERENCES `LENS = (`lens_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_MOVIE_3 = FOREIGN KEY (`format_id`) REFERENCES `FORMAT = (`format_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_MOVIE_4 = FOREIGN KEY (`filmstock_id`) REFERENCES `FILMSTOCK = (`filmstock_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_MOVIE_5 = FOREIGN KEY (`process_id`) REFERENCES `PROCESS = (`process_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog motion picture films (movies)';


# CREATE TABLE `NEGATIVEFORMAT_COMPAT = (
#   format_id = models.IntegerField(11) NOT NULL COMMENT 'ID of the film format',
#   negative_size_id = models.IntegerField(11) NOT NULL COMMENT 'ID of the negative size',
#   PRIMARY KEY (`format_id`,`negative_size_id`),
#   CONSTRAINT `format_id = FOREIGN KEY (`format_id`) REFERENCES `FORMAT = (`format_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `negative_size_id = FOREIGN KEY (`negative_size_id`) REFERENCES `NEGATIVE_SIZE = (`negative_size_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Table to record compatibility between film formats and negative sizes';


# CREATE TABLE `NEGATIVE_SIZE = (
#   negative_size_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of negative size',
#   width = decimal(4,1) 'Width of the negative size in mm',
#   height = decimal(4,1) 'Height of the negative size in mm',
#   negative_size = models.CharField(45) 'Common name of the negative size (e.g. 35mm, 6x7, etc)',
#   crop_factor = decimal(4,2) 'Crop factor of this negative size',
#   area = models.IntegerField(11) 'Area of this negative size in sq. mm',
#   aspect_ratio = decimal(4,2) 'Aspect ratio of this negative size, expressed as a single decimal. (e.g. 3:2 is expressed as 1.5)',
#   PRIMARY KEY (`negative_size_id`)
# ) 'Table to catalog different negative sizes available. Negtives sizes are distinct from film formats.';


# CREATE TABLE `NEGATIVE = (
#   negative_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this negative',
#   film_id = models.IntegerField(11) 'ID of the film that this negative belongs to',
#   frame = models.CharField(5) CHARACTER SET utf8mb4 'Frame number or code of this negative',
#   description = models.CharField(145) CHARACTER SET utf8mb4 'Caption of this picture',
#   date = datetime 'Date & time on which this picture was taken',
#   lens_id = models.IntegerField(11) 'ID of lens used to take this picture',
#   shutter_speed = models.CharField(45) CHARACTER SET latin1 'Shutter speed used to take this picture',
#   aperture = decimal(4,1) 'Aperture used to take this picture (numerical part only)',
#   filter_id = models.IntegerField(11) 'ID of filter used to take this picture',
#   teleconverter_id = models.IntegerField(11) 'ID of teleconverter used to take this picture',
#   notes = text CHARACTER SET utf8mb4 'Extra freeform notes about this exposure',
#   mount_adapter_id = models.IntegerField(11) 'ID of lens mount adapter used to take this pciture',
#   focal_length = models.IntegerField(11) 'If a zoom lens was used, specify the focal length of the lens',
#   latitude = decimal(9,6) 'Latitude of the location where the picture was taken',
#   longitude = decimal(9,6) 'Longitude of the location where the picture was taken',
#   flash = models.BooleanField('Whether flash was used',
#   metering_mode = models.IntegerField(11) 'MeteringMode ID as defined in EXIF spec',
#   exposure_program = models.IntegerField(11) 'ExposureProgram ID as defined in EXIF spec',
#   photographer_id = models.IntegerField(11) 'ID of person who took this photograph',
#   copy_of = models.IntegerField(11) 'Negative ID of negative from which this negative is reproduced/duplicated/rephotographed',
#   PRIMARY KEY (`negative_id`),
#   CONSTRAINT `fk_NEGATIVE_1 = FOREIGN KEY (`film_id`) REFERENCES `FILM = (`film_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_NEGATIVE_10 = FOREIGN KEY (`copy_of`) REFERENCES `NEGATIVE = (`negative_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_NEGATIVE_2 = FOREIGN KEY (`lens_id`) REFERENCES `LENS = (`lens_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_NEGATIVE_3 = FOREIGN KEY (`filter_id`) REFERENCES `FILTER = (`filter_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_NEGATIVE_4 = FOREIGN KEY (`teleconverter_id`) REFERENCES `TELECONVERTER = (`teleconverter_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_NEGATIVE_5 = FOREIGN KEY (`mount_adapter_id`) REFERENCES `MOUNT_ADAPTER = (`mount_adapter_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_NEGATIVE_6 = FOREIGN KEY (`metering_mode`) REFERENCES `METERING_MODE = (`metering_mode_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_NEGATIVE_7 = FOREIGN KEY (`exposure_program`) REFERENCES `EXPOSURE_PROGRAM = (`exposure_program_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_NEGATIVE_8 = FOREIGN KEY (`photographer_id`) REFERENCES `PERSON = (`person_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_NEGATIVE_9 = FOREIGN KEY (`shutter_speed`) REFERENCES `SHUTTER_SPEED = (`shutter_speed`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog negatives (which includes positives/slide too). Negatives are created by cameras, belong to films and can be used to create scans or prints.';


# CREATE TABLE `PAPER_STOCK = (
#   paper_stock_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this paper stock',
#   name = models.CharField(45) 'Name of this paper stock',
#   manufacturer_id = models.IntegerField(11) 'ID of the manufacturer of this paper stock',
#   resin_coated = models.BooleanField('Whether the paper is resin-coated',
#   tonable = models.BooleanField('Whether this paper accepts chemical toning',
#   colour = models.BooleanField('Whether this is a colour paper',
#   finish = models.CharField(45) 'The finish of the paper surface',
#   PRIMARY KEY (`paper_stock_id`),
#   CONSTRAINT `fk_PAPER_STOCK_1 = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) 'Table to catalog different paper stocks available';


# CREATE TABLE `PERSON = (
#   person_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for the person',
#   name = models.CharField(45) 'Name of the photographer',
#   PRIMARY KEY (`person_id`)
# ) 'Table to catalog photographers';


# CREATE TABLE `PRINT = (
#   print_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for the print',
#   negative_id = models.IntegerField(11) 'ID of the negative that this print was made from',
#   date = date 'The date that the print was made',
#   paper_stock_id = models.IntegerField(11) 'ID of the paper stock used',
#   height = decimal(4,1) 'Height of the print in inches',
#   width = decimal(4,1) 'Width of the print in inches',
#   aperture = decimal(3,1) 'Aperture used to make this print (numerical part only, e.g. 5.6)',
#   exposure_time = decimal(5,1) 'Exposure time of this print in seconds',
#   filtration_grade = decimal(2,1) 'Contrast grade of paper used',
#   development_time = models.IntegerField(11) 'Development time of this print in seconds',
#   bleach_time = time 'Duration of bleaching',
#   toner_id = models.IntegerField(11) 'ID of the first toner used to make this print',
#   toner_dilution = models.CharField(6) 'Dilution of the first toner used to make this print',
#   toner_time = time 'Duration of first toning',
#   2nd_toner_id = models.IntegerField(11) 'ID of the second toner used to make this print',
#   2nd_toner_dilution = models.CharField(6) 'Dilution of the second toner used to make this print',
#   2nd_toner_time = time 'Duration of second toning',
#   own = models.BooleanField('Whether we currently own this print',
#   location = models.CharField(45) 'The place where this print is currently',
#   sold_price = decimal(5,2) 'Sale price of the print',
#   enlarger_id = models.IntegerField(11) 'ID of the enlarger used to make this print',
#   lens_id = models.IntegerField(11) 'ID of the lens used to make this print',
#   developer_id = models.IntegerField(11) 'ID of the developer used to develop this print',
#   fine = models.BooleanField('Whether this is a fine print',
#   notes = text 'Freeform notes about this print, e.g. dodging, burning & complex toning',
#   archive_id = models.IntegerField(11) 'ID of the archive to which this print belongs',
#   printer_id = models.IntegerField(11) 'ID of the person who made this print',
#   PRIMARY KEY (`print_id`),
#   CONSTRAINT `fk_PRINT_1 = FOREIGN KEY (`paper_stock_id`) REFERENCES `PAPER_STOCK = (`paper_stock_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_PRINT_2 = FOREIGN KEY (`negative_id`) REFERENCES `NEGATIVE = (`negative_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_PRINT_3 = FOREIGN KEY (`toner_id`) REFERENCES `TONER = (`toner_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_PRINT_4 = FOREIGN KEY (`enlarger_id`) REFERENCES `ENLARGER = (`enlarger_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_PRINT_5 = FOREIGN KEY (`lens_id`) REFERENCES `LENS = (`lens_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_PRINT_6 = FOREIGN KEY (`developer_id`) REFERENCES `DEVELOPER = (`developer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_PRINT_7 = FOREIGN KEY (`archive_id`) REFERENCES `ARCHIVE = (`archive_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_PRINT_8 = FOREIGN KEY (`printer_id`) REFERENCES `PERSON = (`person_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog prints made from negatives';


# CREATE TABLE `PROCESS = (
#   process_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'ID of this development process',
#   name = models.CharField(12) 'Name of this developmenmt process (e.g. C-41, E-6)',
#   colour = models.BooleanField('Whether this is a colour process',
#   positive = models.BooleanField('Whether this is a positive/reversal process',
#   PRIMARY KEY (`process_id`)
# ) 'Table to catalog chemical processes that can be used to develop film and paper';


# CREATE TABLE `PROJECTOR = (
#   projector_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this projector',
#   manufacturer_id = models.IntegerField(11) 'ID of the manufacturer of this projector',
#   model = models.CharField(45) 'Model name of this projector',
#   mount_id = models.IntegerField(11) 'ID of the lens mount of this projector, if it has models.IntegerFielderchangeable lenses',
#   negative_size_id = models.IntegerField(11) 'ID of the largest negative size that this projector can handle',
#   own = models.BooleanField('Whether we currently own this projector',
#   cine = models.BooleanField('Whether this is a cine (movie) projector',
#   PRIMARY KEY (`projector_id`),
#   CONSTRAINT `fk_PROJECTOR_1 = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_PROJECTOR_2 = FOREIGN KEY (`mount_id`) REFERENCES `MOUNT = (`mount_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_PROJECTOR_3 = FOREIGN KEY (`negative_size_id`) REFERENCES `NEGATIVE_SIZE = (`negative_size_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalog projectors (still and movie)';


# CREATE TABLE `REPAIR = (
#   repair_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for the repair job',
#   camera_id = models.IntegerField(11) 'ID of camera that was repaired',
#   lens_id = models.IntegerField(11) 'ID of lens that was repaired',
#   date = date 'The date of the repair',
#   summary = models.CharField(100) 'Brief summary of the repair',
#   description = models.CharField(500) 'Longer description of the repair',
#   PRIMARY KEY (`repair_id`),
#   CONSTRAINT `fk_REPAIR_1 = FOREIGN KEY (`camera_id`) REFERENCES `CAMERA = (`camera_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_REPAIR_2 = FOREIGN KEY (`lens_id`) REFERENCES `LENS = (`lens_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Tabe to catalog all repairs and servicing undertaken on cameras and lenses in the collection';


# CREATE TABLE `SCAN = (
#   scan_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for this scan',
#   negative_id = models.IntegerField(11) 'ID of the negative that was scanned',
#   print_id = models.IntegerField(11) 'ID of the print  that was scanned',
#   filename = models.CharField(128) 'Filename of the scan',
#   date = date 'Date that this scan was made',
#   colour = models.BooleanField('Whether this is a colour image',
#   width = models.IntegerField(11) 'Width of the scanned image in pixels',
#   height = models.IntegerField(11) 'Height of the scanned image in pixels',
#   PRIMARY KEY (`scan_id`),
#   CONSTRAINT `fk_SCAN_1 = FOREIGN KEY (`negative_id`) REFERENCES `NEGATIVE = (`negative_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_SCAN_2 = FOREIGN KEY (`print_id`) REFERENCES `PRINT = (`print_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to record all the images that have been scanned digitally';


# CREATE TABLE `SERIES_MEMBER = (
#   series_member_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this series membership',
#   series_id = models.IntegerField(11) 'ID of the series to which this camera model or lens model belongs',
#   cameramodel_id = models.IntegerField(11) 'ID of the camera model',
#   lensmodel_id = models.IntegerField(11) 'ID of the lens model',
#   PRIMARY KEY (`series_member_id`),
#   CONSTRAINT `fk_SERIES_MEMBER_1 = FOREIGN KEY (`series_id`) REFERENCES `SERIES = (`series_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_SERIES_MEMBER_2 = FOREIGN KEY (`cameramodel_id`) REFERENCES `CAMERAMODEL = (`cameramodel_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#   CONSTRAINT `fk_SERIES_MEMBER_3 = FOREIGN KEY (`lensmodel_id`) REFERENCES `LENSMODEL = (`lensmodel_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to record which cameras and lenses belong to which series';


# CREATE TABLE `SERIES = (
#   series_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this series',
#   name = models.CharField(45) 'Name of this collection, e.g. Canon FD SLRs',
#   PRIMARY KEY (`series_id`)
# ) 'Table to list all series of cameras and lenses';


# CREATE TABLE `SHUTTER_SPEED_AVAILABLE = (
#   cameramodel_id = models.IntegerField(11) NOT NULL COMMENT 'ID of the camera model',
#   shutter_speed = models.CharField(10) CHARACTER SET latin1 NOT NULL COMMENT 'Shutter speed that this camera has',
#   bulb = models.IntegerField(1) DEFAULT 0 COMMENT 'Whether this is a manual "bulb" shutter speed that can only be accessed in B or T modes',
#   PRIMARY KEY (`cameramodel_id`,`shutter_speed`),
#   CONSTRAINT `fk_SHUTTER_SPEED_AVAILABLE_1 = FOREIGN KEY (`shutter_speed`) REFERENCES `SHUTTER_SPEED = (`shutter_speed`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_SHUTTER_SPEED_AVAILABLE_2 = FOREIGN KEY (`cameramodel_id`) REFERENCES `CAMERAMODEL = (`cameramodel_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) COMMENT='Table to associate cameras with shutter speeds';


# CREATE TABLE `SHUTTER_SPEED = (
#   shutter_speed = models.CharField(10) CHARACTER SET latin1 NOT NULL COMMENT 'Shutter speed in fractional notation, e.g. 1/250',
#   duration = decimal(9,5) 'Shutter speed in decimal notation, e.g. 0.04',
#   PRIMARY KEY (`shutter_speed`)
# ) COMMENT='Table to list all possible shutter speeds';


# CREATE TABLE `SHUTTER_TYPE = (
#   shutter_type_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of the shutter type',
#   shutter_type = models.CharField(45) 'Name of the shutter type (e.g. Focal plane, Leaf, etc)',
#   PRIMARY KEY (`shutter_type_id`)
# ) 'Table to catalog the different types of camera shutter';


# CREATE TABLE `TELECONVERTER = (
#   teleconverter_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this teleconverter',
#   mount_id = models.IntegerField(11) 'ID of the lens mount used by this teleconverter',
#   factor = decimal(4,2) 'Magnification factor of this teleconverter (numerical part only, e.g. 1.4)',
#   manufacturer_id = models.IntegerField(11) 'ID of the manufacturer of this teleconverter',
#   model = models.CharField(45) 'Model name of this teleconverter',
#   elements = tinyint(4) 'Number of optical elements used in this teleconverter',
#   groups = tinyint(4) 'Number of optical groups used in this teleconverter',
#   multicoated = models.BooleanField('Whether this teleconverter is multi-coated',
#   PRIMARY KEY (`teleconverter_id`),
#   CONSTRAINT `fk_TELECONVERTER_1 = FOREIGN KEY (`manufacturer_id`) REFERENCES `MANUFACTURER = (`manufacturer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `fk_TELECONVERTER_2 = FOREIGN KEY (`mount_id`) REFERENCES `MOUNT = (`mount_id`) ON DELETE CASCADE ON UPDATE CASCADE
# ) 'Table to catalog teleconverters (multipliers)';


# CREATE TABLE `TONER = (
#   toner_id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of the toner',
#   manufacturer_id = models.IntegerField(11) 'ID of the manufacturer of the toner',
#   toner = models.CharField(45) 'Name of the toner',
#   formulation = models.CharField(45) 'Chemical formulation of the toner',
#   stock_dilution = models.CharField(10) 'Stock dilution of the toner',
#   PRIMARY KEY (`toner_id`)
# ) 'Table to catalog paper toners that can be used during the printing process';


# CREATE TABLE `TO_PRINT = (
#   id = models.IntegerField(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID of this table',
#   negative_id = models.IntegerField(11) 'Negative ID to be printed',
#   width = models.IntegerField(11) 'Width of print to be made',
#   height = models.IntegerField(11) 'Height of print to be made',
#   printed = tinyint(1) DEFAULT 0 COMMENT 'Whether the print has been made',
#   print_id = models.IntegerField(11) 'ID of print made',
#   recipient = models.CharField(45) 'Recipient of the print',
#   added = date 'Date that record was added',
#   PRIMARY KEY (`id`),
#   CONSTRAINT `fk_TO_PRINT_1 = FOREIGN KEY (`negative_id`) REFERENCES `NEGATIVE = (`negative_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) 'Table to catalogue negatives that should be printed';
