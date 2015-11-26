# -*- coding: utf-8 -*-
from django.shortcuts import render


username = "МихалычЪ"


def index(request):
    return render(request, "greet/index.html", {
        "username": username,
    })


def contact(request):
    return render(request, "greet/contact.html", {
        "username": username,
    })


def gallery(request):
    return render(request, "greet/gallery.html", {
        "username": username,
    })


def service(request):
    return render(request, "greet/service.html", {
        "username": username,
    })


def full(request):
    return render(request, "greet/full.html", {
        "username": username,
    })


def buttons(request):
    return render(request, "greet/buttons.html", {
        "username": username,
    })
