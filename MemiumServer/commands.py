import ComputeRequest
import subprocess


class shell_command(ComputeRequest.computeRequest):

    def __init__(self):
        super().__init__("extshell")

    def process(self, *args):
        print("Shell executing command: "+" ".join(map(str, args[0])))
        try:
            return subprocess.check_output(" ".join(map(str, args[0])))
        except Exception as e:
            print(e)
            return "Error"
