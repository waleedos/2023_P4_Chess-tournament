# fichier main.py

from src.views.homepage import HomepageView
from src.views.player import PlayerView

def main():
    homepage_view = HomepageView()
    player_view = PlayerView()

    while True:
        choice = homepage_view.menu()

        if choice == "1":
            while True:
                player_choice = player_view.menu("Player menu")

                if player_choice == "1":  # Lister les joueurs
                    # Traiter l'affichage de la liste des joueurs
                    pass
                elif player_choice == "2":  # Sélectionner un joueur
                    # Traiter la sélection d'un joueur
                    pass
                elif player_choice == "3":  # Créer un joueur
                    player_data = player_view.add_player()
                    # Traiter l'ajout du joueur avec les données player_data
                    print("Player added:", player_data)
                elif player_choice == "4":  # Modifier un joueur
                    # Traiter la modification d'un joueur
                    pass
                elif player_choice == "5":  # Supprimer un joueur
                    # Traiter la suppression d'un joueur
                    pass
                elif player_choice == "6":  # Retourner au menu principal
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "2":
            # Traiter le choix du menu Tournament
            pass
        elif choice == "3":
            # Traiter le choix du menu Report
            pass
        elif choice == "4":
            # Quitter l'application
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
