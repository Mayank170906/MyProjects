import requests
from bs4 import BeautifulSoup

# Request the webpage data
url = 'https://www.cricbuzz.com/api/html/cricket-scorecard/100238'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the match result
match_result = soup.find('div', class_='cb-scrcrd-status').text.strip()
print("Match Result:", match_result)

# Extract the first innings team name and score
innings_1 = soup.find('div', id='innings_1')
team_1_name = innings_1.find('span').text.strip()
team_1_score = innings_1.find('span', class_='pull-right').text.strip()

print(f"{team_1_name}: {team_1_score}")

# Extract players and their scores
players = innings_1.find_all('div', class_='cb-col cb-col-100 cb-scrd-itms')

for player in players:
    player_name = player.find('a').text.strip()
    dismissal_info = player.find('span', class_='text-gray').text.strip()
    
    # Extracting scores, using try-except to handle missing data
    try:
        runs = player.find_all('div', class_='cb-col-8 text-right text-bold')[0].text.strip()
    except IndexError:
        runs = "N/A"  # or 0 if you prefer

    try:
        balls = player.find_all('div', class_='cb-col-8 text-right')[0].text.strip()
    except IndexError:
        balls = "N/A"

    try:
        fours = player.find_all('div', class_='cb-col-8 text-right')[1].text.strip()
    except IndexError:
        fours = "N/A"

    try:
        sixes = player.find_all('div', class_='cb-col-8 text-right')[2].text.strip()
    except IndexError:
        sixes = "N/A"

    try:
        strike_rate = player.find_all('div', class_='cb-col-8 text-right')[3].text.strip()
    except IndexError:
        strike_rate = "N/A"

    print(f"{player_name} | {dismissal_info} | Runs: {runs} | Balls: {balls} | 4s: {fours} | 6s: {sixes} | SR: {strike_rate}")
