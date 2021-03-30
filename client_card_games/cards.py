import pygame


class Colors:
    def __init__(self, p_1, p_2, p_3):
        self.color = p_1, p_2, p_3


white = Colors(255, 255, 255).color
gray = Colors(127, 127, 127).color
black = Colors(0, 0, 0).color
red = Colors(255, 0, 0).color
green = Colors(0, 255, 0).color
blue = Colors(0, 0, 255).color


class Cards(pygame.sprite.Sprite):

    def __init__(self, card, x, y, open_card=True):
        pygame.sprite.Sprite.__init__(self)
        self.card = card
        self.__image = str(f'{self.card}.png')
        self.open_card = open_card
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    @property
    def image(self):
        if self.open_card:
            return pygame.image.load(f'img/{self.card}.png')
        else:
            return pygame.image.load('img/back4.png')

    def move_cards(self, x, y, open_card=True):
        self.x, self.y = x, y
        self.open_card = open_card


class SpriteCards(pygame.sprite.Sprite):
    def __init__(self, list_cards, x_0, y_0, step=100, open_cards=True):
        pygame.sprite.Sprite.__init__(self)
        self.__list_cards = list_cards
        self.x_0 = x_0
        self.y_0 = y_0
        self.step = step
        self.open_cards = open_cards
        self.cards = self.__sprite_cards()

    def __sprite_cards(self):
        deck_sprite = pygame.sprite.Group()
        x = self.x_0
        for cards in self.__list_cards:
            deck_sprite.add(Cards(cards, x, self.y_0, self.open_cards))
            x += self.step
        return deck_sprite


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, text, color, color_fon=gray):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('AGENCYR.TTF', 24)
        self.image = self.font.render(text, True, color, color_fon)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
