from django.shortcuts import render
from football import points

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')
    
def results(request):
    return render(request, 'results.html')