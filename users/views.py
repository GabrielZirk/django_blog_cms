from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from .forms import NewUserForm

# Create your views here.

class RegistrationView(FormView):
    '''FormView handles get and post requests automatically <3 '''
    form_class = NewUserForm
    template_name = 'registration/register.html'
    fields = '__all__'
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        