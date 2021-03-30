import pygame
import socket
import json
import cards
import player

sock = socket.socket()

sock.connect(('localhost', 10000))


class Colors:
    def __init__(self, p_1, p_2, p_3):
        self.color = p_1, p_2, p_3


white = Colors(255, 255, 255).color
gray = Colors(127, 127, 127).color
black = Colors(0, 0, 0).color
red = Colors(255, 0, 0).color
green = Colors(0, 255, 0).color
blue = Colors(0, 0, 255).color


class Game:
    def __init__(self, name_game):
        self.name_game = name_game
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1300, 700))
        self.table_img = pygame.image.load('img/table_texture.jpg')
        self.__shared = []
        self.__player_cards_list = []
        self.__player_points = 0
        self.__dealer_cards_list = []
        self.__dealer_points = 0
        self.player = player.Player(self.__player_cards_list, self.__player_points, (650, 500), 'Oleg')
        self.dealer = player.Player(self.__dealer_cards_list, self.__dealer_points, (100, 500), 'Dealer')
        self.shared_cards = cards.SpriteCards(self.__shared, 1100, 350, 2, open_cards=False).cards

    @staticmethod
    def create_game():
        pygame.init()

    def create_screen(self):
        pygame.display.set_caption(self.name_game)

    def play_game(self):
        sock.send('play'.encode("utf-8"))
        self.__receive_serv()
        self.draw_button = cards.Button(550, 650, 'Draw', black)
        self.pass_button = cards.Button(700, 650, 'Pass', black)

    def __receive_serv(self):
        self.__shared, self.__player_cards_list, self.__player_points, \
        self.__dealer_cards_list, self.__dealer_points = json.loads(sock.recv(1024).decode('utf-8'))

    def round_game(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
                    cmd = 'quit'
                    sock.send(cmd.encode("utf-8"))
                    self.__receive_serv()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.draw_button.rect.collidepoint(*event.pos):
                        cmd = 'draw'
                        sock.send(cmd.encode("utf-8"))
                        self.__receive_serv()
                    elif self.pass_button.rect.collidepoint(*event.pos):
                        cmd = 'pass'
                        sock.send(cmd.encode("utf-8"))
                        self.__receive_serv()

            sprite_point_player = cards.Button(100, 650, f'{self.player.point} point', red, color_fon=None)
            sprite_point_dealer = cards.Button(100, 200, f'{self.dealer.point} point', red, color_fon=None)
            menu_sprite = pygame.sprite.Group(self.draw_button, self.pass_button, sprite_point_dealer,
                                              sprite_point_player)

            self.player.list_cards_upp(self.__player_cards_list)
            self.dealer.list_cards_upp(self.__dealer_cards_list)
            self.shared_cards.update()
            # self.player.sprite_cards.update()
            # self.dealer.sprite_cards.update()
            pygame.display.update()

            self.screen.blit(self.table_img, (0, 0))
            menu_sprite.draw(self.screen)
            self.shared_cards.draw(self.screen)
            self.player.sprite_cards.draw(self.screen)
            self.dealer.sprite_cards.draw(self.screen)

    def quit(self):
        pygame.quit()


black_jack = Game('Black_Jack')
black_jack.create_game()
black_jack.create_screen()
black_jack.play_game()
black_jack.round_game()
black_jack.quit()
