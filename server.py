import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("[NEW CONNECTION] {0} connected.".format(addr))    #print(f"[NEW CONNECTION] {addr} connected.")        #Python 3


    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print("[{0}] {1}".format(addr,msg))        #print(f"[{addr}] {msg}")               #Python 3

    conn.close()


def start():
    server.listen(PORT)    #server.listen()     # pe Python 3 nu tb specificat si PORT
    print("[LISTENING] Server is listening on {0}".format(SERVER))      #print(f"[LISTENING] Server is listening on {SERVER}")           #Python 3
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print("\n[ACTIVE CONNECTIONS] {0}".format(threading.activeCount() -1))                #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")           #Python 3


print("[STARTING] server is starting...")
start()