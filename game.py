from carddeck import Deck

class Game:
    def __init__(self, id=None):
        print("Game init")
        self.deck = Deck()
        self.ready = False

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False