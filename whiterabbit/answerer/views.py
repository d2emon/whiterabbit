# -*- coding: utf-8 -*-
from django.shortcuts import render
from answerer.models import Answer
import datetime


username = "МихалычЪ"


def index(request):
    return render(request, 'answerer/index.html', {
        "username": username,
        "today": datetime.date.today(),
        'answer': Answer.random_item(),
    })
