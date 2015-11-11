from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.core import serializers
from football import points, stats, schedule, predictions, convert
import nflgame # https://github.com/BurntSushi/nflgame/
from datetime import date
from collections import OrderedDict
from string import capwords
import operator

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')
    
def results(request):
    if 'name' not in request.GET or 'scoring' not in request.GET:
        return render(request, 'results.html', {'error':True, 'title':"Error"})
    name = capwords(request.GET['name'])
    scoring = request.GET['scoring']
    year = date.today().year
    week = schedule.current_week()
    weeks = []
    for x in range(1,week+1):
        weeks.append(x)
    position = stats.player_position(name)
    team = stats.player_team(name)
    if position == "QB" or position == "RB" or position == "WR" or position == "TE":
        functionname = scoring+"_player_points"
        getpoints = getattr(points, functionname)
        results = getpoints(name, year, weeks)
    elif position == "K":
        results = points.k_points(name, year, weeks)
    else:
        results = False
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
    total_stats = stats.total_stats(name, year, week)
    if position == "QB" or position == "RB" or position == "WR" or position == "TE":
        output_total_stats = convert.main_stats(total_stats)
        sorted_output_total_stats = OrderedDict(sorted(output_total_stats.items(), key=operator.itemgetter(1), reverse=True))
    elif position == "K":
        output_total_stats = convert.k_stats(total_stats)
        sorted_output_total_stats = OrderedDict(sorted(output_total_stats.items(), key=operator.itemgetter(1), reverse=True))
    else:
        return render(request, 'results.html', {'error':True, 'title':"Error"})
    average_points = predictions.average(name, scoring)
    prediction_stats = predictions.prediction(name, scoring)
    if prediction_stats == "Bye Week":
        prediction_points = "Bye Week"
        sorted_output_prediction_stats = {'Bye Week': "Bye Week"}
    else:
        if position == "QB":
            prediction_points = prediction_stats['points']
            output_prediction_stats = convert.qb_prediction(prediction_stats)
            sorted_output_prediction_stats = OrderedDict(sorted(output_prediction_stats.items(), key=operator.itemgetter(1), reverse=True))
        elif position == "RB":
            prediction_points = prediction_stats['points']
            output_prediction_stats = convert.rb_prediction(prediction_stats)
            sorted_output_prediction_stats = OrderedDict(sorted(output_prediction_stats.items(), key=operator.itemgetter(1), reverse=True))
        elif position == "WR" or position == "TE":
            prediction_points = prediction_stats['points']
            output_prediction_stats = convert.rec_prediction(prediction_stats)
            sorted_output_prediction_stats = OrderedDict(sorted(output_prediction_stats.items(), key=operator.itemgetter(1), reverse=True))
        elif position == "K":
            prediction_points = prediction_stats
            sorted_output_prediction_stats = {'Points':prediction_points}
        else:
            return render(request, 'results.html', {'error':True, 'title':"Error"})
    return render(request, 'results.html', {'title':name, 'name':name, 'total_stats':sorted_output_total_stats, 'results':results, 'scoring':scoring, 'graph_ordered_total_points':graph_ordered_total_points, 'bye_week':bye_week, 'position':position, 'team':team, 'qb':qb, 'flex':flex, 'k':k, 'average':average_points, 'predictions':sorted_output_prediction_stats, 'prediction':prediction_points})

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
    return render(request, 'scoreboard.html', {'scores':scores,'week':current_week, 'past_weeks':weeks, 'current_week':True})

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
    return render(request, 'scoreboard.html', {'scores':scores,'week':wk, 'past_weeks':weeks, 'current_week':False})

def teamnum(request, offset):
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
    if team < 1 or team > 3 or numteams < 1 or numteams > 3:
        raise Http404()
    teamcookiename = "team"+str(team)
    teamdata = request.COOKIES.get(teamcookiename, None)
    url = "/team/?"+teamdata
    return redirect(url)

