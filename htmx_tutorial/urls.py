from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('lazy/', views.lazy_page, name="lazy_page"),
    path('lazy_image/', views.lazy_image, name="lazy_image"),
    path('search/', views.search, name="search"),
]
