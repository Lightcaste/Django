from django.shortcuts import render
from django.http import HttpResponse

def mainscreen(request):
    return render(request, 'mainscreen.html')

# Create your views here.
