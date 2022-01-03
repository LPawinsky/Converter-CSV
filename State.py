class State:
    def __init__(self, version: str, filename: any, path: any, output: any, progress: int):
        self.version = version
        self.path = path
        self.filename = filename
        self.output = output
        self.progress = progress

    def getVersion(self):
        return self.version

    def update_path(self, path):
        self.path = path

    def update_filename(self, filename):
        self.filename = filename

    def update_output(self, output):
        self.output = output

    def reset_state(self):
        self.path = None
        self.filename = None
        self.output = None
        self.progress = 0
        
    def update_state_bar(self):
        self.progress+=20