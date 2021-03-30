import pygame
import os
import time
from deckCards import *
from player import *

# width = 1300
# height = 700
# fps = 30

# Задаем цвета
class Colors:
    def __init__(self, p_1, p_2, p_3):
        self.color = p_1, p_2, p_3

    def __str__(self):
        return f'{self.color}'


white = Colors(255, 255, 255).color
gray = Colors(127, 127, 127).color
black = Colors(0, 0, 0).color
red = Colors(255, 0, 0).color
green = Colors(0, 255, 0).color
blue = Colors(0, 0, 255).color
print(white)
# class Button:
# Класс ярлыков в игре:
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, text, color, color_fon=gray):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('AGENCYR.TTF', 24)
        self.image = self.font.render(text, True, color, color_fon)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


#   def create_sprite_button

# class Data(Button):
#     def count_points(*args):
#         point = 0
#         point_list = shared.dict_black_jack(*list(map(lambda card: card.value, args)))
#         point_list = sorted(point_list, key=lambda x: str(type(x)))
#         for i in point_list:
#             if type(i) == tuple and point + max(i) <= 21:
#                 point += max(i)
#             elif type(i) == tuple and point + max(i) >= 21:
#                 point += min(i)
#             else:
#                 point += i
#         return point

# class Round:
#   def fps
#   def event
#   def update
#   def rendering
# class Round_game(Round):
# class Round_menu(Round):

class Game:
    def __init__(self, name_game, fps):
        self.fps = fps
        self.name_game = name_game
        self.create_game()
        self.clock = pygame.time.Clock()
        self.screen = self.create_screen(1300, 700, self.name_game)

    def create_game(self):
        pygame.init()

    def create_screen(self, width, height, name_screen):
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name_screen)
        return screen

    # def game_quit


class Table(Game):
    def __init__(self, deck):
        Game.__init__(self, fps)
        self.shared_sprite = self.create_shared_deck(deck)

    def load_table_img(self):
        table_img = pygame.image.load('img/table_texture.jpg')

    def create_shared_deck(self, deck):
        shared = DeckCards52(1100, 350, step_cards=2, open_deck=False)
        shared.shuffle()
        return deck.sprite_deck(shared.deck_cards)

    def create_players_place(self):


def display():
    # Создаем игру и окно TODO
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Black Jack")
    table_img = pygame.image.load('img/table_texture.jpg')

    # Функцуия отображения карт в игре:
    def display_deck(*args):
        deck_sprite = pygame.sprite.Group()
        for cards in args:
            deck_sprite.add(cards)
        return deck_sprite

    # Создание общей коллоды и перекартовка:
    shared = DeckCards52(1100, 350, step_cards=2, open_deck=False)
    shared.shuffle()
    shared_sprite = display_deck(shared.deck_cards)

    # Расчитывает результат
    def count_points(*args):
        point = 0
        point_list = shared.dict_black_jack(*list(map(lambda card: card.value, args)))
        point_list = sorted(point_list, key=lambda x: str(type(x)))
        for i in point_list:
            if type(i) == tuple and point + max(i) <= 21:
                point += max(i)
            elif type(i) == tuple and point + max(i) >= 21:
                point += min(i)
            else:
                point += i
        return point

    # Создание места игрока с 2-мя картмаи:
    player = Player((100, 550), 100)
    x_player, y_player = player.pos_cards
    step_player = player.step_cards
    player_cards = shared.get_first_card(2)
    for card in player_cards:
        card.move_cards(x_player, y_player)
        x_player += step_player
    player_sprite = display_deck(player_cards)

    # Создание диллера:
    dealer = Player((100, 100), 'Dealer', 100)
    x_dealer, y_dealer = dealer.pos_cards
    step_dealer = dealer.step_cards
    dealer_cards = shared.get_first_card(2)
    for card in dealer_cards:
        card.move_cards(x_dealer, y_dealer)
        x_dealer += step_dealer
    dealer_cards[-1].open_card = False
    dealer_sprite = display_deck(dealer_cards)
    point_dealer = count_points(dealer_cards[0])

    # Создание спрайтов ярлыков:
    take_cards = Button(550, 650, 'Take', black)
    pass_move = Button(700, 650, 'Pass', black)

    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(fps)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Ярлык Take:
                if take_cards.rect.collidepoint(*event.pos):
                    player_cards.append(*shared.get_first_card(1))
                    player_cards[-1].move_cards(x_player, y_player)
                    x_player += step_player
                    player_sprite = display_deck(player_cards)
                    shared_sprite = display_deck(shared.deck_cards)
                # Ярлык Pass:
                elif pass_move.rect.collidepoint(*event.pos):
                    dealer_cards[-1].move_cards(x_dealer - step_dealer, y_dealer)
                    point_dealer = count_points(*dealer_cards)
                    while point_dealer <= 17:
                        clock.tick(2)
                        dealer_cards.append(*shared.get_first_card(1))
                        dealer_cards[-1].move_cards(x_dealer, y_dealer)
                        x_dealer += step_dealer
                        point_dealer = count_points(*dealer_cards)
                        dealer_sprite = display_deck(dealer_cards)
                        shared_sprite = display_deck(shared.deck_cards)
                        point_player = count_points(*player_cards)
                        point_player_result = Button(100, 650, f'{point_player} point', red, color_fon=None)
                        point_dealer_result = Button(100, 200, f'{point_dealer} point', red, color_fon=None)
                        menu_sprite = pygame.sprite.Group(take_cards, pass_move, point_player_result,
                                                          point_dealer_result)
                        # Обновление
                        shared_sprite.update()
                        player_sprite.update()
                        dealer_sprite.update()
                        pygame.display.update()

                        # Рендеринг
                        screen.blit(table_img, (0, 0))
                        menu_sprite.draw(screen)
                        shared_sprite.draw(screen)
                        player_sprite.draw(screen)
                        dealer_sprite.draw(screen)
        # Поправить очки
        point_player = count_points(*player_cards)
        point_player_result = Button(100, 650, f'{point_player} point', red, color_fon=None)
        point_dealer_result = Button(100, 200, f'{point_dealer} point', red, color_fon=None)
        menu_sprite = pygame.sprite.Group(take_cards, pass_move, point_player_result, point_dealer_result)
        # Обновление
        shared_sprite.update()
        player_sprite.update()
        dealer_sprite.update()
        pygame.display.update()

        # Рендеринг
        screen.blit(table_img, (0, 0))
        menu_sprite.draw(screen)
        shared_sprite.draw(screen)
        player_sprite.draw(screen)
        dealer_sprite.draw(screen)

    pygame.quit()


display()
