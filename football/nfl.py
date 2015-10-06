import nflgame

def rbstats(name, year, wk):
    # takes players full name, year of game, week of game
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