import nflgame

def byeweek(team, year):
    # takes team symbol (3 letters) and year of bye week
    # returns bye week, 0 if no result, does not work for bye weeks that have not yet happened
    gameweeks = []
    for x in range(1, 18):
        games = nflgame.games(year, week=x, home=None, away=None, kind='REG', started=False)
        if games == []:
            return 0
        weekteams = []
        for i in games:
            weekteams.append(i.home)
            weekteams.append(i.away)
        if team not in weekteams and weekteams!=[]:
            return x
    return 0

def flexstats(name, year, wk):
    # takes players full name (string), year of game (int), week of game (int)
    # applies for all players that can play in the flex (RB, WR, TE)
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    else:
        player = playerlist[0]
        rushyds=0
        rushtd=0
        recyds=0
        rectd=0
        games = nflgame.games(year, week=wk)
        gameplayers = nflgame.combine_game_stats(games)
        for p in gameplayers.rushing():
            if p.name == player.gsis_name:
                rushyds=p.rushing_yds
                rushtd=p.rushing_tds
        for p in gameplayers.receiving():
            if p.name == player.gsis_name:
                recyds=p.receiving_yds
                rectd=p.receiving_tds
    return [rushyds, rushtd, recyds, rectd]
    # returns rushing yards, rushing tds, receiving yard, receiving tds
    
def qbstats(name, year, wk):
    # takes players full name (string), year of game (int), week of game (int)
    # applies for all quarterbacks
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    else:
        player = playerlist[0]
        passyds=0
        passtd=0
        inter=0
        rushyds=0
        rushtd=0
        games = nflgame.games(year, week=wk)
        gameplayers = nflgame.combine_game_stats(games)
        for p in gameplayers.passing():
            if p.name == player.gsis_name:
                passyds=p.passing_yds
                rushtd=p.passing_tds
                inter=p.passing_ints
        for p in gameplayers.rushing():
            if p.name == player.gsis_name:
                rushyds=p.rushing_yds
                rushtd=p.rushing_tds
        return [passyds, passtd, inter, rushyds, rushtd]

# Note: still need to add some stats such as fumbles