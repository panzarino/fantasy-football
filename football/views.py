from django.shortcuts import render, redirect
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
    position = stats.player_position(name)
    qb = False
    flex = False
    k = False
    if position == "QB":
        qb = True
    elif position == "K":
        k = True
    elif position == "WR" or position == "RB" or position == "TE":
        flex = True
    else:
        return render(request, 'results.html', {'error':True, 'title':"Error"})
    bye_week = schedule.bye_week_player(name, year)
    total_points = points.total_points(results);
    graph_total_points = points.total_points_no_bye(results)
    ordered_total_points = OrderedDict(sorted(total_points.items()))
    graph_ordered_total_points = OrderedDict(sorted(graph_total_points.items()))
    total_stats = stats.total_stats(name, year, week);
    return render(request, 'results.html', {'title':name, 'name':name, 'total_stats':total_stats, 'results':results, 'scoring':scoring, 'graph_ordered_total_points':graph_ordered_total_points, 'bye_week':bye_week, 'position':position, 'qb':qb, 'flex':flex, 'k':k})

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

def team(request, offset):
    numteams = request.COOKIES.get('teams', None)
    if numteams == None:
        return redirect('/team/new/')
    try:
        numteams = int(numteams)
    except ValueError:
        raise Http404()
    try:
        team = int(offset)
    except ValueError:
        raise Http404()
    if team < 0 or team > 2 or numteams < 0 or numteams > 2:
        raise Http404()
    return render(request, 'team.html', {'team':team})

def new_team(request):
    numteams = request.COOKIES.get('teams', None)
    if numteams != None:
        try:
            numteams = int(numteams)
        except ValueError:
            raise Http404()
        if numteams < 0 or numteams > 2:
            raise Http404()
        if numteams == 2:
            return render(request, 'new_team.html', {'toomany':True, 'title':'Error'})
    if numteams == None:
        teamnum = 1
    else:
        teamnum = numteams+1
    return render(request, 'new_team.html', {'title':'Create a New Team', 'teamnum':teamnum})