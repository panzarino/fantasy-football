import nflgame # https://github.com/BurntSushi/nflgame
from football import stats, bye_week

def get_stats(name, year, wks):
    player = nflgame.find(name, team=None)[0]
    byeweek = bye_week.find(player.team, year)
    player_stats = {}
    for x in range(0, len(wks)):
        dictprop = 'week_'+str(wks[x])
        if wks[x] == byeweek:
            player_stats[dictprop]=None
        else:
            player_stats[dictprop]=(stats.player_stats(name, year, wks[x]))