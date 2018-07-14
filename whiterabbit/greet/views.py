# -*- coding: utf-8 -*-
from django.shortcuts import render


username = "МихалычЪ"


def index(request):
    return render(request, "greet/index.html", {
    })


def contact(request):
    return render(request, "greet/contact.html", {
    })


def gallery(request):
    return render(request, "greet/gallery.html", {
    })


def service(request):
    return render(request, "greet/service.html", {
    })


def full(request):
    return render(request, "greet/full.html", {
    })


def buttons(request):
    return render(request, "greet/buttons.html", {
    })
