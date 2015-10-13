import django

def index(request):
    return django.shortcuts.render(request, 'index.html')