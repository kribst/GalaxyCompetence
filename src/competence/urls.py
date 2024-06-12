from django.urls import path
from .views import index, contact, service, error, success, details

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('service/<int:myid>', details, name='details'),
    path('error/', error, name='error'),
    path('success/', success, name='success'),
    path('<int:myid>', details, name='details'),
]
