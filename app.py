"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
--------------------------------
"""

import constants
import copy
import os

TEAMS = tuple(copy.deepcopy(constants.TEAMS))
PLAYERS = copy.deepcopy(constants.PLAYERS)

PLAYERS_CLEANED = []
players_with_exp = []
players_no_exp = []
panthers = []
bandits = []
warriors = []


# First step in balancing the team: Add a team key:value list to the players
def distribute_players(player_list):
    for i in range(len(player_list)):
        for index, team in enumerate(TEAMS):
            if index == ((i+3) % len(TEAMS)):
                player_list[i].update(team=team)


# Prints team details based on the team chosen
def print_team(index, team_name):
    print(f'\nTeam {TEAMS[index]} Stats')
    print('--------------------')
    print(f'Total players: {len(team_name)}')
    total_experienced = 0
    total_inexperienced = 0
    height = []
    players = []
    guardians = []
    for player in team_name:
        if player['experience']:
            total_experienced += 1
        else:
            total_inexperienced += 1
        height.append(player['height'])
        players.append(player['name'])
        guardians += player['guardians']
    print(f'Total experienced: {total_experienced}')
    print(f'Total inexperienced: {total_inexperienced}')
    print(f'Average height: {round(sum(height) / len(height), 2)} inches')
    print('\nPlayers on Team:')
    print('\n'.join(players))
    print('\nGuardians:')
    print(', '.join(guardians))


# Main function of the app
def basketball_stats_tool():
    while True:
        print('BASKETBALL TEAM STATS TOOL')
        print('')
        print('---- MENU----')
        print('''
Here are your choices:
[1] Display Team Stats
[2] Quit
        ''')

        choice = int(input('Enter an option: '))
        while not(choice == 1 or choice == 2):
            choice = int(input('Please an option from the choices above: '))

        if choice != 1:
            print('\nThank you for using our app. Have a good day!\n')
            exit()
        else:
            print('')
            for index, team in enumerate(TEAMS, 1):
                print(f'[{index}] {team}')

        choose_team = int(input('\nEnter an option: '))
        while not(choose_team == 1 or choose_team == 2 or choose_team == 3):
            choose_team = int(input('Please an option from the choices above: '))
            continue

        if choose_team == 1:
            print_team(0, panthers)
        elif choose_team == 2:
            print_team(1, bandits)
        elif choose_team == 3:
            print_team(2, warriors)
        else:
            exit()

        input('\n\nPress ENTER to continue...')
        # Reference: https://stackoverflow.com/questions/59497109/is-there-a-python-3-command-to-clear-the-output-console
        os.system('clear')


if __name__ == "__main__":
    # 01 This cleans the copied data and creates a new list, PLAYERS_CLEANED
    for player in PLAYERS:
        player['height'] = int(player['height'][0:3])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player['guardians'] = player['guardians'].split(' and ')
        PLAYERS_CLEANED.append(player)

    # 02 Sort the player list to experience and experienced and add them to their coresponding list
    for index, player in enumerate(PLAYERS_CLEANED):
        if player['experience']:
            players_with_exp.append(player)
        else:
            players_no_exp.append(player)

    distribute_players(players_with_exp)
    distribute_players(players_no_exp)

    # 03 Distribute the players to the 3 teams equally
    for i in range(9):
        if players_with_exp[i]['team'] == 'Panthers' and players_no_exp[i]['team'] == 'Panthers':
            panthers.append(players_with_exp[i])
            panthers.append(players_no_exp[i])
        elif players_with_exp[i]['team'] == 'Bandits' and players_no_exp[i]['team'] == 'Bandits':
            bandits.append(players_with_exp[i])
            bandits.append(players_no_exp[i])
        elif players_with_exp[i]['team'] == 'Warriors' and players_no_exp[i]['team'] == 'Warriors':
            warriors.append(players_with_exp[i])
            warriors.append(players_no_exp[i])

    basketball_stats_tool()
