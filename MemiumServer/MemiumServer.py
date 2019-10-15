import Server
import commands


class MemiumServer(Server.Server):

    def __init__(self):
        super().__init__(42069)
        self.add_command(commands.shell_command())
        self.mainloop()


s = MemiumServer()