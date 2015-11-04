import nflgame # https://github.com/BurntSushi/nflgame
from datetime import date

def bye_week(team, year):
    # takes team symbol and year of bye week
    # returns bye week, 0 if no result, does not work for bye weeks that have not yet happened
    gameweeks = []
    for x in range(1, 18):
        games = nflgame.games(year, week=x, home=None, away=None, kind='REG', started=False)
        if games == []:
            return None
        weekteams = []
        for i in games:
            weekteams.append(i.home)
            weekteams.append(i.away)
        if team not in weekteams and weekteams!=[]:
            return x
    return None

def bye_week_player(name, year):
    # takes team symbol and year of bye week
    # returns bye week, 0 if no result, does not work for bye weeks that have not yet happened
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    player = playerlist[0]
    team = player.team
    gameweeks = []
    for x in range(1, 18):
        games = nflgame.games(year, week=x, home=None, away=None, kind='REG', started=False)
        if games == []:
            return None
        weekteams = []
        for i in games:
            weekteams.append(i.home)
            weekteams.append(i.away)
        if team not in weekteams and weekteams != []:
            return x
    return None

def current_week():
    # returns current week of season
    year = date.today().year
    for x in range(1, 18):
        games = nflgame.games(year, week=x, home=None, away=None, kind='REG', started=False)
        if games == []:
            return x-1

def opponent(team, year, week):
    # takes team symbol, year of game, week of game
    # returns opponent in a certain week
    schedule = nflgame.sched.games
    for x in schedule:
        if schedule[x]['week'] == week and schedule[x]['year'] == year:
            if schedule[x]['home'] == team:
                return schedule[x]['away']
            elif schedule[x]['away'] == team:
                return schedule[x]['home']
    return None