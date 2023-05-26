from colorama import Fore, Style
from tabulate import tabulate


def get_new_tournament_info():
    name = input("Nom du tournoi : ")
    location = input("Lieu du tournoi : ")
    description = input("Description du tournoi : ")
    start_date = input("Début du tournoi (jj/mm/aaaa) : ")
    end_date = input("Fin du tournoi (jj/mm/aaaa) : ")
    time_control = int(input("Contrôle du temps (1=bullet, 2=blitz, 3=coup rapide) : "))
    change_rounds = input("Voulez-vous changer le nombre de tours (4 par défaut) ? (O/N) : ")

    if change_rounds.lower() == "o":
        rounds = int(input("Entrez le nombre de tours : "))
    else:
        rounds = 4

    tournament_data = {
        "name": name,
        "location": location,
        "description": description,
        "start_date": start_date,
        "end_date": end_date,
        "time_control": time_control,
        "rounds": rounds,
        "players": [],  # Initialiser la liste des joueurs à vide
    }

    return tournament_data


def display_all_tournaments(tournaments):
    if tournaments:
        headers = [
            "Nom",
            "Lieu",
            "Début du tournoi",
            "Fin du tournoi",
            "Description",
            "Contrôle du temps",
            "Nombre de tours",
            "Joueurs participants",
        ]
        tournament_data = []
        for tournament in tournaments:
            tournament_row = [
                tournament.name,
                tournament.location,
                tournament.start_date,
                tournament.end_date,
                tournament.description,
                tournament.time_control,
                tournament.rounds,
                ", ".join(tournament.players),
            ]
            tournament_data.append(tournament_row)

        print(Fore.GREEN + tabulate(tournament_data, headers=headers, tablefmt="fancy_grid"))
        print(Fore.RED + "\nVoici tous les tournois enregistrés!" + "\n\n" + Style.RESET_ALL)
    else:
        print("Aucun tournoi enregistré.")
