import socket

def connect_to_ids(host='129.21.127.87', port=5555):
    sock = socket.socket()
    sock.connect((host, port))
    print("Sending query to IDS...")
    message = input("->")
    while message != 'q':
        message1 = bytearray(message, "ascii")
        sock.send(message1)
        message = input("->")
    sock.close()


def main():

    connect_to_ids()

if __name__ == '__main__':
    main()