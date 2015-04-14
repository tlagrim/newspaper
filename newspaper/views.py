from django.http import HttpResponse
from django.shortcuts import render
from contributors.models import Contributor


def about_page(request):
    
    return render(request, 'about.html')
