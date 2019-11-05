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
        result_length = len(res)
        header = f"len:{result_length}"
        print("Sending header: " + header)
        self.conn.send(header.encode("utf-8"))
        print("Sending content: " + str(res))
        self.conn.send(str(res).encode("utf-8"))

    def mainloop(self):
        self.conn, addr = self.s.accept()
        while True:
            if self.conn:
                print("Got connection from " + addr[0])
            data = self.conn.recv(1024)
            data = data.decode("utf-8")
            print("Recieved: "+data)
            data = data.split(" ")
            commandname = data[0]
            args = data[1:]
            self.execute_command(commandname, args)








