import nflgame # https://github.com/BurntSushi/nflgame

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
    # takes players full name, year of game, week of game(s)
    # applies for all players that can play in the flex (RB, WR, TE)
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    else:
        player = playerlist[0]
        stats = {'rushing_yds':0, 'rushing_tds':0, 'receiving_yds':0, 'receiving_tds':0}
        games = nflgame.games(year, week=wk)
        gameplayers = nflgame.combine_game_stats(games)
        for p in gameplayers.rushing():
            if p.name == player.gsis_name:
                stats['rushing_yds']=p.rushing_yds
                stats['rushing_tds']=p.rushing_tds
        for p in gameplayers.receiving():
            if p.name == player.gsis_name:
                stats['receiving_yds']=p.receiving_yds
                stats['receiving_tds']=p.receiving_tds
    return stats
    # returns rushing yards, rushing tds, receiving yard, receiving tds
    
def qbstats(name, year, wk):
    # takes players full name, year of game, week of game(s)
    # applies for all quarterbacks
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    else:
        player = playerlist[0]
        stats = {'rushing_yds':0, 'rushing_tds':0, 'passing_yds':0, 'passing_tds':0, 'passing_ints':0}
        games = nflgame.games(year, week=wk)
        gameplayers = nflgame.combine_game_stats(games)
        for p in gameplayers.passing():
            if p.name == player.gsis_name:
                stats['passing_yds']=p.passing_yds
                stats['passing_tds']=p.passing_tds
                stats['passing_ints']=p.passing_ints
        for p in gameplayers.rushing():
            if p.name == player.gsis_name:
                stats['rushing_yds']=p.rushing_yds
                stats['rushing_tds']=p.rushing_tds
        return stats

# Note: still need to add some stats such as fumbles, change to dictionary not array