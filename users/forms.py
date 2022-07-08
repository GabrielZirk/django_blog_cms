from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):  
    '''Django's built-in register form
    UserCreationForm sets is_superuser and is_staff as False
    '''
    email = forms.EmailField(required=True) # email field is not included in UserCreationForm out of the box
    username = forms.CharField(max_length=20, min_length=5)

    class Meta:
        model = User
        fields = ["username", "email", "password1"]

    def save(self):  
        '''Call super-save function and add email field to it'''
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user
