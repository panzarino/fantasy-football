def main_stats(stats):
    # takes a set of main (QB, RB, WR, TE) stats and converts it for printing
    output = {}
    output['Rushing Yards']=stats['rushing_yds']
    output['Rushing Touchdowns']=stats['rushing_tds']
    output['Receiving Yards']=stats['receiving_yds']
    output['Receiving Touchdowns']=stats['receiving_tds']
    output['Fumbles']=stats['fumbles']
    output['Punt Return Touchdowns']=stats['puntret_tds']
    output['Kick Return Touchdowns']=stats['kickret_tds']
    output['Rushing 2 Point Conversions']=stats['rushing_2pt']
    output['Receiving 2 Point Conversion']=stats['receiving_2pt']
    output['Passing Yards']=stats['passing_yds']
    output['Passing Touchdowns']=stats['passing_tds']
    output['Passing Interceptions']=stats['passing_ints']
    output['Passing 2 Point Conversions']=stats['passing_2pt']
    output['Receptions']=stats['receptions']
    return output

def k_stats(stats):
    # takes a set of kicker stats and converts it for printing
    output = {}
    output['Field Goals Made']=stats['fgmade']
    output['Field Goals Attempted']=stats['fga']
    output['Field Goals Missed']=stats['fga']-stats['fgmade']
    output['Extra Points Made']=stats['xpmade']
    output['Extra Points Attempted']=stats['xpa']
    output['Extra Points Missed']=stats['xpa']-stats['xpmade']
    return output

def qb_prediction(prediction):
    # takes a set of QB predictions and converts it for printing
    output = {}
    output['Passing Yards']=prediction['passing_yds']
    output['Passing Touchdowns']=prediction['passing_tds']
    output['Rushing Yards']=prediction['rushing_yds']
    output['Rushing Touchdowns']=prediction['rushing_tds']
    return output

def rb_prediction(prediction):
    # takes a set of RB predictions and converts it for printing
    output = {}
    output['Rushing Yards']=prediction['rushing_yds']
    output['Rushing Touchdowns']=prediction['rushing_tds']
    output['Receiving Yards']=prediction['receiving_yds']
    output['Receiving Touchdowns']=prediction['receiving_tds']
    return output

def rec_prediction(prediction):
    # takes a set of WR or TE predictions and converts it for printing
    output = {}
    output['Receiving Yards']=prediction['receiving_yds']
    output['Receiving Touchdowns']=prediction['receiving_tds']
    return output