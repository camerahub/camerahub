"""
This module defines legacy UI routes
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from schema import views

urlpatterns = [

    #path('archive/<int:id_owner>/print',
    #     views.ArchivePrint.as_view(), name='archive-print'),

    #path('camera/<int:id_owner>/sell', views.CameraSell.as_view(), name='camera-sell'),

    #path('lens/<int:id_owner>/sell', views.LensSell.as_view(), name='lens-sell'),

    #path('print/<int:id_owner>/print',
    #     views.PrintPrint.as_view(), name='print-print'),
    #path('print/<int:id_owner>/archive', views.PrintArchive.as_view(), name='print-archive'),
    #path('print/<int:id_owner>/sell', views.PrintSell.as_view(), name='print-sell'),

    path('film/<int:id_owner>/print',
         views.FilmPrint.as_view(), name='film-print'),
    #path('film/<int:id_owner>/load', views.FilmLoad.as_view(), name='film-load'),
    #path('film/<int:id_owner>/develop', views.FilmDevelop.as_view(), name='film-develop'),
    #path('film/<int:id_owner>/archive', views.FilmArchive.as_view(), name='film-archive'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
