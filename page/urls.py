from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from page.views import *
from home import settings
from page import views
urlpatterns = [

                  path("", my_view, name="home"),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('dasturlar', views.dasturlar_view, name='dasturlar'),
                  path('internet', views.internet_view, name='internet'),
                  path('wifi', views.wifi_view, name='wifi'),
                  path('kompyuter', views.kompyuter_view, name='kompyuter'),
                  path('server', views.server_view, name='server'),
                  path('hodim', views.hodim_view, name='hodim'),
                  path('kamera', views.kamera_view, name='kamera'),
                  path('gps', views.gps_view, name='gps'),
                  path('taklif', views.taklif_view, name='taklif'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
