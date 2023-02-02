from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View
# Create your views here.
from page.models import *


class LognView(TemplateView):
    template_name = 'logn.html'


def my_view(request):
    return redirect('/accounts/login/', foo='bar')


def dasturlar_view(request):
    context = {
        "data": Dastur.objects.all(),
        "user": request.user,

    }

    return render(request, 'dasturlar.html', context=context)


def internet_view(request):
    context = {
        "data": Internet.objects.all(),
        "user": request.user,

    }

    return render(request, 'internet.html', context=context)


def wifi_view(request):
    context = {
        "data": Wifi.objects.all(),
        "user": request.user,

    }

    return render(request, 'wifi.html', context=context)


def kompyuter_view(request):
    context = {
        "data": Kompyuter.objects.all(),
        "user": request.user,

    }

    return render(request, 'kompyuter.html', context=context)


def server_view(request):
    context = {
        "data": Server.objects.all(),
        "user": request.user,

    }

    return render(request, 'server.html', context=context)


def hodim_view(request):
    context = {
        "data": Hodim.objects.all(),
        "user": request.user,

    }

    return render(request, 'hodim.html', context=context)


def kamera_view(request):
    context = {
        "data": Kamera.objects.all(),
        "user": request.user,

    }

    return render(request, 'kamera.html', context=context)


def gps_view(request):
    context = {
        "data": Gps.objects.all(),
        "user": request.user,

    }

    return render(request, 'gps.html', context=context)


def taklif_view(request):
    context = {
        "data": Taklif.objects.all(),
        "user": request.user,

    }

    return render(request, 'takliflar.html', context=context)
