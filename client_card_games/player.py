import cards
import random
import pygame

name_list = ['Alex', 'Anthony', 'Brandon', 'Christopher', 'David', 'Dillon', 'Ethan', 'Fred', 'Josh',
             'Justin', 'Kevin', 'Ryan', 'Thomas', 'Tyler', 'William']


class Player(pygame.sprite.Sprite):
    def __init__(self, list_cards, point, pos_cards, name=random.choice(name_list), step_cards=100):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.point = point
        self.__list_cards = list_cards
        self.__pos_cards = pos_cards
        self.__step_cards = step_cards
        self.sprite_cards = self.__sprite_cards()

    def __sprite_cards(self):
        return cards.SpriteCards(self.__list_cards, self.point, *self.__pos_cards, open_cards=True).cards

    def list_cards_upp(self, args):
        self.__list_cards = args
        self.sprite_cards = self.__sprite_cards()
        self.sprite_cards.update()
