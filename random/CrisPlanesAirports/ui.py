from service import ServiceException


class UI:
    def __init__(self, service):
        self.__service = service


    def __print_menu(self):
        print('1. Sort the passengers in a plane by last name')
        print('0. Exit')


    def run(self):
        while True:
            self.__print_menu()
            option = input('Option: ').strip()

            if option == '1':
                # input
                plane_number = input('Plane number: ').strip()

                # processing
                try:
                    passangers = self.__service.sort_passangers(plane_number)
                except ServiceException as se:
                    print(se)  # afisam mesajul de eroare
                    continue  # continue da skip la afisarea pasagerilor
                
                # success output
                for passanger in passangers:
                    print(passanger)

            # ...

            elif option == '0':
                break

            else:
                print('Invalid option!')