import socket

IP = "127.0.0.1"
PORT = 42069
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)
print("Server started")

while True:
    conn, addr = s.accept()
    if conn:
        print("Got connection from " + addr)
    data = conn.recv(2)
    print(data)

conn.close()