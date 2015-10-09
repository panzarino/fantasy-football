import nflgame # https://github.com/BurntSushi/nflgame

def find(team, year):
    # takes team symbol (3 letters) and year of bye week
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