

class Plane:
    def __init__(self, number, airline_company, capacity, destination, passangers=None):
        self.number = number
        self.airline_company = airline_company
        self.capacity = capacity
        self.destination = destination
        self.passangers = passangers or []


    def __str__(self):
        return f'{self.number} {self.airline_company} {self.capacity} {self.destination}'


    @staticmethod
    def from_string(line: str) -> 'Plane':
        number, airline_company, capacity, destination = line.split()
        return Plane(number, airline_company, int(capacity), destination)


    def add_passanger(self, passanger) -> bool:
        if len(self.passangers) < self.capacity:
            self.passangers.append(passanger)
            return True
        return False


    def get_passangers(self) -> list:
        return self.passangers

    
    # ...