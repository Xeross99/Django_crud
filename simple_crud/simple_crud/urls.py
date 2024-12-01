from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', views.index, name='index'),
    path('wszyskie_produkty', views.products, name='index'),
]