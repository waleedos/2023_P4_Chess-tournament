# fichier /src/views/tournament.py

from .common import top_bottom, get_choice, menu
from .player import PlayerView
from src.models.match import Matchs

class TournamentView:
    @top_bottom
    def menu(self, preview: str) -> str:
        """display the tournament menu and get the choice"""

        print("\n                              Tournament Menu\n")
        menu(preview)
        print("                              *tournament name must be unique")
        print("                              *tournament name is deletable but not editable\n")

        return get_choice()

    def list_tournaments(self, tournaments_list: list, action: str):
        """display the tournaments list created in the system"""

        if len(tournaments_list) == 0:
            print(f"\n0 tournaments {action} in the system.\n")
        elif len(tournaments_list) == 1:
            print(f"\n1 tournament {action} in the system:\n")
        else:
            print(f"\n{len(tournaments_list)} tournaments {action} in the system:\n")

        if len(tournaments_list) > 0:
            print(" Tournament name      | Place           | Status          | Start Date       | End Date")
            print("______________________|_________________|_________________|_________________|_________________")
            for t in tournaments_list:
                name = t["name"].ljust(20, " ")
                place = t["place"].ljust(15, " ")
                status = t["status"].ljust(15, " ")
                start_date = t["start_date"].ljust(15, " ")
                end_date = t["end_date"].ljust(15, " ")
                print(f" {name} | {place} | {status} | {start_date} | {end_date}")
            print()

    def create(self) -> list:
        """get the tournament's data"""

        print("\nTournament name* must be unique.\n")
        print("Please enter the tournament's values now:\n")

        response1 = self._get_name()
        response2 = self._get_place()
        response3 = self._get_description()

        return [response1, response2, response3]

    def create_response(self, response1: bool, response2: bool):
        """display a response after creating a tournament"""

        if response1 and response2:
            print("\n🟢 Tournament created successfully!\n")
        elif response1 and not response2:
            print("\n🛑🚫 A minimum of 4 valid player ines is required to create a tournament.\n")
            print("Please retry with correct values.\n")
        elif not response1 and not response2:
            print("\n🛑🚫 The tournament name is not unique!\n")
            print("Please try again with a different tournament name.\n")

    def list_players(self, players_list: list):
        """display the list of players"""

        PlayerView().list_players(players_list, "registered", "system")

    def add_players(self, number_of_players: int):
        """get the players' ines"""

        return [input(f"Player {i+1}'s ine > ") for i in range(number_of_players)]

    def add_players_response(
        self, response1: bool, response2: bool, added_players: int, players_to_add: int
    ):
        """display a response after adding players to a tournament"""

        if response1 and response2:
            print(f"\n🟢 {added_players}/{players_to_add} players added successfully!\n")
        elif response1 and not response2:
            if added_players > 0:
                print(f"\n🛑🚫 Only {added_players}/{players_to_add} players added successfully!\n")
            else:
                print(f"\n🛑🚫 0/{players_to_add} players added...\n")
            print("Please check the players' ines that haven't been added.\n")
            print("All players' ines must exist in the system before they can be added to a tournament.\n")
        elif not response1:
            self._inexistent_tournament()

    def edit(self) -> list:
        """get the tournament's new values to edit"""

        print("\nWhich tournament would you like to edit?\n")
        response1 = self._get_name()
        print("\nPlease enter the tournament's new values now:\n")
        response2 = self._get_place()
        response3 = self._get_description()

        return [response1, response2, response3]

    def edit_response(self, response: bool):
        """display a response after editing a tournament"""

        if response:
            print("\n🟢 Tournament edited successfully!\n")
        else:
            self._inexistent_tournament()

    def delete(self) -> str:
        """get the tournament's name to delete"""

        print("\nWhich tournament would you like to delete?\n")
        print("🟠 The tournament's data will be permanently lost...\n")

        return self._get_name()

    def delete_response(self):
        """display a response after deleting a tournament"""

        print("\n🟢 Tournament deleted successfully!\n")

    def select(self) -> str:
        """get the tournament's name to select"""

        print("\nThe tournament must be created in the system.\n")
        print("\nWhich tournament would you like to select?\n")

        return self._get_name()

    def select_response(self, tournament_data: list, player_ranking: list):
        """display a response after selecting a tournament"""

        self._select_view1(tournament_data)
        self._select_view2(player_ranking)

    def select_end(self, tournament_data: list, player_ranking: list):
        """display the tournament's data when it has concluded"""

        self._select_view1(tournament_data)

        for i, p in enumerate(player_ranking):
            rank = str(i+1).ljust(5, " ")
            last_name = p["last_name"].ljust(15, " ")
            score = str(p["score"]).ljust(5, " ")
            print(f" {rank} | {last_name} | {score}")
        print()

    def select_match(self, tournament_data: list, player_ranking: list, match_list: list) -> str:
        """display the tournament's data when a match is selected"""

        self._select_view1(tournament_data)
        self._select_view2(player_ranking)

        for i, match in enumerate(match_list):
            print(Matchs(i+1, match))

        print("\nWould you like to enter the result of a match?\n")

        return self._get_user_choice()

    def select_result(self) -> list:
        """get the match result"""

        print("\nThe winner gets 1 point, the loser gets 0 points,")
        print("and both players get 0.5 points if they draw.")
        print("\nFor which match would you like to enter the result?\n")

        response1 = input("\nThe match number (e.g., 1) > ")
        response2 = input("The score of the player in white (e.g., 1) > ")
        response3 = input("The score of the player in black (e.g., 0) > ")

        return [response1, response2, response3]

    def select_result_response(self, response1: bool, response2: bool):
        """display a response after entering a match result"""

        if response1 and response2:
            print("\n🟢 Match updated successfully!\n")
        elif response1 and not response2:
            print("\n🛑🚫 Invalid result entered!\n")
            print("Please try again with a valid result.\n")
        elif not response1:
            print("\n🛑🚫 Invalid match number!\n")
            print("Please try again with a valid match number.\n")

    def _get_name(self) -> str:
        """get the tournament's name"""

        return input("Tournament name* > ")

    def _get_place(self) -> str:
        """get the tournament's place"""

        return input("Tournament place > ")

    def _get_description(self) -> str:
        """get the tournament's description"""

        return input("Tournament description > ")

    def _get_user_choice(self) -> str:
        """get the user's choice"""

        return input("Enter your choice (y/n) > ")

    def _inexistent_tournament(self):
        """display a message if the tournament doesn't exist"""

        print("\n🛑🚫 This tournament name does not exist in the system!\n")
        print("Please try again with a registered tournament name.\n")

    def _select_view1(self, tournament_data: list):
        """display the tournament's data when it is selected"""

        print()
        print("-" * 80)
        print("\n _______________________________________________________________")
        print("| Tournament name           | Status      | Current round |")
        print("|___________________________|_____________|________________|")
        print("|                           |             |                |")
        name = tournament_data[0].ljust(27, " ")
        status = tournament_data[1].ljust(13, " ")
        current_round = tournament_data[2].ljust(15, " ")

        print(f"| {name} | {status} | {current_round} |")
        print("|___________________________|_____________|________________|\n")

    def _select_view2(self, player_ranking: list):
        """display the tournament's players when it is selected"""

        if len(player_ranking) > 0:
            for i, p in enumerate(player_ranking):
                rank = str(i+1).ljust(5, " ")
                last_name = p["last_name"].ljust(15, " ")
                score = str(p["score"]).ljust(5, " ")
                print(f" {rank} | {last_name} | {score}")
            print()
