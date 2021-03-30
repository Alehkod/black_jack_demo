import pygame
import socket
import json
import cards

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

    def create_game(self):
        pygame.init()

    def create_screen(self):
        self.screen = pygame.display.set_mode((1300, 700))
        pygame.display.set_caption(self.name_game)

    def create_interface(self):
        self.table_img = pygame.image.load('img/table_texture.jpg')
        sock.send('play'.encode("utf-8"))
        self.shared, self.player_cards_list, self.player_points, self.dealer_cards_list, self.dealer_points = json.loads(
            sock.recv(1024).decode('utf-8'))
        self.shared_cards = cards.SpriteCards(self.shared, 1100, 350, 2, open_cards=False).cards
        # self.player_cards = cards.SpriteCards(player_cards, 100, 550, 100).cards
        # self.dealer_cards = cards.SpriteCards(dealer_cards, 100, 100, 100).cards
        self.draw_button = cards.Button(550, 650, 'draw', black)
        self.pass_button = cards.Button(700, 650, 'Pass', black)
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
                    self.shared, self.player_cards_list, self.player_points, self.dealer_cards_list, self.dealer_points = json.loads(
                        sock.recv(1024).decode('utf-8'))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.draw_button.rect.collidepoint(*event.pos):
                        cmd = 'draw'
                        sock.send(cmd.encode("utf-8"))
                        self.shared, self.player_cards_list, self.player_points, self.dealer_cards_list, self.dealer_points = json.loads(
                            sock.recv(1024).decode('utf-8'))
                    elif self.pass_button.rect.collidepoint(*event.pos):
                        cmd = 'pass'
                        sock.send(cmd.encode("utf-8"))
                        self.shared, self.player_cards_list, self.player_points, self.dealer_cards_list, self.dealer_points = json.loads(
                            sock.recv(1024).decode('utf-8'))

            # shared, player_cards, player_pints, dealer_cards, dealer_points = json.loads(
            #     sock.recv(1024).decode('utf-8'))
            point_player_result = cards.Button(100, 650, f'{self.player_points} point', red, color_fon=None)
            point_dealer_result = cards.Button(100, 200, f'{self.dealer_points} point', red, color_fon=None)
            self.shared_cards = cards.SpriteCards(self.shared, 1100, 350, 2, open_cards=False).cards
            self.player_cards = cards.SpriteCards(self.player_cards_list, 100, 550, 100).cards
            self.dealer_cards = cards.SpriteCards(self.dealer_cards_list, 100, 100, 100).cards
            self.draw_button = cards.Button(550, 650, 'draw', black)
            self.pass_button = cards.Button(700, 650, 'Pass', black)
            menu_sprite = pygame.sprite.Group(self.draw_button, self.pass_button, point_player_result,
                                              point_dealer_result)
            self.shared_cards.update()
            self.player_cards.update()
            self.dealer_cards.update()
            pygame.display.update()

            self.screen.blit(self.table_img, (0, 0))
            menu_sprite.draw(self.screen)
            self.shared_cards.draw(self.screen)
            self.player_cards.draw(self.screen)
            self.dealer_cards.draw(self.screen)
            # sock.send(''.encode("utf-8"))
    def quit(self):
        pygame.quit()


black_jack = Game('Black_Jack')
black_jack.create_game()
black_jack.create_screen()
black_jack.create_interface()
black_jack.round_game()
black_jack.quit()
