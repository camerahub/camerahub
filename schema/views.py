from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

def index(request):
    return render(request, 'schema/index.html')

class CameraList(generic.ListView):
  model = Camera
  template_name = 'schema/list.html'

class CameraDetail(generic.DetailView):
  model = Camera
  #template_name = 'schema/detail.html'

class CameraCreate(CreateView):
  model = Camera
  fields = '__all__'
  template_name = 'schema/create.html'

class CameraUpdate(UpdateView):
  model = Camera
  fields = '__all__'
  template_name = 'schema/update.html'