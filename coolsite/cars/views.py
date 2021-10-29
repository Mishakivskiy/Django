from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Cars app page.")

def categories(request, catid):
    return HttpResponse(f"<h1>Categories</h1><p>{catid}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Years Archive</h1><p>{year}</p>")
