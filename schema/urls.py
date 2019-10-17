from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('camera/', views.CameraListView.as_view(), name='camera-list'),
  path('camera/<int:pk>', views.CameraDetailView.as_view(), name='camera-detail'),
  path('camera/create/', views.CameraCreate.as_view(), name='camera-create'),
  path('camera/<int:pk>/update', views.CameraUpdate.as_view(), name='camera-update'),
]