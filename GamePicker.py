import requests
import random

api_key = input('Enter your Steam API key: ')
accounts_num = int(input('Enter the number of accounts: '))
accounts_games_data = {}

for i in range(accounts_num):
    steam_id = input(f'Enter the SteamID64 of user {i + 1}: ')
    url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json'
    
    try:
        # Make the request to the Steam API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        games_data = response.json()
        appids = [game.get('appid') for game in games_data.get('response', {}).get('games', [])]
        # Store the games data in the dictionary with the steam_id as the key
        accounts_games_data[steam_id] = appids

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data for Steam ID {steam_id}: {e}")

if accounts_games_data:
    # Get the intersection of all appid lists to find common games
    common_appids = set(accounts_games_data[next(iter(accounts_games_data))])  # Start with the first account's appids

    for appid_list in accounts_games_data.values():
        common_appids.intersection_update(appid_list)  # Find intersection with each subsequent account's appids
    # Convert the set to a list
    common_appids = list(common_appids)

n = len(common_appids)
how_many = int(input(f'There are {n} common games. How many do you want to choose from? '))

if how_many > n:
    raise ValueError(f'You cannot choose more than {n} games.')
for game in range(how_many):
    g = random.randint(0, n - 1)
    print(f'https://store.steampowered.com/app/{common_appids[g]}')

x = input('Press Enter to exit . . . \n')
if x == '':
    exit()