from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from schema.models import Process, Scan, Negative, Film, ShutterSpeed, Teleconverter, TeleconverterModel, Toner
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print
from schema.models import Flash, FlashModel, Format, Lens, LensModel, Manufacturer
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock, Filter

# The text to put at the top of each admin page, as an <h1> (a string). By default, this is “Django administration”.
admin.site.site_header = 'CameraHub'

# The text to put at the end of each admin page’s <title> (a string). By default, this is “Django site admin”.
admin.site.site_title = 'CameraHub admin'

# The text to put at the top of the admin index page (a string). By default, this is “Site administration”.
admin.site.index_title = 'CameraHub admin'

# The URL for the “View site” link at the top of each admin page. By default, site_url is /. Set it to None to remove the link.
#admin.site.site_url = None

# Now register the admin pages, customising where necessary
admin.site.register(Accessory)
admin.site.register(Archive)
admin.site.register(Battery, SimpleHistoryAdmin)
admin.site.register(BulkFilm)
admin.site.register(Camera)
admin.site.register(CameraModel)
admin.site.register(Developer, SimpleHistoryAdmin)
admin.site.register(EnlargerModel, SimpleHistoryAdmin)
admin.site.register(Enlarger)
admin.site.register(FilmStock, SimpleHistoryAdmin)
admin.site.register(Filter)
admin.site.register(FlashModel, SimpleHistoryAdmin)
admin.site.register(Flash)
admin.site.register(Format, SimpleHistoryAdmin)
admin.site.register(Lens)
admin.site.register(LensModel, SimpleHistoryAdmin)
admin.site.register(Manufacturer, SimpleHistoryAdmin)
admin.site.register(Mount, SimpleHistoryAdmin)
admin.site.register(MountAdapter)
admin.site.register(NegativeSize, SimpleHistoryAdmin)
admin.site.register(Order)
admin.site.register(PaperStock, SimpleHistoryAdmin)
admin.site.register(Person)
admin.site.register(Print)
admin.site.register(Process)
admin.site.register(Scan)
admin.site.register(Negative)
admin.site.register(Film)
admin.site.register(ShutterSpeed)
admin.site.register(Teleconverter)
admin.site.register(TeleconverterModel, SimpleHistoryAdmin)
admin.site.register(Toner, SimpleHistoryAdmin)

#admin.site.register(Condition)
#admin.site.register(ExposureProgram)
#admin.site.register(MeteringMode)
#admin.site.register(Toning)
