from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request == "POST":
        return HttpResponse("you must have posted smth")
    else: return HttpResponse(request.method)
