import player


class WorldPlayers:

    def __init__(self):
        self.players = [player.Player(3,5)]
  
    def __str__(self):
        string = ""
        for single_cell in cells:
            string.append(single_cell)
        return cells[0]

    def get_serializable(self):
        serializable_data = []
        for single_player in self.players:
            serializable_data.append(single_player.get_serializable())
        return serializable_data
