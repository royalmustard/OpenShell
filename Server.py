import socket
import MemiumError


class Server:

    def __init__(self, port):
        self.PORT = port
        self.IP = "127.0.0.1"
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.IP, self.PORT))
        self.s.listen(1)
        self.conn = None
        print("Server started")
        self.commandlist = {}

    def add_command(self, creq, overwrite=False):
        commandname = creq.commandname.lower()
        if commandname in self.commandlist.keys() and not overwrite:
            raise MemiumError.CommandAlreadyExistsError
        self.commandlist[commandname] = creq.process

    def execute_command(self, commandname, args):
        if commandname not in self.commandlist.keys():
            print(f"{commandname} does not exist!")
            return
        res = self.commandlist[commandname](args)
        lres = str(len(res)).rjust(4, "0")
        header = f"len:{lres}"
        print("Sending header: " + header)
        self.conn.send(header.encode("utf-8"))
        ack = self.conn.recv(4)
        print(str(ack))
        if ack.decode("utf-8") == "true":
            print("Sending content: " + str(res))
            self.conn.send(res)

    def mainloop(self):
        self.conn, addr = self.s.accept()
        if self.conn:
            print("Got connection from " + addr[0])
        while True:
            data = self.conn.recv(1024)
            data = data.decode("utf-8")
            print("Recieved: "+data)
            data = data.split(" ")
            commandname = data[0]
            args = data[1:]
            self.execute_command(commandname, args)








