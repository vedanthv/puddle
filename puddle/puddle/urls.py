from core.views import index,contact
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',index,name = 'index'),
    path('contact/',contact,name = 'contact'),
    path('admin/', admin.site.urls),
]
