from django.shortcuts import render
from django.http import Http404
from football import points, stats, schedule
import nflgame # https://github.com/BurntSushi/nflgame/
from datetime import date
from collections import OrderedDict

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')
    
def results(request):
    if 'name' not in request.GET or 'scoring' not in request.GET:
        return render(request, 'results.html', {'error':True, 'title':"Error"})
    name = request.GET['name']
    scoring = request.GET['scoring']
    year = date.today().year
    week = schedule.current_week()
    weeks = []
    for x in range(1,week+1):
        weeks.append(x)
    if scoring == 'standard':
        results = points.standard_player_points(name, year, weeks)
    elif scoring == 'decimal':
        results = points.decimal_player_points(name, year, weeks)
    elif scoring == 'standard_ppr':
        results = points.standard_ppr_player_points(name, year, weeks)
    elif scoring == 'decimal_ppr':
        results = points.decimal_ppr_player_points(name, year, weeks)
    elif scoring == 'standard_half_ppr':
        results = points.standard_half_ppr_player_points(name, year, weeks)
    elif scoring == 'decimal_half_ppr':
        results = points.decimal_half_ppr_player_points(name, year, weeks)
    else:
        return render(request, 'results.html', {'error':True, 'title':"Error"})
    if results == False:
        return render(request, 'results.html', {'error':True, 'title':"Error"})
    bye_week = schedule.bye_week_player(name, year)
    total_points = points.total_points(results);
    graph_total_points = points.total_points_no_bye(results)
    ordered_total_points = OrderedDict(sorted(total_points.items()))
    graph_ordered_total_points = OrderedDict(sorted(graph_total_points.items()))
    total_stats = stats.total_stats(name, year, week);
    return render(request, 'results.html', {'title':name, 'name':name, 'total_stats':total_stats, 'results':results, 'scoring':scoring, 'graph_ordered_total_points':graph_ordered_total_points, 'bye_week':bye_week})

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