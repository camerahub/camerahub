from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('cameras/', views.CameraListView.as_view(), name='cameras'),
  path('cameras/<int:pk>', views.CameraDetailView.as_view(), name='cameras'),
]