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

def flex_stats(name, year, wk):
    # takes players full name, year of game, week of game(s)
    # applies for all players that can play in the flex (RB, WR, TE)
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    else:
        player = playerlist[0]
        stats = {'rushing_yds':0, 'rushing_tds':0, 'receiving_yds':0, 'receiving_tds':0, 'fumbles':0}
        games = nflgame.games(year, week=wk)
        gameplayers = nflgame.combine_game_stats(games)
        for p in gameplayers:
            if p.name == player.gsis_name:
                stats['rushing_yds']+=p.rushing_yds
                stats['rushing_tds']+=p.rushing_tds
                stats['receiving_yds']+=p.receiving_yds
                stats['receiving_tds']+=p.receiving_tds
                stats['fumbles']+=p.fumbles_tot
        return stats
    
def qb_stats(name, year, wk):
    # takes players full name, year of game, week of game(s)
    # applies for all quarterbacks
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    else:
        player = playerlist[0]
        stats = {'rushing_yds':0, 'rushing_tds':0, 'passing_yds':0, 'passing_tds':0, 'passing_ints':0, 'fumbles':0}
        games = nflgame.games(year, week=wk)
        gameplayers = nflgame.combine_game_stats(games)
        for p in gameplayers:
            if p.name == player.gsis_name:
                stats['passing_yds']+=p.passing_yds
                stats['passing_tds']+=p.passing_tds
                stats['passing_ints']+=p.passing_ints
                stats['rushing_yds']+=p.rushing_yds
                stats['rushing_tds']+=p.rushing_tds
                stats['fumbles']+=p.fumbles_tot
        return stats

def k_stats(name, year, wk):
    # takes players full name, year of game, week of game(s)
    # applies for all kickers
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    else:
        player = playerlist[0]
        stats = {'fgmade':0, 'fga':0, 'xpmade':0, 'xpa':0}
        games = nflgame.games(year, week=wk)
        gameplayers = nflgame.combine_game_stats(games)
        for p in gameplayers:
            if p.name == player.gsis_name:
                stats['fgmade']+=p.kicking_fgm
                stats['fga']+=p.kicking_fga
                stats['xpmade']+=p.kicking_xpmade
                stats['xpa']+=p.kicking_xpa
        return stats
        # need to find way to get fg yards