import pyperclip
import socket
import threading

SERVER_HOST = "120.79.33.119"
SERVER_PORT = 8002

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))


def recv():
    while (True):
        msg = client_socket.recv(4096)
        print("RECV:", msg)
        pyperclip.copy(msg)


recv_thread = threading.Thread(target=recv)
recv_thread.start()

while True:
    content = pyperclip.waitForNewPaste()
    client_socket.send(msg.encode("utf-8"))
