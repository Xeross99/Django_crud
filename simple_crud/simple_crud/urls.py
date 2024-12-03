from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', views.index, name='index'),
    path('wszystkie_produkty/', views.products, name='wszystkie_produkty'),
    path('produkty/<int:product_id>/', views.product_id, name='product_id'),
    path('produkty/nowy/', views.create_product, name='product_new_path'),
    path('produkt/<int:product_id>/edytuj/', views.edit_product, name='product_edit_path'),
]