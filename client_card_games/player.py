import deckCards
import random

name_list = ['Alex', 'Anthony', 'Brandon', 'Christopher', 'David', 'Dillon', 'Ethan', 'Fred', 'Josh',
             'Justin', 'Kevin', 'Ryan', 'Thomas', 'Tyler', 'William']


class Player:
    def __init__(self, list_cards, point, pos_cards, name=random.choice(name_list), step_cards=100):
        self.name = name
        self.point = point
        self.card_list = list_cards
        self.pos_cards = pos_cards
        self.step_cards = step_cards
