# fichier main.py

from src.views.homepage import HomepageView

def main():
    homepage_view = HomepageView()

    while True:
        choice = homepage_view.menu()

        if choice == "1":
            # Traiter le choix du menu Player
            pass
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
