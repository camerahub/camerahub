from django.urls import include, path
from rest_framework import routers
from api import views

# API endpoints
router = routers.DefaultRouter()
router.register(r'film', views.FilmViewSet)
router.register(r'negative', views.NegativeViewSet)

urlpatterns = [
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
