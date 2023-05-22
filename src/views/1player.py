# fichier /src/views/player.py

from .common import top_bottom, get_choice, menu
from tabulate import tabulate
from colorama import Fore, Style

class PlayerView:
    @top_bottom
    def menu(self, preview: str) -> str:
        """display the player menu and get the choice"""

        print("\n                              Player menu\n")
        menu(preview)

        return get_choice()

    def list_players(self, players_list: list, action: str, location: str):
        """display the list of players"""

        if len(players_list) == 0:
            print(f"\n 0 player {action} in the {location}.\n")
        elif len(players_list) == 1:
            print(f"\n 1 player {action} in the {location}:\n")
        else:
            print(f"\n {len(players_list)} players {action} in the {location}:\n")

        if len(players_list) > 0:
            headers = [Fore.GREEN + "Player ID" + Style.RESET_ALL, Fore.GREEN + "First Name" + Style.RESET_ALL, Fore.GREEN + "Last Name" + Style.RESET_ALL, Fore.GREEN + "Birth Date" + Style.RESET_ALL]
            data = []

            for player in players_list:
                player_id = player["id"].ljust(15, " ")
                first_name = player["first_name"].ljust(15, " ")
                last_name = player["last_name"].ljust(15, " ")
                birth_date = player["birth_date"].ljust(15, " ")

                data.append([player_id, first_name, last_name, birth_date])

            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
            print()

    def add_player(self):
        """get the player's data"""

        print("\nPlease enter the player's values:\n")

        first_name = input("First name: ")
        last_name = input("Last name: ")
        birth_date = input("Birth date (dd/mm/yyyy): ")
        chess_id = input("Chess ID (e.g., AB12345): ")

        player_data = [
            [Fore.GREEN + "Field" + Style.RESET_ALL, Fore.GREEN + "Value" + Style.RESET_ALL],
            ["First Name", first_name],
            ["Last Name", last_name],
            ["Birth Date", birth_date],
            ["Chess ID", chess_id]
        ]

        print("\nPlayer added:")
        print(tabulate(player_data, tablefmt="fancy_grid"))

        return [first_name, last_name, birth_date, chess_id]

    def add_response(self, response: bool):
        """display response after adding a player"""

        if response:
            print("\nPlayer added successfully!\n")
        else:
            print("\nFailed to add player. Please try again.\n")

    def select(self):
        """get the player ID"""

        return input("Player ID > ")

    def select_response(self, player_data: list):
        """display the selected player's data"""

        if player_data:
            headers = [Fore.GREEN + "Field" + Style.RESET_ALL, Fore.GREEN + "Value" + Style.RESET_ALL]
            print("\nSelected player:")
            print(tabulate(player_data, headers=headers, tablefmt="fancy_grid"))
            print()
        else:
            print("\nPlayer not found. Please try again.\n")

    def edit_player(self):
        """get the player's new data to edit"""

        print("\nPlease enter the player's new values:\n")

        player_id = input("Player ID: ")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        birth_date = input("Birth date (dd/mm/yyyy): ")
        chess_id = input("Chess ID (e.g., AB12345): ")

        return [player_id, first_name, last_name, birth_date, chess_id]

    def edit_response(self, response: bool):
        """display response after editing a player"""

        if response:
            print("\nPlayer edited successfully!\n")
        else:
            print("\nFailed to edit player. Please try again.\n")

    def delete(self):
        """get the player ID to delete"""

        return input("Player ID to delete > ")

    def delete_response(self, response: bool):
        """display response after deleting a player"""

        if response:
            print("\nPlayer deleted successfully!\n")
        else:
            print("\nFailed to delete player. Please try again.\n")
