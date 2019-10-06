import socket

IP = "127.0.0.1"
PORT = 42069
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)

conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data)

conn.close()