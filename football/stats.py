import nflgame # https://github.com/BurntSushi/nflgame

def total_stats(name, year, max_wk):
    wks = []
    for x in range(1, (max_wk+1)):
        wks.append(x)
    return player_stats(name, year, wks)

def player_stats(name, year, wk):
    # takes player's full name, year of game(s), week of game(s)
    # returns stats based on player's position
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return False
    player = playerlist[0]
    player_id = player.gsis_id
    player_position = player.position
    if player_position == 'RB' or player_position == 'WR' or player_position == 'TE' or player_position == 'QB':
        output = main_stats(player_id, year, wk)
    elif player_position == "K":
        output = k_stats(player_id, year, wk)
    else:
        output = False
    return output

def main_stats(player_id, year, wk):
    # takes player's id, year of game(s), week of game(s)
    # applies for all skill position players (QB, RB, WR, TE)
    stats = {'rushing_yds':0, 'rushing_tds':0, 'receiving_yds':0, 'receiving_tds':0, 'fumbles':0, 'puntret_tds':0, 'kickret_tds':0, 'rushing_2pt':0, 'receiving_2pt':0, 'passing_yds':0, 'passing_tds':0, 'passing_ints':0, 'passing_2pt':0}
    games = nflgame.games(year, week=wk)
    gameplayers = nflgame.combine_game_stats(games)
    for p in gameplayers:
        if p.playerid == player_id:
            stats['rushing_yds']=p.rushing_yds
            stats['rushing_tds']=p.rushing_tds
            stats['receiving_yds']=p.receiving_yds
            stats['receiving_tds']=p.receiving_tds
            stats['fumbles']=p.fumbles_tot
            stats['puntret_tds']=p.puntret_tds
            stats['kickret_tds']=p.kickret_tds
            stats['rushing_2pt']=p.rushing_twoptm
            stats['receiving_2pt']=p.receiving_twoptm
            stats['passing_yds']=p.passing_yds
            stats['passing_tds']=p.passing_tds
            stats['passing_ints']=p.passing_ints
            stats['passing_2pt']=p.passing_twoptm
            stats['receptions']=p.receiving_rec
    return stats

def k_stats(player_id, year, wk):
    # takes player's full name, year of game(s), week of game(s)
    # applies for all kickers
    stats = {'fgmade':0, 'fga':0, 'xpmade':0, 'xpa':0}
    games = nflgame.games(year, week=wk)
    gameplayers = nflgame.combine_game_stats(games)
    for p in gameplayers:
        if p.playerid == player_id:
            stats['fgmade']=p.kicking_fgm
            stats['fga']=p.kicking_fga
            stats['xpmade']=p.kicking_xpmade
            stats['xpa']=p.kicking_xpa
    return stats

def d_stats(team_symbol, year, wk):
    # takes team symbol, year of games(s), week of game(s)
    # used for D/ST stats
    stats = {'rushing_yds_allowed':0, 'rushing_tds_allowed':0, 'passing_yds_allowed':0, 'passing_tds_allowed':0, 'total_points_allowed':0, 'passing_ints':0, 'fumbles_forced':0, 'top_rec_performances':{}}
    games = nflgame.games(year, week=wk, home=team_symbol, away=team_symbol)
    gameplayers = nflgame.combine_game_stats(games)
    for g in games:
        if g.home != team_symbol:
            stats['total_points_allowed']=g.score_home
        if g.away != team_symbol:
            stats['total_points_allowed']=g.score_away
    for p in gameplayers:
        if p.team != team_symbol:
            stats['rushing_tds_allowed']+=p.rushing_yds
            stats['rushing_tds_allowed']+=p.rushing_tds
            stats['passing_tds_allowed']+=p.passing_yds
            stats['passing_tds_allowed']+=p.passing_tds
            stats['passing_ints']+=p.passing_ints
            stats['fumbles_forced']+=p.fumbles_tot
    for p in gameplayers.receiving().sort('receiving_yds').limit(3):
        if p.team != team_symbol:
            stats['top_rec_performances'][p.name]={}
            stats['top_rec_performances'][p.name]['receiving_yds']=p.receiving_yds
            stats['top_rec_performances'][p.name]['receiving_tds']=p.receiving_tds
    return stats