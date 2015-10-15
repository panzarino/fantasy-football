import django
from football import points

def index(request):
    return django.shortcuts.render(request, 'index.html')

def search(request):
    return django.shortcuts.render(request, 'search.html')
    
def results(request):
    return django.shortcuts.render(request, 'results.html')