import socket
import threading

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8002

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

clients = []


def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)


def handle_client(client_socket, client_addr):
    clients.append(client_socket)
    while True:
        msg = client_socket.recv(4096)
        broadcast(msg, client_socket)


while True:
    client_socket, client_addr = server_socket.accept()
    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_addr)
    )