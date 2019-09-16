from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(content=b"<p>Congrats, you've reached the blogs index view</p>")
