from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register(r'manufacturer', views.ManufacturerViewSet, 'Manufacturer')
router.register(r'archive', views.ArchiveViewSet, 'Archive')
router.register(r'battery', views.BatteryViewSet, 'Battery')
router.register(r'condition', views.ConditionViewSet, 'Condition')
router.register(r'exposureprogram', views.ExposureProgramViewSet, 'ExposureProgram')
router.register(r'filter', views.FilterViewSet, 'Filter')
router.register(r'negativesize', views.NegativeSizeViewSet, 'NegativeSize')
router.register(r'format', views.FormatViewSet, 'Format')
router.register(r'flashmodel', views.FlashModelViewSet, 'FlashModel')
router.register(r'flash', views.FlashViewSet, 'Flash')
router.register(r'enlargermodel', views.EnlargerModelViewSet, 'EnlargerModel')
router.register(r'enlarger', views.EnlargerViewSet, 'Enlarger')
router.register(r'meteringmode', views.MeteringModeViewSet, 'MeteringMode')
router.register(r'mount', views.MountViewSet, 'Mount')
router.register(r'paperstock', views.PaperStockViewSet, 'PaperStock')
router.register(r'person', views.PersonViewSet, 'Person')
router.register(r'process', views.ProcessViewSet, 'Process')
router.register(r'teleconvertermodel', views.TeleconverterModelViewSet, 'TeleconverterModel')
router.register(r'teleconverter', views.TeleconverterViewSet, 'Teleconverter')
router.register(r'toner', views.TonerViewSet, 'Toner')
router.register(r'filmstock', views.FilmStockViewSet, 'FilmStock')
router.register(r'bulkfilm', views.BulkFilmViewSet, 'BulkFilm')
router.register(r'mountadapter', views.MountAdapterViewSet, 'MountAdapter')
router.register(r'shutterspeed', views.ShutterSpeedViewSet, 'ShutterSpeed')
router.register(r'developer', views.DeveloperViewSet, 'Developer')
router.register(r'lensmodel', views.LensModelViewSet, 'LensModel')
router.register(r'cameramodel', views.CameraModelViewSet, 'CameraModel')
router.register(r'accessory', views.AccessoryViewSet, 'Accessory')
router.register(r'lens', views.LensViewSet, 'Lens')
router.register(r'camera', views.CameraViewSet, 'Camera')
router.register(r'film', views.FilmViewSet, 'Film')
router.register(r'negative', views.NegativeViewSet, 'Negative')
router.register(r'print', views.PrintViewSet, 'Print')
router.register(r'toning', views.ToningViewSet, 'Toning')
router.register(r'scan', views.ScanViewSet, 'Scan')
router.register(r'order', views.OrderViewSet, 'Order')

urlpatterns = [
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
