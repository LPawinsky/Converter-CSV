from quarter_script import quarter_script
from daily_script import daily_script
from convert_prn_to_data import convert_data
import os

class Decider:
    def __init__(self, case, path, output):
        self.case = case
        self.path = path
        self.output = output
        self.ext = os.path.splitext(path)[1]

    def case_decide(self):
        if self.ext == '.csv':
            if self.case == 'Q':
                quarter_script(self.path, self.output, None, 'path')
            if self.case == 'D':
                daily_script(self.path, self.output, None, 'path')
        if self.ext == '.txt':
            if self.case == 'Q':
                quarter_script(self.path, self.output, convert_data(self.path), 'nonpath')
            if self.case == 'D':
                daily_script(self.path, self.output, convert_data(self.path), 'nonpath')