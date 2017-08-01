from django.shortcuts import render

from django.template.response import TemplateResponse

from roseapp.models import Reading


def home(request):

    data = Reading.objects.last()
    return TemplateResponse(request, 'index.html', {'data': data})

# Create your views here.
