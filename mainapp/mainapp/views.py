from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    names = {"Bill", "Ted", "Johnny", "Daniel", "Jim", "Michael"}
    context = {
        'names': names,
    }
    return render(request, "home.html", context)