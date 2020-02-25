from django.urls import path
from django.views.generic import TemplateView

from schema import views

urlpatterns = [

  # Static pages
  path('', TemplateView.as_view(template_name='schema/index.html'), name='index'),
  path('about', TemplateView.as_view(template_name='schema/about.html'), name='about'),
  path('stats', views.StatsView.as_view(), name='stats'),

  path('accessory/', views.AccessoryList.as_view(), name='accessory-list'),
  path('accessory/<int:pk>', views.AccessoryDetail.as_view(), name='accessory-detail'),
  path('accessory/create/', views.AccessoryCreate.as_view(), name='accessory-create'),
  path('accessory/<int:pk>/update', views.AccessoryUpdate.as_view(), name='accessory-update'),

  path('archive/', views.ArchiveList.as_view(), name='archive-list'),
  path('archive/<int:pk>', views.ArchiveDetail.as_view(), name='archive-detail'),
  path('archive/create/', views.ArchiveCreate.as_view(), name='archive-create'),
  path('archive/<int:pk>/update', views.ArchiveUpdate.as_view(), name='archive-update'),
  
  path('battery/', views.BatteryList.as_view(), name='battery-list'),
  path('battery/<int:pk>', views.BatteryDetail.as_view(), name='battery-detail'),
  path('battery/create/', views.BatteryCreate.as_view(), name='battery-create'),
  path('battery/<int:pk>/update', views.BatteryUpdate.as_view(), name='battery-update'),
  
  path('bulkfilm/', views.BulkFilmList.as_view(), name='bulkfilm-list'),
  path('bulkfilm/<int:pk>', views.BulkFilmDetail.as_view(), name='bulkfilm-detail'),
  path('bulkfilm/create/', views.BulkFilmCreate.as_view(), name='bulkfilm-create'),
  path('bulkfilm/<int:pk>/update', views.BulkFilmUpdate.as_view(), name='bulkfilm-update'),
  
  path('camera/', views.CameraList.as_view(), name='camera-list'),
  path('camera/<int:pk>', views.CameraDetail.as_view(), name='camera-detail'),
  path('camera/create/', views.CameraCreate.as_view(), name='camera-create'),
  path('camera/<int:pk>/update', views.CameraUpdate.as_view(), name='camera-update'),
  
  path('cameramodel/', views.CameraModelList.as_view(), name='cameramodel-list'),
  path('cameramodel/<int:pk>', views.CameraModelDetail.as_view(), name='cameramodel-detail'),
  path('cameramodel/create/', views.CameraModelCreate.as_view(), name='cameramodel-create'),
  path('cameramodel/<int:pk>/update', views.CameraModelUpdate.as_view(), name='cameramodel-update'),
  
  path('developer/', views.DeveloperList.as_view(), name='developer-list'),
  path('developer/<int:pk>', views.DeveloperDetail.as_view(), name='developer-detail'),
  path('developer/create/', views.DeveloperCreate.as_view(), name='developer-create'),
  path('developer/<int:pk>/update', views.DeveloperUpdate.as_view(), name='developer-update'),
  
  path('enlarger/', views.EnlargerList.as_view(), name='enlarger-list'),
  path('enlarger/<int:pk>', views.EnlargerDetail.as_view(), name='enlarger-detail'),
  path('enlarger/create/', views.EnlargerCreate.as_view(), name='enlarger-create'),
  path('enlarger/<int:pk>/update', views.EnlargerUpdate.as_view(), name='enlarger-update'),
  
  path('filmstock/', views.FilmStockList.as_view(), name='filmstock-list'),
  path('filmstock/<int:pk>', views.FilmStockDetail.as_view(), name='filmstock-detail'),
  path('filmstock/create/', views.FilmStockCreate.as_view(), name='filmstock-create'),
  path('filmstock/<int:pk>/update', views.FilmStockUpdate.as_view(), name='filmstock-update'),
  
  path('filter/', views.FilterList.as_view(), name='filter-list'),
  path('filter/<int:pk>', views.FilterDetail.as_view(), name='filter-detail'),
  path('filter/create/', views.FilterCreate.as_view(), name='filter-create'),
  path('filter/<int:pk>/update', views.FilterUpdate.as_view(), name='filter-update'),
  
  path('flash/', views.FlashList.as_view(), name='flash-list'),
  path('flash/<int:pk>', views.FlashDetail.as_view(), name='flash-detail'),
  path('flash/create/', views.FlashCreate.as_view(), name='flash-create'),
  path('flash/<int:pk>/update', views.FlashUpdate.as_view(), name='flash-update'),
  
  path('flashprotocol/', views.FlashProtocolList.as_view(), name='flashprotocol-list'),
  path('flashprotocol/<int:pk>', views.FlashProtocolDetail.as_view(), name='flashprotocol-detail'),
  path('flashprotocol/create/', views.FlashProtocolCreate.as_view(), name='flashprotocol-create'),
  path('flashprotocol/<int:pk>/update', views.FlashProtocolUpdate.as_view(), name='flashprotocol-update'),
  
  path('format/', views.FormatList.as_view(), name='format-list'),
  path('format/<int:pk>', views.FormatDetail.as_view(), name='format-detail'),
  path('format/create/', views.FormatCreate.as_view(), name='format-create'),
  path('format/<int:pk>/update', views.FormatUpdate.as_view(), name='format-update'),
  
  path('lens/', views.LensList.as_view(), name='lens-list'),
  path('lens/<int:pk>', views.LensDetail.as_view(), name='lens-detail'),
  path('lens/create/', views.LensCreate.as_view(), name='lens-create'),
  path('lens/<int:pk>/update', views.LensUpdate.as_view(), name='lens-update'),
  
  path('lensmodel/', views.LensModelList.as_view(), name='lensmodel-list'),
  path('lensmodel/<int:pk>', views.LensModelDetail.as_view(), name='lensmodel-detail'),
  path('lensmodel/create/', views.LensModelCreate.as_view(), name='lensmodel-create'),
  path('lensmodel/<int:pk>/update', views.LensModelUpdate.as_view(), name='lensmodel-update'),
  
  path('manufacturer/', views.ManufacturerList.as_view(), name='manufacturer-list'),
  path('manufacturer/<int:pk>', views.ManufacturerDetail.as_view(), name='manufacturer-detail'),
  path('manufacturer/create/', views.ManufacturerCreate.as_view(), name='manufacturer-create'),
  path('manufacturer/<int:pk>/update', views.ManufacturerUpdate.as_view(), name='manufacturer-update'),
  
  path('mount/', views.MountList.as_view(), name='mount-list'),
  path('mount/<int:pk>', views.MountDetail.as_view(), name='mount-detail'),
  path('mount/create/', views.MountCreate.as_view(), name='mount-create'),
  path('mount/<int:pk>/update', views.MountUpdate.as_view(), name='mount-update'),
  
  path('mountadapter/', views.MountAdapterList.as_view(), name='mountadapter-list'),
  path('mountadapter/<int:pk>', views.MountAdapterDetail.as_view(), name='mountadapter-detail'),
  path('mountadapter/create/', views.MountAdapterCreate.as_view(), name='mountadapter-create'),
  path('mountadapter/<int:pk>/update', views.MountAdapterUpdate.as_view(), name='mountadapter-update'),
  
  path('negativesize/', views.NegativeSizeList.as_view(), name='negativesize-list'),
  path('negativesize/<int:pk>', views.NegativeSizeDetail.as_view(), name='negativesize-detail'),
  path('negativesize/create/', views.NegativeSizeCreate.as_view(), name='negativesize-create'),
  path('negativesize/<int:pk>/update', views.NegativeSizeUpdate.as_view(), name='negativesize-update'),
  
  path('order/', views.OrderList.as_view(), name='order-list'),
  path('order/<int:pk>', views.OrderDetail.as_view(), name='order-detail'),
  path('order/create/', views.OrderCreate.as_view(), name='order-create'),
  path('order/<int:pk>/update', views.OrderUpdate.as_view(), name='order-update'),
  
  path('paperstock/', views.PaperStockList.as_view(), name='paperstock-list'),
  path('paperstock/<int:pk>', views.PaperStockDetail.as_view(), name='paperstock-detail'),
  path('paperstock/create/', views.PaperStockCreate.as_view(), name='paperstock-create'),
  path('paperstock/<int:pk>/update', views.PaperStockUpdate.as_view(), name='paperstock-update'),
  
  path('person/', views.PersonList.as_view(), name='person-list'),
  path('person/<int:pk>', views.PersonDetail.as_view(), name='person-detail'),
  path('person/create/', views.PersonCreate.as_view(), name='person-create'),
  path('person/<int:pk>/update', views.PersonUpdate.as_view(), name='person-update'),
  
  path('print/', views.PrintList.as_view(), name='print-list'),
  path('print/<int:pk>', views.PrintDetail.as_view(), name='print-detail'),
  path('print/create/', views.PrintCreate.as_view(), name='print-create'),
  path('print/<int:pk>/update', views.PrintUpdate.as_view(), name='print-update'),
  
  path('process/', views.ProcessList.as_view(), name='process-list'),
  path('process/<int:pk>', views.ProcessDetail.as_view(), name='process-detail'),
  path('process/create/', views.ProcessCreate.as_view(), name='process-create'),
  path('process/<int:pk>/update', views.ProcessUpdate.as_view(), name='process-update'),
  
  path('repair/', views.RepairList.as_view(), name='repair-list'),
  path('repair/<int:pk>', views.RepairDetail.as_view(), name='repair-detail'),
  path('repair/create/', views.RepairCreate.as_view(), name='repair-create'),
  path('repair/<int:pk>/update', views.RepairUpdate.as_view(), name='repair-update'),
  
  path('scan/', views.ScanList.as_view(), name='scan-list'),
  path('scan/<int:pk>', views.ScanDetail.as_view(), name='scan-detail'),
  path('scan/create/', views.ScanCreate.as_view(), name='scan-create'),
  path('scan/<int:pk>/update', views.ScanUpdate.as_view(), name='scan-update'),
  
  path('negative/', views.NegativeList.as_view(), name='negative-list'),
  path('negative/<int:pk>', views.NegativeDetail.as_view(), name='negative-detail'),
  path('negative/create/', views.NegativeCreate.as_view(), name='negative-create'),
  path('negative/<int:pk>/update', views.NegativeUpdate.as_view(), name='negative-update'),
  
  path('film/', views.FilmList.as_view(), name='film-list'),
  path('film/<int:pk>', views.FilmDetail.as_view(), name='film-detail'),
  path('film/create/', views.FilmCreate.as_view(), name='film-create'),
  path('film/<int:pk>/update', views.FilmUpdate.as_view(), name='film-update'),
  
  path('series/', views.SeriesList.as_view(), name='series-list'),
  path('series/<int:pk>', views.SeriesDetail.as_view(), name='series-detail'),
  path('series/create/', views.SeriesCreate.as_view(), name='series-create'),
  path('series/<int:pk>/update', views.SeriesUpdate.as_view(), name='series-update'),
  
  path('teleconverter/', views.TeleconverterList.as_view(), name='teleconverter-list'),
  path('teleconverter/<int:pk>', views.TeleconverterDetail.as_view(), name='teleconverter-detail'),
  path('teleconverter/create/', views.TeleconverterCreate.as_view(), name='teleconverter-create'),
  path('teleconverter/<int:pk>/update', views.TeleconverterUpdate.as_view(), name='teleconverter-update'),
  
  path('toner/', views.TonerList.as_view(), name='toner-list'),
  path('toner/<int:pk>', views.TonerDetail.as_view(), name='toner-detail'),
  path('toner/create/', views.TonerCreate.as_view(), name='toner-create'),
  path('toner/<int:pk>/update', views.TonerUpdate.as_view(), name='toner-update'),
]
