from django.http import HttpResponse
from django.shortcuts import render
from contributors.models import Contributor


def about_page(request):
    #contributors = Contributor.objects.get()
    return render(request, 'about.html')
