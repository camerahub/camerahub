from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('accessory/', views.AccessoryList.as_view(), name='accessory-list'),
  path('accessory/<int:pk>', views.AccessoryDetail.as_view(), name='accessory-detail'),

  path('archive/', views.ArchiveList.as_view(), name='archive-list'),
  path('archive/<int:pk>', views.ArchiveDetail.as_view(), name='archive-detail'),
  
  path('battery/', views.BatteryList.as_view(), name='battery-list'),
  path('battery/<int:pk>', views.BatteryDetail.as_view(), name='battery-detail'),
  
  path('bulkfilm/', views.BulkFilmList.as_view(), name='bulkfilm-list'),
  path('bulkfilm/<int:pk>', views.BulkFilmDetail.as_view(), name='bulkfilm-detail'),
  
  path('camera/', views.CameraList.as_view(), name='camera-list'),
  path('camera/<int:pk>', views.CameraDetail.as_view(), name='camera-detail'),
  path('camera/create/', views.CameraCreate.as_view(), name='camera-create'),
  path('camera/<int:pk>/update', views.CameraUpdate.as_view(), name='camera-update'),
  
  path('cameramodel/', views.CameraModelList.as_view(), name='cameramodel-list'),
  path('cameramodel/<int:pk>', views.CameraModelDetail.as_view(), name='cameramodel-detail'),
  
  path('developer/', views.DeveloperList.as_view(), name='developer-list'),
  path('developer/<int:pk>', views.DeveloperDetail.as_view(), name='developer-detail'),
  
  path('enlarger/', views.EnlargerList.as_view(), name='enlarger-list'),
  path('enlarger/<int:pk>', views.EnlargerDetail.as_view(), name='enlarger-detail'),
  
  path('filmstock/', views.FilmStockList.as_view(), name='filmstock-list'),
  path('filmstock/<int:pk>', views.FilmStockDetail.as_view(), name='filmstock-detail'),
  
  path('filter/', views.FilterList.as_view(), name='filter-list'),
  path('filter/<int:pk>', views.FilterDetail.as_view(), name='filter-detail'),
  
  path('flash/', views.FlashList.as_view(), name='flash-list'),
  path('flash/<int:pk>', views.FlashDetail.as_view(), name='flash-detail'),
  
  path('flashprotocol/', views.FlashProtocolList.as_view(), name='flashprotocol-list'),
  path('flashprotocol/<int:pk>', views.FlashProtocolDetail.as_view(), name='flashprotocol-detail'),
  
  path('format/', views.FormatList.as_view(), name='format-list'),
  path('format/<int:pk>', views.FormatDetail.as_view(), name='format-detail'),
  
  path('lens/', views.LensList.as_view(), name='lens-list'),
  path('lens/<int:pk>', views.LensDetail.as_view(), name='lens-detail'),
  
  path('lensmodel/', views.LensModelList.as_view(), name='lensmodel-list'),
  path('lensmodel/<int:pk>', views.LensModelDetail.as_view(), name='lensmodel-detail'),
  
  path('manufacturer/', views.ManufacturerList.as_view(), name='manufacturer-list'),
  path('manufacturer/<int:pk>', views.ManufacturerDetail.as_view(), name='manufacturer-detail'),
  
  path('meteringtype/', views.MeteringTypeList.as_view(), name='meteringtype-list'),
  path('meteringtype/<int:pk>', views.MeteringTypeDetail.as_view(), name='meteringtype-detail'),
  
  path('mount/', views.MountList.as_view(), name='mount-list'),
  path('mount/<int:pk>', views.MountDetail.as_view(), name='mount-detail'),
  
  path('mountadapter/', views.MountAdapterList.as_view(), name='mountadapter-list'),
  path('mountadapter/<int:pk>', views.MountAdapterDetail.as_view(), name='mountadapter-detail'),
  
  path('negativesize/', views.NegativeSizeList.as_view(), name='negativesize-list'),
  path('negativesize/<int:pk>', views.NegativeSizeDetail.as_view(), name='negativesize-detail'),
  
  path('order/', views.OrderList.as_view(), name='order-list'),
  path('order/<int:pk>', views.OrderDetail.as_view(), name='order-detail'),
  
  path('paperstock/', views.PaperStockList.as_view(), name='paperstock-list'),
  path('paperstock/<int:pk>', views.PaperStockDetail.as_view(), name='paperstock-detail'),
  
  path('person/', views.PersonList.as_view(), name='person-list'),
  path('person/<int:pk>', views.PersonDetail.as_view(), name='person-detail'),
  
  path('print/', views.PrintList.as_view(), name='print-list'),
  path('print/<int:pk>', views.PrintDetail.as_view(), name='print-detail'),
  
  path('process/', views.ProcessList.as_view(), name='process-list'),
  path('process/<int:pk>', views.ProcessDetail.as_view(), name='process-detail'),
  
  path('repair/', views.RepairList.as_view(), name='repair-list'),
  path('repair/<int:pk>', views.RepairDetail.as_view(), name='repair-detail'),
  
  path('scan/', views.ScanList.as_view(), name='scan-list'),
  path('scan/<int:pk>', views.ScanDetail.as_view(), name='scan-detail'),
  
  path('negative/', views.NegativeList.as_view(), name='negative-list'),
  path('negative/<int:pk>', views.NegativeDetail.as_view(), name='negative-detail'),
  
  path('film/', views.FilmList.as_view(), name='film-list'),
  path('film/<int:pk>', views.FilmDetail.as_view(), name='film-detail'),
  
  path('series/', views.SeriesList.as_view(), name='series-list'),
  path('series/<int:pk>', views.SeriesDetail.as_view(), name='series-detail'),
  
  path('teleconverter/', views.TeleconverterList.as_view(), name='teleconverter-list'),
  path('teleconverter/<int:pk>', views.TeleconverterDetail.as_view(), name='teleconverter-detail'),
  
  path('toner/', views.TonerList.as_view(), name='toner-list'),
  path('toner/<int:pk>', views.TonerDetail.as_view(), name='toner-detail'),
]