class Validate:
    def __init__(self, path, output, case):
        self.path = path
        self.output = output
        self.case = case

    def validation(self):
        from validation_fail import validation_fail
        if self.path == None and self.output == None:
            validation_fail('Brak ściezki wejścia wyjścia')
        if self.path == None and self.output != None:
            validation_fail('Brak pliku. Wybierz plik.')
        if self.output == None and self.path != None:
            validation_fail('Brak folderu do konwersji')
        if self.path != None and self.output != None:
            from Decider import Decider
            decider = Decider(self.path, self.output, self.case)
            decider.decide()