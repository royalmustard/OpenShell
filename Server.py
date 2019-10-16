import socket
import MemiumError


class Server:

    def __init__(self, port):
        self.PORT = port
        self.IP = "127.0.0.1"
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.IP, self.PORT))
        self.s.listen(1)
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
        self.s.send(str(self.commandlist[commandname]()).encode("utf-8"))

    def mainloop(self):
        while True:
            conn, addr = self.s.accept()
            if conn:
                print("Got connection from " + addr[0])
            data = conn.recv(1024)
            data = data.decode("utf-8")
            print("Recieved: "+data)
            data = data.split(" ")
            commandname = data[0]
            args = data[1:]
            self.execute_command(commandname, args)








