from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def index(request):
    return render(request, 'schema/index.html')

from .models import Camera
class CameraListView(generic.ListView):
  model = Camera
  template_name = 'schema/list.html'

class CameraDetailView(generic.DetailView):
  model = Camera
  template_name = 'schema/detail.html'