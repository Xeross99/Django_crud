from django.shortcuts import render

def index(request):
  return render(request, 'main/dashboard.html')

def products(request):
  return render(request, 'main/index.html')