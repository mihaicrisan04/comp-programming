from plane import Plane


class PlaneRepositoryException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlaneRepository:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = {}
        self.read_data()


    def read_data(self):
        with open(self.file_name, 'r') as file:
            for line in file.readlines():
                # line format: number airline_company capacity destination
                plane = Plane.from_string(line)
                self.data[plane.number] = plane

    def save_data(self):
        with open(self.file_name, 'w') as file:
            for plane in self.data.values():
                file.write(str(plane) + '\n')


    def add_plane(self, plane: Plane) -> None:
        if plane.number in self.data:
            raise PlaneRepositoryException('There is already a plane with this number!')

        self.data[plane.number] = plane
        self.save_data()


    def get_plane(self, number: str) -> Plane:
        if number not in self.data:
            raise PlaneRepositoryException('There is no plane with this number!')

        return self.data.get(number)


    def get_all_planes(self) -> list:
        return list(self.data.values())


    def delete_plane(self, number: str) -> None:
        if number not in self.data:
            raise PlaneRepositoryException('There is no plane with this number!')

        del self.data[number]
        self.save_data()