from faker import Faker
from random import shuffle


def get_players():
    players = [Faker().name() for x in range(50)]
    # while True:
    #     try:
    #         player = input('Enter Name: ')
    #         if any(p.isdigit() for p in player):
    #             raise ValueError()
    #     except ValueError:
    #         print("Enter names only!")
    #         continue
    #     if player == 'done' or player == 'd' or player == "":
    #         break
    #     else:
    #         players.append(player)
    return players


def set_teams(players):
    team_size = int(input("People per team: "))
    while len(players) % team_size != 0:
        print("Uneven amount of players for team sizes.")
        team_size = int(input("Enter a team size that is divisible by amount of players: "))
    num_teams = len(players) // team_size
    print(f"With {len(players)} players, {num_teams} team{'s' if num_teams > 1 else ''} of {team_size} will be generated.")
    for _ in range(100):
        shuffle(players)
    return [players[i::num_teams] for i in range(num_teams)]


def print_teams(teams):
    for i, t in enumerate(teams):
        print(f'Team {i+1}: ', end='')
        print(*t, sep=', ')


def main():
    total_players = get_players()
    teams = set_teams(total_players)
    print_teams(teams)


if __name__ == '__main__':
    main()
