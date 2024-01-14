from plane import Plane
from passanger import Passanger
from plane_repository import PlaneRepositoryException
from passanger_repository import PassangerRepositoryException


class ServiceException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Service:
    def __init__(self, plane_repository, passanger_repository):
        self.plane_repository = plane_repository
        self.passanger_repository = passanger_repository

    
    def sort_passangers(self, plane_number: str) -> list:
        try:
            plane = self.plane_repository.get_plane(plane_number)
        except PlaneRepositoryException:
            raise ServiceException('There is no plane with this number!')

        passangers = plane.get_passangers()
        passangers.sort(key=lambda passanger: passanger.last_name)

        return passangers

    
    # ...
