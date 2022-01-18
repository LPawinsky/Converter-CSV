from time import sleep

class State:
    def __init__(self, path, output_path, version):
        self.path = path
        self.output_path = output_path
        self.version = version

    def update_path(self, val):
        self.path = None
        sleep(0.2)
        self.path = val

    def update_output(self, val):
        self.output_path = None
        sleep(0.2)
        self.output_path = val
    
