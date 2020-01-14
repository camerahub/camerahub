from .forms import UserCreationFormWithEmail
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'signup.html'