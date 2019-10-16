class computeRequest:

    """A standard command for the Server to process. All other commands should inherit from this"""

    def __init__(self, commandname):
        self.commandname = commandname

    """this method processes the command. It should always return a String which is then sent back to the client.
        it recieves a list of string as arguments"""

    def process(self, *args):

        return "Hi"
