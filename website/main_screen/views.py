from django.shortcuts import render
from django.http import HttpResponse

def main_screen(request):
    return render(request, 'main_screen/main_screen.html')


