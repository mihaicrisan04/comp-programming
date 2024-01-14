from passanger_repository import PassangerRepository
from plane_repository import PlaneRepository
from service import Service
from ui import UI


def main():
    plane_repository = PlaneRepository('planes.txt')
    passanger_repository = PassangerRepository('passangers.txt', plane_repository)
    service = Service(plane_repository, passanger_repository)
    ui = UI(service)

    ui.run()


if __name__ == '__main__':
    main()