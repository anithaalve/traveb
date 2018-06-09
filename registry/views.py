# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from django.views.generic import View
from registry.forms import signupform

# Create your views here.

def login(request):
  return render(request, 'registry/login.html')

def logout(request):
  return render(request, 'registry/logout.html')

class signupformview(View):
  formclass = signupform
  templatename = 'registry/signup.html'

  def get(self, request):
    form = self.formclass(None)
    return render(request, self.templatename, {'form': form})

  def post(self, request):
    form = self.formclass(request.POST)

    if form.is_valid():
      user = form.save(commit=False)

      #cleaning the data(nomalize)
      username =  form.cleaned_data['username']
      password =  form.cleaned_data['password']
      user.set_password(password)
      user.save()

      #return user object if authentication is success
      user = authenticate(username=username, password=password)

      if user is not None:
        if user.is_active:
          authlogin(request, user)
          return redirect('/')
   
    return render(request, self.templatename, {'form': form})

def profile(request):
  args = {'user': request.user}
  return render(request, 'registry/profile.html', args)
