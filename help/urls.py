from django.urls import path
from django.views.generic import TemplateView
from help.views import ConditionListView

urlpatterns = [

    # Static pages
    path('', TemplateView.as_view(template_name='index.html'), name='help'),
    path('concepts', TemplateView.as_view(template_name='concepts.html'), name='concepts'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('condition', ConditionListView.as_view(), name='condition-list'),
]
