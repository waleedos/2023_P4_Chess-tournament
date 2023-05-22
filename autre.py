from .common import top_bottom, get_choice, menu

class PlayerView:
    @top_bottom
    def menu(self, preview: str) -> str:
        """display the player menu and get the choice"""

        print("\n                              Player menu\n")
        menu(preview)
        print("                              7 -- Back to Home Menu\n")

        return get_choice()

    def add_player(self):
        """get the player's data"""

        print("\nPlease enter the player's values:\n")

        first_name = input("First name: ")
        last_name = input("Last name: ")
        birth_date = input("Birth date (YYYY-MM-DD): ")

        return [first_name, last_name, birth_date]