import pandas as pd

class CricketTeamSelection:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.players_data = pd.read_excel(self.excel_file)

    def display_player_numbers(self):
        """Display players with corresponding numbers for easy selection."""
        print("\nAvailable Players:")
        for idx, player in enumerate(self.players_data['PlayerName'], start=1):
            print(f"{idx}. {player}")

    def select_team(self, team_name):
        """Allows a user to select 11 players for their team by entering numbers."""
        selected_players = []
        print(f"\n{team_name}: Select 11 players by entering the player numbers from the list below.")
        self.display_player_numbers()

        while len(selected_players) < 11:
            try:
                player_num = int(input(f"Select player {len(selected_players)+1} for {team_name} (1-22): "))
                if 1 <= player_num <= 22:
                    player_name = self.players_data['PlayerName'].iloc[player_num - 1]
                    if player_name not in selected_players:
                        selected_players.append(player_name)
                        print(f"{player_name} added to {team_name}.")
                    else:
                        print("Player already selected. Choose a different player.")
                else:
                    print("Invalid number. Enter a number between 1 and 22.")
            except ValueError:
                print("Please enter a valid number.")

        return selected_players

    def calculate_team_score(self, team_players):
        """Calculate the team score based on players' stats."""
        team_stats = self.players_data[self.players_data['PlayerName'].isin(team_players)]
        total_runs = team_stats['Runs'].sum()
        total_wickets = team_stats['Wickets'].sum()
        
        return total_runs + (total_wickets * 25)

    def compare_teams(self, team1, team2):
        """Compare two teams and declare the winner based on total scores."""
        team1_score = self.calculate_team_score(team1)
        team2_score = self.calculate_team_score(team2)

        print("\nTeam 1 Players:", team1)
        print("Team 2 Players:", team2)

        print(f"\nTeam 1 Score: {team1_score}")
        print(f"Team 2 Score: {team2_score}")

        if team1_score > team2_score:
            print("\nTeam 1 wins!")
        elif team2_score > team1_score:
            print("\nTeam 2 wins!")
        else:
            print("\nIt's a tie!")

# Usage
match = CricketTeamSelection("csk_vs_mi_2024_match.xlsx")
team1 = match.select_team("Team 1")
team2 = match.select_team("Team 2")
match.compare_teams(team1, team2)
