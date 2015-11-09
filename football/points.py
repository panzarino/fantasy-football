import nflgame # https://github.com/BurntSushi/nflgame
from football import stats, schedule

def get_stats(name, year, wks):
    # gets stats for a player
    # note: weeks must be defined as a list
    playersearch = nflgame.find(name, team=None)
    if playersearch == []:
        return False
    player = playersearch[0]
    byeweek = schedule.bye_week(player.team, year)
    player_stats = {}
    try:
        wks.remove(byeweek)
    except ValueError:
        wks=wks
    for x in range(0, len(wks)):
        dictprop = 'Week '+str(wks[x])
        player_stats[dictprop]=(stats.player_stats(name, year, wks[x]))
        player_stats[dictprop]['week']=wks[x]
        player_stats[dictprop]['bye_week'] = False
    return player_stats

def standard_player_points(name, year, wks):
    # returns standard scoring points
    player_stats = get_stats(name, year, wks)
    if player_stats == False:
        return False
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

def decimal_player_points(name, year, wks):
    # returns standard decimal scoring points
    player_stats = get_stats(name, year, wks)
    if player_stats == False:
        return False
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
        points[x]['passing_yds']=player_stats[x]['passing_yds']*.04
        points[x]['passing_tds']=player_stats[x]['passing_tds']*4
        points[x]['passing_ints']=player_stats[x]['passing_ints']*(-2)
        points[x]['passing_2pt']=player_stats[x]['passing_2pt']*2
        points[x]['bye_week']=player_stats[x]['bye_week']
    return points

def standard_ppr_player_points(name, year, wks):
    # returns standard scoring points
    player_stats = get_stats(name, year, wks)
    if player_stats == False:
        return False
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
        points[x]['receptions']=player_stats[x]['receptions']
    return points

def decimal_ppr_player_points(name, year, wks):
    # returns standard scoring points
    player_stats = get_stats(name, year, wks)
    if player_stats == False:
        return False
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
        points[x]['passing_yds']=player_stats[x]['passing_yds']*.04
        points[x]['passing_tds']=player_stats[x]['passing_tds']*4
        points[x]['passing_ints']=player_stats[x]['passing_ints']*(-2)
        points[x]['passing_2pt']=player_stats[x]['passing_2pt']*2
        points[x]['bye_week']=player_stats[x]['bye_week']
        points[x]['receptions']=player_stats[x]['receptions']
    return points

def standard_half_ppr_player_points(name, year, wks):
    # returns standard scoring points
    player_stats = get_stats(name, year, wks)
    if player_stats == False:
        return False
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
        points[x]['receptions']=player_stats[x]['receptions']*(.5)
    return points

def decimal_half_ppr_player_points(name, year, wks):
    # returns standard scoring points
    player_stats = get_stats(name, year, wks)
    if player_stats == False:
        return False
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
        points[x]['passing_yds']=player_stats[x]['passing_yds']*.04
        points[x]['passing_tds']=player_stats[x]['passing_tds']*4
        points[x]['passing_ints']=player_stats[x]['passing_ints']*(-2)
        points[x]['passing_2pt']=player_stats[x]['passing_2pt']*2
        points[x]['bye_week']=player_stats[x]['bye_week']
        points[x]['receptions']=player_stats[x]['receptions']*(.5)
    return points

def k_points(name, year, wks):
    # returns standard points for kickers
    player_stats = get_stats(name, year, wks)
    if player_stats == False:
        return False
    points = {}
    for x in player_stats:
        points[x]={}
    for x in player_stats:
        points[x]['fgmade']=float(player_stats[x]['fgmade']*3)
        points[x]['xpmade']=player_stats[x]['xpmade']
        fgmissed = player_stats[x]['fga']-player_stats[x]['fgmade']
        points[x]['fgmissed']=fgmissed*(-1)
        points[x]['bye_week']=player_stats[x]['bye_week']
    return points

def total_points(points):
    # accepts dictionary of single game points
    total_points = {}
    for x in points:
        total_points[x]={}
    for x in points:
        total = 0
        for i in points[x]:
            if i != "bye_week":
                total+=points[x][i]
        total_points[x]=total
    return total_points

def total_points_no_bye(points):
    # accepts dictionary of single game points
    # removes bye week from output
    total_points = {}
    for x in points:
        if points[x]['bye_week'] != True:
            total_points[x]={}
    for x in points:
        if points[x]['bye_week'] != True:
            total = 0
            for i in points[x]:
                if i != "bye_week":
                    total+=points[x][i]
            total_points[x]=total
    return total_points