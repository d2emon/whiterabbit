# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime


username = "МихалычЪ"


def index(request):
    return render(request, "greet/index.html", {
        "username": username,
        "today": datetime.date.today(),
    })


def contact(request):
    return render(request, "greet/contact.html", {
        "username": username,
        "today": datetime.date.today(),
    })


def gallery(request):
    return render(request, "greet/gallery.html", {
        "username": username,
        "today": datetime.date.today(),
    })


def service(request):
    return render(request, "greet/service.html", {
        "username": username,
        "today": datetime.date.today(),
    })


def full(request):
    return render(request, "greet/full.html", {
        "username": username,
        "today": datetime.date.today(),
    })


def buttons(request):
    return render(request, "greet/buttons.html", {
        "username": username,
        "today": datetime.date.today(),
    })
