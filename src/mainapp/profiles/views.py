from django.shortcuts import render
from django.http import HttpResponse
from .models import Profiles


def admin_contacts(request):
    profiles = Profiles.objects.all()
    return render(request, "profiles/profiles_page.html", {'profiles': profiles})
