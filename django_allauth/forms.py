#django_allauth/forms.py
from django.contrib.auth import get_user_model
#from django.forms import forms
from django import forms

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']




