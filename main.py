import csv
from pathlib import Path
import random
import time

game_started = False
match_time = 0

def load():
    with open(( str(Path.home())+"/Downloads/IE1.csv"), 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)
        data = lines[1:]
        header = lines[0]
        return {row[0]: {header[i]: value for i, value in enumerate(row)} for row in data}

def filter_players(players, condition):
    filtered_players = {key: value for key, value in players.items() if condition(value)}
    return filtered_players

def generate_team(players):
    team = {}
    team['GK'] = select_players(players, 'GK', 1)
    team['DF'] = select_players(players, 'DF', 4)
    team['MF'] = select_players(players, 'MF', 4)
    team['FW'] = select_players(players, 'FW', 2)
    team['Score'] = 0
    return team

def select_players(players, position, count):
    filtered_players = filter_players(players, lambda x: x['Position'] == position)
    selected_players = random.sample(list(filtered_players.keys()), count)
    return selected_players

def match(blue, red, player = None):
    global game_started, match_time
    if game_started == False:
        player = touch(random.choice(list(blue['FW'])), blue)
        game_started = True
    
    while match_time < 90:
        print("Minute ", match_time)
        match_time += 1
        attributes = players[player]
        player = action(player,attributes, blue, red)
    
    print("Full Time")
    exit()
    
def action(player,attributes,blue, red):

    if attributes['Position'] == 'GK':
        return touch(player, blue)
        
    if attributes['Position'] == 'DF':
        return touch(player, blue)
        
    if attributes['Position'] == 'MF':
        return touch(player, blue)

    if attributes['Position'] == 'FW':
        return shoot(players[player], players[red['GK'][0]], blue, red)

def shoot(fw, gk, blue, red):
    print(fw['Name'] + " shoots")
    time.sleep(1)
    if int(fw['Kick']) > int(gk['Guard']):
        print("Goal!")
        blue['Score'] += 1
        print("Score: ", blue['Score'], "-", red['Score'])
        match(red, blue, gk['Name'])
    print("Saved by " + gk['Name'])
    gk['Guard'] = int(gk['Guard']) - 3
    return fw['Name']

def touch(player, team):
    print(player + " is with the ball")
    partner = random.choice([p for p in list(blue['DF'] + blue['MF'] + blue['FW']) if p != player])
    print(player + " passes to " + partner)
    return partner

players = load()
blue = generate_team(players)
red = generate_team(players)
match(blue, red)


