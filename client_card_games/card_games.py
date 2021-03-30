import socket
import json

sock = socket.socket()

sock.connect(('localhost', 10000))

while True:
    command = input()
    sock.send(command.encode("utf-8"))
    shared, player_cards, player_pints, dealer_cards, dealer_points = json.loads(sock.recv(1024).decode('utf-8'))
    print(shared)
    if command == 'quit':
        sock.close()
        break
