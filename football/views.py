from django.shortcuts import render
from django.http import Http404
from football import points, stats, schedule
import nflgame # https://github.com/BurntSushi/nflgame/
from datetime import date

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')
    
def results(request):
    if 'name' not in request.GET:
        return render(request, 'results.html', {'error':True, 'title':"Error"})
    name = request.GET['name']
    year = date.today().year
    week = schedule.current_week()
    weeks = []
    for x in range(1,week+1):
        weeks.append(x)
    results = points.standard_player_points(name, year, weeks)
    if results == False:
        return render(request, 'results.html', {'error':True, 'title':"Error"})
    return render(request, 'results.html', {'title':name, 'name':name})

def scoreboard(request):
    current_week = schedule.current_week()
    year = date.today().year
    games = nflgame.games(year, week=current_week)
    scores = []
    for x in games:
        scores.append(x)
    weeks = []
    for x in range(0,current_week):
        weeks.append(x+1)
    return render(request, 'scoreboard.html', {'scores':scores,'week':current_week, 'past_weeks':weeks})

def previous_scoreboard(request, offset):
    try:
        wk = int(offset)
    except ValueError:
        raise Http404()
    current_week = schedule.current_week()
    if wk>current_week:
        raise Http404()
    year = date.today().year
    games = nflgame.games(year, week=wk)
    scores = []
    for x in games:
        scores.append(x)
    weeks = []
    for x in range(0,current_week):
        weeks.append(x+1)
    return render(request, 'previous_scoreboard.html', {'scores':scores,'week':wk, 'past_weeks':weeks})