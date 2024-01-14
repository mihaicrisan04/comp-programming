

class Passanger:
    def __init__(self, first_name, last_name, passport):
        self.first_name = first_name
        self.last_name = last_name
        self.passport = passport


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.passport}'


    def __eq__(self, other):
        return self.passport == other.passport


    @staticmethod
    def from_string(line) -> 'Passanger':
        first_name, last_name, passport = line.split()
        return Passanger(first_name, last_name, passport)

    
    # ...
