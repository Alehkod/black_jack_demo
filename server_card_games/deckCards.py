from cards import *
import random


class DeckCards:
    def __init__(self, value_list, suits_dict):

        self.value_list = value_list
        self.suits_dict = suits_dict
        self.deck_cards = list(self.__generate_deck())

    def get_random_card(self):
        i = self.deck_cards.index(random.choice(self.deck_cards))
        return self.deck_cards.pop(i)

    def get_first_card(self, number=1):
        deck_card = []
        for i in range(number):
            get_card = self.deck_cards.pop(-1)
            deck_card.append(get_card)
        return deck_card

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def __generate_deck(self):
        self.deck_cards = []
        for value in self.value_list:
            for suit in self.suits_dict:
                yield Cards(value, suit)


class DeckCards52(DeckCards):
    __suits_list = [
        'heart',
        'diamond',
        'club',
        'spade',
    ]
    __value_list = [
        '2', '3', '4', '5',
        '6', '7', '8', '9', '10',
        'J', 'Q', 'K', 'A'
    ]

    def __init__(self):
        DeckCards.__init__(self, self.__value_list, self.__suits_list)


class DeckCards36(DeckCards):
    __suits_list = [
        'heart',
        'diamond',
        'club',
        'spade',
    ]
    __value_list = [
        '6', '7', '8', '9', '10',
        'J', 'Q', 'K', 'A'
    ]

    def __init__(self):
        DeckCards.__init__(self, self.__value_list, self.__suits_list)
