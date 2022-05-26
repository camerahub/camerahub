from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from schema import views

app_name = 'schema'
urlpatterns = [

    # Static pages
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('stats', views.StatsView.as_view(), name='stats'),
    path('mystats', views.MyStatsView.as_view(), name='mystats'),
    path('search/', views.SearchView.as_view(), name='search'),

    path('accessory/', views.AccessoryList.as_view(), name='accessory-list'),
    path('accessory/<int:id_owner>', views.AccessoryDetail.as_view(),
         name='accessory-detail'),
    path('accessory/create/', views.AccessoryCreate.as_view(),
         name='accessory-create'),
    path('accessory/<int:id_owner>/update',
         views.AccessoryUpdate.as_view(), name='accessory-update'),

    path('archive/', views.ArchiveList.as_view(), name='archive-list'),
    path('archive/<int:id_owner>',
         views.ArchiveDetail.as_view(), name='archive-detail'),
    path('archive/create/', views.ArchiveCreate.as_view(), name='archive-create'),
    path('archive/<int:id_owner>/print',
         views.ArchivePrint.as_view(), name='archive-print'),
    path('archive/<int:id_owner>/update',
         views.ArchiveUpdate.as_view(), name='archive-update'),

    path('battery/', views.BatteryList.as_view(), name='battery-list'),
    path('battery/<slug:slug>', views.BatteryDetail.as_view(), name='battery-detail'),
    path('battery/create/', views.BatteryCreate.as_view(), name='battery-create'),
    path('battery/<slug:slug>/update',
         views.BatteryUpdate.as_view(), name='battery-update'),

    path('bulkfilm/', views.BulkFilmList.as_view(), name='bulkfilm-list'),
    path('bulkfilm/<int:id_owner>',
         views.BulkFilmDetail.as_view(), name='bulkfilm-detail'),
    path('bulkfilm/create/', views.BulkFilmCreate.as_view(), name='bulkfilm-create'),
    path('bulkfilm/<int:id_owner>/update',
         views.BulkFilmUpdate.as_view(), name='bulkfilm-update'),

    path('camera/', views.CameraList.as_view(), name='camera-list'),
    path('camera/<int:id_owner>', views.CameraDetail.as_view(), name='camera-detail'),
    path('camera/create/', views.CameraCreate.as_view(), name='camera-create'),
    path('camera/<int:id_owner>/update',
         views.CameraUpdate.as_view(), name='camera-update'),
    path('camera/<int:id_owner>/sell',
         views.CameraSell.as_view(), name='camera-sell'),

    path('cameramodel/', views.CameraModelList.as_view(), name='cameramodel-list'),
    path('cameramodel/<slug:slug>', views.CameraModelDetail.as_view(),
         name='cameramodel-detail'),
    path('cameramodel/create/', views.CameraModelCreate.as_view(),
         name='cameramodel-create'),
    path('cameramodel/<slug:slug>/update',
         views.CameraModelUpdate.as_view(), name='cameramodel-update'),

    path('developer/', views.DeveloperList.as_view(), name='developer-list'),
    path('developer/<slug:slug>', views.DeveloperDetail.as_view(),
         name='developer-detail'),
    path('developer/create/', views.DeveloperCreate.as_view(),
         name='developer-create'),
    path('developer/<slug:slug>/update',
         views.DeveloperUpdate.as_view(), name='developer-update'),

    path('enlargermodel/', views.EnlargerModelList.as_view(),
         name='enlargermodel-list'),
    path('enlargermodel/<slug:slug>', views.EnlargerModelDetail.as_view(),
         name='enlargermodel-detail'),
    path('enlargermodel/create/', views.EnlargerModelCreate.as_view(),
         name='enlargermodel-create'),
    path('enlargermodel/<slug:slug>/update',
         views.EnlargerModelUpdate.as_view(), name='enlargermodel-update'),

    path('enlarger/', views.EnlargerList.as_view(), name='enlarger-list'),
    path('enlarger/<int:id_owner>',
         views.EnlargerDetail.as_view(), name='enlarger-detail'),
    path('enlarger/create/', views.EnlargerCreate.as_view(), name='enlarger-create'),
    path('enlarger/<int:id_owner>/update',
         views.EnlargerUpdate.as_view(), name='enlarger-update'),

    path('filmstock/', views.FilmStockList.as_view(), name='filmstock-list'),
    path('filmstock/<slug:slug>', views.FilmStockDetail.as_view(),
         name='filmstock-detail'),
    path('filmstock/create/', views.FilmStockCreate.as_view(),
         name='filmstock-create'),
    path('filmstock/<slug:slug>/update',
         views.FilmStockUpdate.as_view(), name='filmstock-update'),

    path('filter/', views.FilterList.as_view(), name='filter-list'),
    path('filter/<int:pk>', views.FilterDetail.as_view(), name='filter-detail'),
    path('filter/create/', views.FilterCreate.as_view(), name='filter-create'),
    path('filter/<int:pk>/update',
         views.FilterUpdate.as_view(), name='filter-update'),

    path('flash/', views.FlashList.as_view(), name='flash-list'),
    path('flash/<int:id_owner>', views.FlashDetail.as_view(), name='flash-detail'),
    path('flash/create/', views.FlashCreate.as_view(), name='flash-create'),
    path('flash/<int:id_owner>/update',
         views.FlashUpdate.as_view(), name='flash-update'),

    path('flashmodel/', views.FlashModelList.as_view(), name='flashmodel-list'),
    path('flashmodel/<slug:slug>', views.FlashModelDetail.as_view(),
         name='flashmodel-detail'),
    path('flashmodel/create/', views.FlashModelCreate.as_view(),
         name='flashmodel-create'),
    path('flashmodel/<slug:slug>/update',
         views.FlashModelUpdate.as_view(), name='flashmodel-update'),

    path('format/', views.FormatList.as_view(), name='format-list'),
    path('format/<int:pk>', views.FormatDetail.as_view(), name='format-detail'),
    path('format/create/', views.FormatCreate.as_view(), name='format-create'),
    path('format/<int:pk>/update',
         views.FormatUpdate.as_view(), name='format-update'),

    path('lens/', views.LensList.as_view(), name='lens-list'),
    path('lens/<int:id_owner>', views.LensDetail.as_view(), name='lens-detail'),
    path('lens/create/', views.LensCreate.as_view(), name='lens-create'),
    path('lens/<int:id_owner>/update',
         views.LensUpdate.as_view(), name='lens-update'),
    path('lens/<int:id_owner>/sell', views.LensSell.as_view(), name='lens-sell'),

    path('lensmodel/', views.LensModelList.as_view(), name='lensmodel-list'),
    path('lensmodel/<slug:slug>', views.LensModelDetail.as_view(),
         name='lensmodel-detail'),
    path('lensmodel/create/', views.LensModelCreate.as_view(),
         name='lensmodel-create'),
    path('lensmodel/<slug:slug>/update',
         views.LensModelUpdate.as_view(), name='lensmodel-update'),

    path('manufacturer/', views.ManufacturerList.as_view(),
         name='manufacturer-list'),
    path('manufacturer/<slug:slug>', views.ManufacturerDetail.as_view(),
         name='manufacturer-detail'),
    path('manufacturer/create/', views.ManufacturerCreate.as_view(),
         name='manufacturer-create'),
    path('manufacturer/<slug:slug>/update',
         views.ManufacturerUpdate.as_view(), name='manufacturer-update'),

    path('mount/', views.MountList.as_view(), name='mount-list'),
    path('mount/<slug:slug>', views.MountDetail.as_view(), name='mount-detail'),
    path('mount/create/', views.MountCreate.as_view(), name='mount-create'),
    path('mount/<slug:slug>/update',
         views.MountUpdate.as_view(), name='mount-update'),

    path('mountadapter/', views.MountAdapterList.as_view(),
         name='mountadapter-list'),
    path('mountadapter/<int:id_owner>', views.MountAdapterDetail.as_view(),
         name='mountadapter-detail'),
    path('mountadapter/create/', views.MountAdapterCreate.as_view(),
         name='mountadapter-create'),
    path('mountadapter/<int:id_owner>/update',
         views.MountAdapterUpdate.as_view(), name='mountadapter-update'),

    path('negativesize/', views.NegativeSizeList.as_view(),
         name='negativesize-list'),
    path('negativesize/<int:pk>', views.NegativeSizeDetail.as_view(),
         name='negativesize-detail'),
    path('negativesize/create/', views.NegativeSizeCreate.as_view(),
         name='negativesize-create'),
    path('negativesize/<int:pk>/update',
         views.NegativeSizeUpdate.as_view(), name='negativesize-update'),

    path('order/', views.OrderList.as_view(), name='order-list'),
    path('order/<int:id_owner>', views.OrderDetail.as_view(), name='order-detail'),
    path('order/create/', views.OrderCreate.as_view(), name='order-create'),
    path('order/<int:id_owner>/update',
         views.OrderUpdate.as_view(), name='order-update'),

    path('paperstock/', views.PaperStockList.as_view(), name='paperstock-list'),
    path('paperstock/<int:pk>', views.PaperStockDetail.as_view(),
         name='paperstock-detail'),
    path('paperstock/create/', views.PaperStockCreate.as_view(),
         name='paperstock-create'),
    path('paperstock/<int:pk>/update',
         views.PaperStockUpdate.as_view(), name='paperstock-update'),

    path('person/', views.PersonList.as_view(), name='person-list'),
    path('person/<int:id_owner>', views.PersonDetail.as_view(), name='person-detail'),
    path('person/create/', views.PersonCreate.as_view(), name='person-create'),
    path('person/<int:id_owner>/update',
         views.PersonUpdate.as_view(), name='person-update'),

    path('print/', views.PrintList.as_view(), name='print-list'),
    path('print/<int:id_owner>', views.PrintDetail.as_view(), name='print-detail'),
    path('print/<int:id_owner>/print',
         views.PrintPrint.as_view(), name='print-print'),
    path('print/create/', views.PrintCreate.as_view(), name='print-create'),
    path('print/<int:id_owner>/update',
         views.PrintUpdate.as_view(), name='print-update'),
    path('print/<int:id_owner>/archive',
         views.PrintArchive.as_view(), name='print-archive'),

    path('process/', views.ProcessList.as_view(), name='process-list'),
    path('process/<int:pk>', views.ProcessDetail.as_view(), name='process-detail'),
    path('process/create/', views.ProcessCreate.as_view(), name='process-create'),
    path('process/<int:pk>/update',
         views.ProcessUpdate.as_view(), name='process-update'),

    path('scan/', views.ScanList.as_view(), name='scan-list'),
    path('scan/<uuid:uuid>', views.ScanDetail.as_view(), name='scan-detail'),
    path('scan/create/', views.ScanCreate.as_view(), name='scan-create'),
    path('scan/<uuid:uuid>/update',
         views.ScanUpdate.as_view(), name='scan-update'),

    path('negative/', views.NegativeList.as_view(), name='negative-list'),
    path('negative/<str:slug>',
         views.NegativeDetail.as_view(), name='negative-detail'),
    path('negative/create/', views.NegativeCreate.as_view(), name='negative-create'),
    path('negative/<str:slug>/update',
         views.NegativeUpdate.as_view(), name='negative-update'),

    path('film/', views.FilmList.as_view(), name='film-list'),
    path('film/<int:id_owner>', views.FilmDetail.as_view(), name='film-detail'),
    path('film/create/', views.FilmCreate.as_view(), name='film-create'),
    path('film/<int:id_owner>/update',
         views.FilmUpdate.as_view(), name='film-update'),
    path('film/<int:id_owner>/print',
         views.FilmPrint.as_view(), name='film-print'),
    path('film/<int:id_owner>/load', views.FilmLoad.as_view(), name='film-load'),
    path('film/<int:id_owner>/develop',
         views.FilmDevelop.as_view(), name='film-develop'),
    path('film/<int:id_owner>/archive',
         views.FilmArchive.as_view(), name='film-archive'),

    path('teleconverter/', views.TeleconverterList.as_view(),
         name='teleconverter-list'),
    path('teleconverter/<int:id_owner>',
         views.TeleconverterDetail.as_view(), name='teleconverter-detail'),
    path('teleconverter/create/', views.TeleconverterCreate.as_view(),
         name='teleconverter-create'),
    path('teleconverter/<int:id_owner>/update',
         views.TeleconverterUpdate.as_view(), name='teleconverter-update'),

    path('teleconvertermodel/', views.TeleconverterModelList.as_view(),
         name='teleconvertermodel-list'),
    path('teleconvertermodel/<slug:slug>',
         views.TeleconverterModelDetail.as_view(), name='teleconvertermodel-detail'),
    path('teleconvertermodel/create/', views.TeleconverterModelCreate.as_view(),
         name='teleconvertermodel-create'),
    path('teleconvertermodel/<slug:slug>/update',
         views.TeleconverterModelUpdate.as_view(), name='teleconvertermodel-update'),

    path('toner/', views.TonerList.as_view(), name='toner-list'),
    path('toner/<slug:slug>', views.TonerDetail.as_view(), name='toner-detail'),
    path('toner/create/', views.TonerCreate.as_view(), name='toner-create'),
    path('toner/<slug:slug>/update',
         views.TonerUpdate.as_view(), name='toner-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
