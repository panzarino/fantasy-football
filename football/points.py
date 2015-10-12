import nflgame # https://github.com/BurntSushi/nflgame
from football import stats, schedule

def get_stats(name, year, wks):
    # gets stats for a player
    # note: weeks must be defined as a list
    player = nflgame.find(name, team=None)[0]
    byeweek = schedule.bye_week(player.team, year)
    player_stats = {}
    for x in range(0, len(wks)):
        dictprop = 'week_'+str(wks[x])
        player_stats[dictprop]=(stats.player_stats(name, year, wks[x]))
        if wks[x] == byeweek:
            player_stats[dictprop]['bye_week'] = True
        else:
            player_stats[dictprop]['bye_week'] = False
    return player_stats

def standard_player_points(name, year, wks):
    # returns standard scoring points
    player_stats = get_stats(name, year, wks)
    print player_stats
    points = {}
    for x in player_stats:
        points[x]={}
    for x in player_stats:
        points[x]['rushing_yds']=int(player_stats[x]['rushing_yds']/10)
        points[x]['rushing_tds']=player_stats[x]['rushing_tds']*6
        points[x]['receiving_yds']=int(player_stats[x]['receiving_yds']/10)
        points[x]['receiving_tds']=player_stats[x]['receiving_tds']*6
        points[x]['fumbles']=player_stats[x]['fumbles']*(-2)
        points[x]['puntret_tds']=player_stats[x]['puntret_tds']*6
        points[x]['kickret_tds']=player_stats[x]['kickret_tds']*6
        points[x]['rushing_2pt']=player_stats[x]['rushing_2pt']*2
        points[x]['receiving_2pt']=player_stats[x]['receiving_2pt']*2
        points[x]['passing_yds']=int(player_stats[x]['passing_yds']/25)
        points[x]['passing_tds']=player_stats[x]['passing_tds']*4
        points[x]['passing_ints']=player_stats[x]['passing_ints']*(-2)
        points[x]['passing_2pt']=player_stats[x]['passing_2pt']*2
        points[x]['bye_week']=player_stats[x]['bye_week']
    return points

def standard_decimal_player_points(name, year, wks):
    # returns standard decimal scoring points
    player_stats = get_stats(name, year, wks)
    print player_stats
    points = {}
    for x in player_stats:
        points[x]={}
    for x in player_stats:
        points[x]['rushing_yds']=player_stats[x]['rushing_yds']*.1
        points[x]['rushing_tds']=player_stats[x]['rushing_tds']*6
        points[x]['receiving_yds']=player_stats[x]['receiving_yds']*.1
        points[x]['receiving_tds']=player_stats[x]['receiving_tds']*6
        points[x]['fumbles']=player_stats[x]['fumbles']*(-2)
        points[x]['puntret_tds']=player_stats[x]['puntret_tds']*6
        points[x]['kickret_tds']=player_stats[x]['kickret_tds']*6
        points[x]['rushing_2pt']=player_stats[x]['rushing_2pt']*2
        points[x]['receiving_2pt']=player_stats[x]['receiving_2pt']*2
        points[x]['passing_yds']=int(player_stats[x]['passing_yds']/25)
        points[x]['passing_tds']=player_stats[x]['passing_tds']*4
        points[x]['passing_ints']=player_stats[x]['passing_ints']*(-2)
        points[x]['passing_2pt']=player_stats[x]['passing_2pt']*2
        points[x]['bye_week']=player_stats[x]['bye_week']
    return points