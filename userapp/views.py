from django.shortcuts import render
from django.views import View
from django.conf import settings

from .models import *

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

class KodTasdiqlash(View):
    def get(self, request):
        return render(request, 'kod_tasdiqlash.html')
