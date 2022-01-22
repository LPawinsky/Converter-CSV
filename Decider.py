import os.path
from pathlib import Path

class Decider:
    def __init__(self, path, output, case):
        self.path = path
        self.output = output
        self.case = case
        self.ext = str(os.path.splitext(path)[1])
        self.filename = str(Path(path).stem)
        
    def decide(self):
        from ExtractWindow import extract
        if self.ext == '.csv':
            if self.case == 'Q':
                extract(self.path, self.output, 'qcsv')
            if self.case == 'M':
                extract(self.path, self.output, 'mcsv')
            if self.case == 'D':
                extract(self.path, self.output, 'dcsv')
            if self.case == 'W':
                extract(self.path, self.output, 'wcsv')
        if self.ext == '.txt':
            if self.case == 'Q':
                extract(self.path, self.output, 'qtxt')
            if self.case == 'M':
                extract(self.path, self.output, 'mtxt')
            if self.case == 'D':
                extract(self.path, self.output, 'dtxt')
            if self.case == 'W':
                extract(self.path, self.output, 'wtxt')
