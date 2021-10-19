""" Configure views for Homepage app """
from django.shortcuts import render


def index(request):
    """ A view to return index of homepage """
    return render(request, 'homepage/index.html')
