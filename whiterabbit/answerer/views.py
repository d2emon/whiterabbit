# -*- coding: utf-8 -*-
from django.shortcuts import render
from answerer.models import Answer


username = "МихалычЪ"


def index(request):
    return render(request, 'answerer/index.html', {
        'answer': Answer.random_item(),
    })
