from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from schema import views

app_name = 'schema'
urlpatterns = [

    # Static pages
    path('', views.IndexView.as_view(), name='index'),
    path('stats', views.StatsView.as_view(), name='stats'),
    path('mystats', views.MyStatsView.as_view(), name='mystats'),
    path('search/', views.SearchView.as_view(), name='search'),

        path('tag/<slug:slug>', views.TagDetail.as_view(), name='tag-detail'),

    path('accessory/<int:id_owner>', views.AccessoryDetail.as_view(),
         name='accessory-detail'),

    path('archive/<int:id_owner>',
         views.ArchiveDetail.as_view(), name='archive-detail'),
    path('archive/<int:id_owner>/print',
         views.ArchivePrint.as_view(), name='archive-print'),

    path('battery/<slug:slug>', views.BatteryDetail.as_view(), name='battery-detail'),

    path('bulkfilm/<int:id_owner>',
         views.BulkFilmDetail.as_view(), name='bulkfilm-detail'),

    path('camera/<int:id_owner>', views.CameraDetail.as_view(), name='camera-detail'),
    path('camera/<int:id_owner>/sell',
         views.CameraSell.as_view(), name='camera-sell'),

    path('cameramodel/<slug:slug>', views.CameraModelDetail.as_view(),
         name='cameramodel-detail'),

    path('developer/<slug:slug>', views.DeveloperDetail.as_view(),
         name='developer-detail'),

    path('enlargermodel/<slug:slug>', views.EnlargerModelDetail.as_view(),
         name='enlargermodel-detail'),

    path('enlarger/<int:id_owner>',
         views.EnlargerDetail.as_view(), name='enlarger-detail'),

    path('filmstock/<slug:slug>', views.FilmStockDetail.as_view(),
         name='filmstock-detail'),

    path('filter/<int:pk>', views.FilterDetail.as_view(), name='filter-detail'),

    path('flash/<int:id_owner>', views.FlashDetail.as_view(), name='flash-detail'),

    path('flashmodel/<slug:slug>', views.FlashModelDetail.as_view(),
         name='flashmodel-detail'),

    path('format/<int:pk>', views.FormatDetail.as_view(), name='format-detail'),

    path('lens/<int:id_owner>', views.LensDetail.as_view(), name='lens-detail'),
    path('lens/<int:id_owner>/sell', views.LensSell.as_view(), name='lens-sell'),

    path('lensmodel/<slug:slug>', views.LensModelDetail.as_view(),
         name='lensmodel-detail'),

    path('manufacturer/<slug:slug>', views.ManufacturerDetail.as_view(),
         name='manufacturer-detail'),

    path('mount/<slug:slug>', views.MountDetail.as_view(), name='mount-detail'),

    path('mountadapter/<int:id_owner>', views.MountAdapterDetail.as_view(),
         name='mountadapter-detail'),

    path('negativesize/<int:pk>', views.NegativeSizeDetail.as_view(),
         name='negativesize-detail'),

    path('paperstock/<int:pk>', views.PaperStockDetail.as_view(),
         name='paperstock-detail'),

    path('person/<int:id_owner>', views.PersonDetail.as_view(), name='person-detail'),

    path('print/<int:id_owner>', views.PrintDetail.as_view(), name='print-detail'),
    path('print/<int:id_owner>/print',
         views.PrintPrint.as_view(), name='print-print'),
    path('print/<int:id_owner>/archive',
         views.PrintArchive.as_view(), name='print-archive'),
    path('print/<int:id_owner>/sell',
         views.PrintSell.as_view(), name='print-sell'),

    path('process/<int:pk>', views.ProcessDetail.as_view(), name='process-detail'),

    path('scan/<uuid:uuid>', views.ScanDetail.as_view(), name='scan-detail'),

    path('negative/<str:slug>',
         views.NegativeDetail.as_view(), name='negative-detail'),

    path('film/<int:id_owner>', views.FilmDetail.as_view(), name='film-detail'),
    path('film/<int:id_owner>/print',
         views.FilmPrint.as_view(), name='film-print'),
    path('film/<int:id_owner>/load', views.FilmLoad.as_view(), name='film-load'),
    path('film/<int:id_owner>/develop',
         views.FilmDevelop.as_view(), name='film-develop'),
    path('film/<int:id_owner>/archive',
         views.FilmArchive.as_view(), name='film-archive'),

    path('teleconverter/<int:id_owner>',
         views.TeleconverterDetail.as_view(), name='teleconverter-detail'),
    path('teleconvertermodel/<slug:slug>',
         views.TeleconverterModelDetail.as_view(), name='teleconvertermodel-detail'),

    path('toner/<slug:slug>', views.TonerDetail.as_view(), name='toner-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
