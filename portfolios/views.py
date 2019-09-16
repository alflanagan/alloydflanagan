from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<p>Congrats, this is the portfolios index view.')
