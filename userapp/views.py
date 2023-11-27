from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .models import Profil
import random
from eskiz.client import SMSClient
from django.contrib.auth import login, logout, authenticate
from .models import *

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        profil = Profil.objects.create_user(
            username = request.POST.get("t"),
            first_name = request.POST.get("f"),
            last_name = request.POST.get("l"),
            password = request.POST.get("p"),
            tel = request.POST.get("t"),
            shahar = request.POST.get("sh"),
            davlat = request.POST.get("d"),
            jins = request.POST.get("gender"),
            tasdiqlash_kodi = str(random.randrange(10000, 100000))
        )
        mijoz = SMSClient(
            api_url="https://notify.eskiz.uz/api/",
            email=settings.EMAIL,
            password=settings.P
        )
        mijoz._send_sms(
            phone_number=profil.tel,
            message=f"Alistyle uchun tasdiqlash kodingiz:"
                    f"{profil.tasdiqlash_kodi}"
        )
        login(request, profil)
        return redirect("/user/tasdiqlash/")

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.tasdiqlangan:
            return render(request, 'page-user-login.html')
        return redirect("/user/register/")

    def post(self, request):
        profil = authenticate(
            username = request.POST.get("l"),
            password = request.POST.get("p"),
        )
        if profil:
            login(request, profil)
            return redirect("/asosiy/home/")
        return redirect("/user/login/")

class KodTasdiqlash(View):
    def  get(self, request):
        return render(request, 'kod_tasdiqlash.html')

    def post(self, request):
        profil = Profil.objects.get(id=request.user.id)
        if profil.tasdiqlash_kodi == request.POST.get("k"):
            profil.tasdiqlangan = True
            profil.save()
            return redirect("/asosiy/home/")
        return redirect("/user/tasdiqlash/")
