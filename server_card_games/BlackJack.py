import deckCards
import player
import json
import socket


class Game:
    def __init__(self):
        self.shared = deckCards.DeckCards52()
        self.player = player.Player()
        self.dealer = player.Player('Dealer')

    def play_button(self):
        self.shared.shuffle()
        self.player.get_first_card(self.shared, 2)
        self.dealer.get_first_card(self.shared, 1)

    def pass_button(self):
        while self.dealer.point <= 17:
            self.dealer.get_first_card(self.shared, 1)

    def draw_button(self):
        self.player.get_first_card(self.shared, 1)

    def quit_button(self):
        print("I'm UPAL!")
        return False


def parse_message(message):
    return json.loads(message)


sock = socket.socket()
sock.bind(('', 10000))
sock.listen(1)
print("Start Listen")
conn, addr = sock.accept()
print("====================================Connection=======================================")

black_jack = Game()


def convert():
    data = json.dumps((str(black_jack.shared.deck_cards),
                       str(black_jack.player.card_list),
                       black_jack.player.point,
                       str(black_jack.dealer.card_list),
                       black_jack.dealer.point,
                       )).encode('utf-8')
    return data


while True:

    client_cmd = conn.recv(1024).decode("utf-8")
    if client_cmd == 'quit':
        print('quit')
        black_jack.quit_button()
        conn.send(convert())
        break
    elif client_cmd == 'play':
        print('play')
        black_jack.play_button()
        conn.send(convert())
    elif client_cmd == 'draw':
        print('draw')
        black_jack.draw_button()
        conn.send(convert())
    elif client_cmd == 'pass':
        print('pass')
        black_jack.pass_button()
        conn.send(convert())
    else:
        conn.send(convert())

conn.close()
