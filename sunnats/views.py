from django.http import HttpRequest
from django.shortcuts import render

from .models import *


def index(request: HttpRequest):
    return render(request, "index.html", {
        "categories": SunnatCategory.objects.all()
    })


def category(request: HttpRequest, slug):
    category = SunnatCategory.objects.get(slug=slug)
    return render(request, "category.html", {
        "category": category
    })


def biographies(request: HttpRequest):
    return render(request, "biographies.html", {
        "biographies": Person.objects.all()
    })


def about(request: HttpRequest):
    return render(request, "about.html", {
    })