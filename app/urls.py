from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'app'
urlpatterns = [
     path('cameramodel/', views.cameramodel_list().as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
