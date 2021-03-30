import points
import random

name_list = ['Alex', 'Anthony', 'Brandon', 'Christopher', 'David', 'Dillon', 'Ethan', 'Fred', 'Josh',
             'Justin', 'Kevin', 'Ryan', 'Thomas', 'Tyler', 'William']


class Player:
    def __init__(self, name=random.choice(name_list), ):
        self.name = name
        self.card_list = []
        self.point = 0

    def get_first_card(self, deck_cards, n):
        for i in range(n):
            self.card_list.append(*deck_cards.get_first_card(1))
        self.point = points.Points(self.card_list).point