def team(request):
    teamname = request.GET['teamname']
    teamnum = request.GET['teamnum']
    teamplayers = []
    for x in range(1,16):
        dataname = "player"+str(x)
        teamplayers.append(request.GET[dataname])
    qb = []
    rb = []
    wr = []
    te = []
    k = []
    none = []
    for x in teamplayers:
        if x == 'empty':
            none.append(x)
        else:
            playerposition = stats.player_position(x)
            if playerposition == "QB":
                qb.append(x)
            elif playerposition == "RB":
                rb.append(x)
            elif playerposition == "WR":
                wr.append(x)
            elif playerposition == "TE":
                te.append(x)
            elif playerposition == "K":
                k.append(x)
            else:
                none.append(x)
    scoring = request.GET['scoring']
    return render(request, "team.html", {'title':teamname, 'teamnum':teamnum, 'teamname':teamname, 'qb':qb, 'rb':rb, 'wr':wr, 'te':te, 'k':k, 'other':none, 'scoring':scoring})

def new_team(request):
    numteams = request.COOKIES.get('teams', None)
    if numteams != None:
        try:
            numteams = int(numteams)
        except ValueError:
            raise Http404()
        if numteams < 1 or numteams > 3:
            raise Http404()
        if numteams == 3:
            return render(request, 'new_team.html', {'toomany':True, 'title':'Error'})
    if numteams == None:
        teamnum = 1
    else:
        teamnum = numteams+1
    return render(request, 'new_team.html', {'title':'Create a New Team', 'teamnum':teamnum})

def team_list(request):
    numteams = request.COOKIES.get('teams', None)
    if numteams == None:
        return redirect('/team/new/')
    try:
        numteams = int(numteams)
    except ValueError:
        raise Http404()
    names = []
    for x in range(0, numteams):
        cookiename = "teamname"+str((x+1))
        name = request.COOKIES.get(cookiename, None)
        name = name.replace("_", " ")
        names.append(name)
    return render(request, 'my_teams.html', {'title':'My Teams', 'teamnames':names})

def edit_team(request, offset):
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
    if team < 1 or team > 3 or numteams < 1 or numteams > 3:
        raise Http404()
    teamcookiename = "team"+str(team)
    teamdata = request.COOKIES.get(teamcookiename, None)
    url = "/team/edit/?"+teamdata
    return redirect(url)

def edit(request):
    teamname = request.GET['teamname']
    teamnum = request.GET['teamnum']
    scoring = request.GET['scoring']
    players = []
    for x in range(1,16):
        getstr = "player"+str(x)
        players.append(request.GET[getstr])
    while len(players)<15:
        players.append('empty')
    return render(request, 'edit_team.html', {'teamname':teamname, 'players':players, 'scoring':scoring, 'teamnum':teamnum})

def player_points(request):
    scoring = request.GET['scoring']
    name = request.GET['name']
    position = request.GET['position']
    year = date.today().year
    current_week = schedule.current_week()
    bye_week = schedule.bye_week_player(name, year)
    if current_week == bye_week:
        return HttpResponse("Bye Week")
    dictkey = "Week "+str(current_week)
    current_week = [current_week]
    if position == "QB" or position == "RB" or position == "WR" or position == "TE":
        functionname = scoring+"_player_points"
        getpoints = getattr(points, functionname)
        pts = getpoints(name, year, current_week)
        total_points = points.total_points(pts)[dictkey]
        return HttpResponse(total_points)
    if position == "K":
        pts = points.k_points(name, year, current_week)
        total_points = points.total_points(pts)[dictkey]
        return HttpResponse(total_points)

def prediction(request):
    scoring = request.GET['scoring']
    name = request.GET['name']
    year = date.today().year
    current_week = schedule.current_week()
    bye_week = schedule.bye_week_player(name, year)
    if current_week == bye_week:
        return HttpResponse("Bye Week")
    prediction = predictions.prediction(name, scoring)
    return HttpResponse(prediction['points'])