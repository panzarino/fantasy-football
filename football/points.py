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
    player_stats = get_stats(name, year, wks)
    points = {}
    # unfinished method