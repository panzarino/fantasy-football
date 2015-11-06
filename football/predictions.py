import nflgame # https://github.com/BurntSushi/nflgame/
from football import stats, points, schedule

def average(name, scoring):
    # takes player name, type of scoring
    # returns player average points
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return None
    player = playerlist[0]
    team = player.team
    position = player.position
    year, current_week = nflgame.live.current_year_and_week()
    bye_week = schedule.bye_week(team, year)
    wk = []
    for x in range(1, current_week):
        if x != bye_week:
            wk.append(x)
    if position == "K":
        player_points = points.total_points(points.k_points(name, year, wk))
    else:
        functionname = scoring+"_player_points"
        getpoints = getattr(points, functionname)
        player_points = points.total_points(getpoints(name, year, wk))
    weeks_played = 0
    total_points = 0
    for x in player_points:
        if player_points[x] != 0:
            total_points += player_points[x]
            weeks_played += 1
    avg = round(float(total_points)/weeks_played)
    return avg

def prediction(name, scoring):
    # takes player name, type of scoring
    # returns fantasy point prediction for next week
    playerlist = nflgame.find(name, team=None)
    if playerlist == []:
        return None
    player = playerlist[0]
    team = player.team
    position = player.position
    if position == "K":
        return average(name, scoring)
    year, current_week = nflgame.live.current_year_and_week()
    opponent = schedule.opponent(team, year, current_week)
    if opponent == None:
        return "Bye Week"
    bye_week = schedule.bye_week(team, year)
    wk = []
    for x in range(1, current_week):
        if x != bye_week:
            wk.append(x)
    total_weeks = []
    for x in range(1, current_week):
        total_weeks.append(x)
    functionname = scoring+"_player_points"
    getpoints = getattr(points, functionname)
    player_points = points.total_points(getpoints(name, year, wk))
    weeks_played = 0
    for x in player_points:
        if player_points[x] != 0:
            weeks_played += 1
    total_player_stats = stats.player_stats(name, year, wk)
    total_opponent_stats = stats.defense_team_stats(opponent, year, total_weeks)
    total_team_stats = stats.offense_team_stats(team, year, total_weeks)
    opponent_weeks_played = len(total_weeks)
    if schedule.bye_week(opponent, year) < current_week:
        opponent_weeks_played-=1
    if position == "QB":
        # calculate passing yds
        player_avg_passing_yds = float(total_player_stats['passing_yds'])/weeks_played
        opponent_avg_passing_yds = float(total_opponent_stats['passing_yds_allowed'])/opponent_weeks_played
        prediction_passing_yds = round((player_avg_passing_yds+opponent_avg_passing_yds)/2)
        # calculate passing tds
        player_avg_passing_tds = float(total_player_stats['passing_tds'])/weeks_played
        opponent_avg_passing_tds = float(total_opponent_stats['passing_tds_allowed'])/opponent_weeks_played
        prediction_passing_tds = round((player_avg_passing_tds+opponent_avg_passing_tds)/2)
        # calculate rushing yds
        player_avg_rushing_yds = float(total_player_stats['rushing_yds'])/weeks_played
        player_rushing_yds_pct = float(total_player_stats['rushing_yds'])/total_team_stats['rushing_yds'] # percentage of total yds the player contributes
        opponent_avg_rushing_yds = float(total_opponent_stats['rushing_yds_allowed'])/opponent_weeks_played
        prediction_rushing_yds = round(player_rushing_yds_pct*(player_avg_rushing_yds+opponent_avg_rushing_yds)/2)
        # calculate rushing tds
        player_avg_rushing_tds = float(total_player_stats['rushing_yds'])/weeks_played
        player_rushing_tds_pct = float(total_player_stats['rushing_tds'])/total_team_stats['rushing_tds'] # percentage of total tds the player contributes
        opponent_avg_rushing_tds = float(total_opponent_stats['rushing_tds_allowed'])/opponent_weeks_played
        prediction_rushing_tds = round(player_rushing_tds_pct*(player_avg_rushing_tds+opponent_avg_rushing_tds)/2)
        # calculate total points
        prediction_total_points = prediction_passing_yds*.04 + prediction_passing_tds*4 + prediction_rushing_yds*.1 + prediction_rushing_tds*6
        # return predictions
        return {'passing_yds':prediction_passing_yds, 'passing_tds':prediction_passing_tds, 'rushing_yds':prediction_rushing_yds, 'rushing_tds':prediction_rushing_tds, 'points':prediction_total_points}
    elif position == "RB":
        # calculate rushing yds
        player_avg_rushing_yds = float(total_player_stats['rushing_yds'])/weeks_played
        player_rushing_yds_pct = float(total_player_stats['rushing_yds'])/total_team_stats['rushing_yds'] # percentage of total yds the player contributes
        opponent_avg_rushing_yds = float(total_opponent_stats['rushing_yds_allowed'])/opponent_weeks_played
        prediction_rushing_yds = round(player_rushing_yds_pct*(player_avg_rushing_yds+opponent_avg_rushing_yds)/2)
        # calculate rushing tds
        player_avg_rushing_tds = float(total_player_stats['rushing_tds'])/weeks_played
        player_rushing_tds_pct = float(total_player_stats['rushing_tds'])/total_team_stats['rushing_tds'] # percentage of total tds the player contributes
        opponent_avg_rushing_tds = float(total_opponent_stats['rushing_tds_allowed'])/opponent_weeks_played
        prediction_rushing_tds = round(player_rushing_tds_pct*(player_avg_rushing_tds+opponent_avg_rushing_tds)/2)
        # percentages are generally very low for good players
        if (prediction_rushing_tds == 0 and player_rushing_tds_pct > .35) or weeks_played-player_avg_rushing_tds<4:
            prediction_rushing_tds += 1.0
        # calculate receiving yds
        player_avg_receiving_yds = float(total_player_stats['receiving_yds'])/weeks_played
        player_receiving_yds_pct = float(total_player_stats['receiving_yds'])/total_team_stats['passing_yds'] # percentage of total yds the player contributes
        opponent_avg_receiving_yds = float(total_opponent_stats['passing_yds_allowed'])/opponent_weeks_played
        prediction_receiving_yds = round(player_receiving_yds_pct*(player_avg_receiving_yds+opponent_avg_receiving_yds)/2)
        # calculate receiving tds
        player_avg_receiving_tds = float(total_player_stats['receiving_tds'])/weeks_played
        player_receiving_tds_pct = float(total_player_stats['receiving_tds'])/total_team_stats['passing_tds'] # percentage of total tds the player contributes
        opponent_avg_receiving_tds = float(total_opponent_stats['passing_tds_allowed'])/opponent_weeks_played
        prediction_receiving_tds = round(player_receiving_tds_pct*(player_avg_receiving_tds+opponent_avg_receiving_tds)/2)
        # percentages are generally very low for good players
        if (prediction_receiving_tds == 0 and player_receiving_tds_pct > .25) or weeks_played-player_avg_receiving_tds<4:
            prediction_receiving_tds += 1.0
        # calculate total points
        prediction_total_points = prediction_rushing_yds*.1 + prediction_rushing_tds*6 + prediction_receiving_yds*.1 + prediction_receiving_tds*6
        # return predictions
        return {'rushing_yds':prediction_rushing_yds, 'rushing_tds':prediction_rushing_tds, 'receiving_yds':prediction_receiving_yds, 'receiving_tds':prediction_receiving_tds, 'points':prediction_total_points}
    elif position == "WR" or position == "TE":
        # calculate receiving yds
        player_avg_receiving_yds = float(total_player_stats['receiving_yds'])/weeks_played
        player_receiving_yds_pct = float(total_player_stats['receiving_yds'])/total_team_stats['passing_yds'] # percentage of total yds the player contributes
        opponent_avg_receiving_yds = float(total_opponent_stats['passing_yds_allowed'])/opponent_weeks_played
        prediction_receiving_yds = round(player_receiving_yds_pct*(player_avg_receiving_yds+opponent_avg_receiving_yds)/2)
        # calculate receiving tds
        player_avg_receiving_tds = float(total_player_stats['receiving_tds'])/weeks_played
        player_receiving_tds_pct = float(total_player_stats['receiving_tds'])/total_team_stats['passing_tds'] # percentage of total tds the player contributes
        opponent_avg_receiving_tds = float(total_opponent_stats['passing_tds_allowed'])/opponent_weeks_played
        prediction_receiving_tds = round(player_receiving_tds_pct*(player_avg_receiving_tds+opponent_avg_receiving_tds)/2)
        # percentages are generally very low for good players
        if (prediction_receiving_tds == 0 and player_receiving_tds_pct > .25) or weeks_played-player_avg_receiving_tds<4:
            prediction_receiving_tds += 1
        # calculate total points
        prediction_total_points = prediction_receiving_yds*.1 + prediction_receiving_tds*6
        # return predictions
        return {'receiving_yds':prediction_receiving_yds, 'receiving_tds':prediction_receiving_tds, 'points':prediction_total_points}
    else:
        return