import ComputeRequest
import subprocess


class shell_command(ComputeRequest.computeRequest):

    def __init__(self):
        super().__init__("extshell")

    def execute(self, *args):
        return subprocess.check_output(" ".join(args))
