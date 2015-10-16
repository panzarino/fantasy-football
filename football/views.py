from django.shortcuts import render
from football import points, stats, schedule
import nflgame # https://github.com/BurntSushi/nflgame/

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')
    
def results(request):
    return render(request, 'results.html')

def scoreboard(request):
    current_week = schedule.current_week()
    from datetime import date
    year = date.today().year
    games = nflgame.games(year, week=current_week)
    scores = []
    for x in games:
        scores.append(x)
    return render(request, 'scoreboard.html', {'scores':scores})