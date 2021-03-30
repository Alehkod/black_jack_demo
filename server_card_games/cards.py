class Cards:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} {self.suit}'

    def __str__(self):
        return f'{self.suit}_{self.value}'