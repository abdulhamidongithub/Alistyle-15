from django.shortcuts import render
from django.views import View

class HomeLoginsizView(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class HomeView(View):
    def get(self, request):
        return render(request, 'page-index.html')

