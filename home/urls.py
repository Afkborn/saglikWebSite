from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('services/<int:service_id>/', views.services, name='services'),
    path('services/', views.servicesHome, name='services'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)