from passanger import Passanger


class PassangerRepositoryException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PassangerRepository:
    def __init__(self, file_name: str, plane_repository):
        self.file_name = file_name
        self.plane_repository = plane_repository
        self.data = {}
        self.read_data()

    
    def read_data(self):
        with open(self.file_name, 'r') as file:
            for line in file.readlines():
                # line format: plane_number first_name last_name passport
                plane_number = line.split()[0]

                plane = self.plane_repository.get_plane(plane_number)

                line = line[len(plane_number):]
                passanger = Passanger.from_string(line)

                plane.add_passanger(passanger)
                self.data[passanger.passport] = passanger


    def save_data(self):
        with open(self.file_name, 'w') as file:
            for plane in self.plane_repository.get_all_planes():
                for passanger in plane.get_passangers():
                    file.write(str(plane.number) + ' ' + str(passanger) + '\n')


    def add_passanger(self, passanger: Passanger) -> None:
        if passanger.passport in self.data:
            raise PassangerRepositoryException('There is already a passanger with this passport!')

        self.data[passanger.passport] = passanger
        self.save_data()


    def get_passanger(self, passport: str) -> Passanger:
        if passport not in self.data:
            raise PassangerRepositoryException('There is no passanger with this passport!')

        return self.data.get(passport)


    def get_all_passangers(self) -> list:
        return list(self.data.values())


    def delete_passanger(self, passport: str) -> None:
        if passport not in self.data:
            raise PassangerRepositoryException('There is no passanger with this passport!')

        del self.data[passport]
        self.save_data()


    def add_passanger_to_plane(self, plane_number: str, passanger: Passanger) -> None:
        plane = self.plane_repository.get_plane(plane_number)

        plane_passangers = plane.get_passangers()

        if passanger in plane_passangers:
            raise PassangerRepositoryException('This passanger is already in this plane!')

        plane.add_passanger(passanger)
        self.save_data()