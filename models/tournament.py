# Fichier : /models/tournament.py
from models.player import Player
class Tournament:
    def __init__(self, name, location, start_date, end_date, description, time_control, number_of_rounds, players=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.number_of_rounds = number_of_rounds
        self.players = players if players else []


    def add_players(self, players):
        for player in players:
            if isinstance(player, Player):
                self.players.append(player)
            else:
                raise TypeError("Only Player objects can be added to the tournament.")


    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "number_of_rounds": self.number_of_rounds,
            "players": [player.ChessId for player in self.players],
        }
