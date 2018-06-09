from django import forms
from django.contrib.auth.models import User

class signupform(forms.ModelForm):
  email = forms.EmailField(max_length=70)
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = [
               'username',
               'email',
               'password',
             ]
