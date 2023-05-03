from django.views import generic
from django.urls import reverse_lazy

from .usersforms import CustomUserCreation

class SignUpView(generic.CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreation
    success_url = reverse_lazy('home')