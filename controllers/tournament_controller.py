import json
from models.tournament import Tournament
from views.tournament_view import display_all_tournaments, display_tournament_creation_success, get_new_tournament_info
from controllers.player_controller import load_players
from models.player import Player  # Ajout de l'import de la classe Player


def load_tournaments():
    try:
        with open('data/tournaments.json', 'r') as file:
            tournaments_data = json.load(file)
            if "tournaments" in tournaments_data and isinstance(tournaments_data["tournaments"], list):
                return [Tournament(**tournament_info) for tournament_info in tournaments_data["tournaments"]]
            else:
                return []
    except FileNotFoundError:
        return []


def save_tournaments(tournaments):
    data = {"tournaments": [tournament.to_dict() for tournament in tournaments]}
    with open('data/tournaments.json', 'w') as file:
        json.dump(data, file, indent=4)


def add_tournament(tournament):
    tournaments = load_tournaments()
    tournaments.append(tournament)
    save_tournaments(tournaments)
    display_tournament_creation_success(tournament)  # Afficher la phrase de confirmation


def create_new_tournament():
    tournament_data = get_new_tournament_info()
    # Change 'rounds' to 'number_of_rounds'
    if 'rounds' in tournament_data:
        tournament_data['number_of_rounds'] = tournament_data.pop('rounds')
    tournament = Tournament(**tournament_data)
    add_tournament(tournament)
    return tournament


def add_players_to_tournament():
    tournaments = load_tournaments()
    display_all_tournaments(tournaments)
    if tournaments:
        tournament_index = int(input("\nSélectionnez l'index du tournoi auquel vous souhaitez ajouter des joueurs : ")) - 1
        if 0 <= tournament_index < len(tournaments):
            tournament = tournaments[tournament_index]
            players = load_players()
            tournament.add_players(players)
            save_tournaments(tournaments)
            print("Les joueurs ont été ajoutés au tournoi avec succès.")
        else:
            print("Index de tournoi invalide.")
    else:
        print("Aucun tournoi enregistré.")


def select_tournament():
    tournaments = load_tournaments()
    display_all_tournaments(tournaments)
    tournament_index = int(input("Sélectionnez l'index du tournoi auquel vous souhaitez ajouter des joueurs : "))
    if tournament_index >= 0 and tournament_index < len(tournaments):
        return tournaments[tournament_index]
    else:
        print("Index de tournoi invalide.")
        return None
