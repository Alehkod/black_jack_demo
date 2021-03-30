from cards import *
import random
import pygame


class DeckCards(pygame.sprite.Sprite):
    def __init__(self, value_list, suits_dict, x_deck=0, y_deck=0, step_cards=5, open_deck=True):
        pygame.sprite.Sprite.__init__(self)
        self.value_list = value_list
        self.suits_dict = suits_dict
        self.x_deck = x_deck
        self.y_deck = y_deck
        self.step = step_cards
        self.open_deck = open_deck
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
        self.x_deck = self.__copy_x
        self.__gen_cord()

    def __generate_deck(self):
        self.deck_cards = []
        self.__copy_x = self.x_deck
        for value in self.value_list:
            for suit in self.suits_dict:
                yield Cards(value, suit, self.x_deck, self.y_deck, self.open_deck)
                self.x_deck += self.step

    def __gen_cord(self):
        for card in self.deck_cards:
            card.x = self.x_deck
            self.x_deck += self.step

    def move_deck(self, x, y, step=5, open_deck=True):
        self.x_deck, self.y_deck = x, y
        self.open_deck = open_deck
        self.step = step

    def sprite_deck(self, *args):
        deck_sprite = pygame.sprite.Group()
        for cards in args:
            deck_sprite.add(cards)
        return deck_sprite


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

    def __init__(self, x=0, y=0, step_cards=5, open_deck=True):
        DeckCards.__init__(self, self.__value_list, self.__suits_list, x, y, step_cards, open_deck)


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

    def __init__(self, x=0, y=0, step_cards=5, open_deck=True):
        DeckCards.__init__(self, self.__value_list, self.__suits_list, x, y, step_cards, open_deck)
