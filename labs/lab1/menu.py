from airplanes import Airplanes
from airplane import Airplane
from flights import Flights
from flight import Flight

import pickle


class Menu:
    def __init__(self):
        self.airplanes = Airplanes('airplanes')
        self.flights = Flights('flights')

    @staticmethod
    def show_options():
        print('Press 1: Airplanes')
        print('Press 2: Flights')

    @staticmethod
    def ask(question):
        while True:
            check = input(question + ' (y/n) ').lower()
            if check in ('y', 'yes'):
                return True
            elif check in ('n', 'no'):
                return False

    def serialize(self):
        try:
            self.airplanes.serialize()
            self.flights.serialize()
        except OSError as e:
            print(e)
        except pickle.PickleError:
            print('Serialization error!')

    def deserialize(self):
        try:
            self.airplanes.deserialize()
            self.flights.deserialize()
        except OSError as e:
            print(e)
        except pickle.PickleError:
            print('Deserialization error!')

    # Print:
    @staticmethod
    def print_help():
        print('help   -- Print all commands')
        print('exit   -- Exiting the program')
        print('show   -- Show list')
        print('add    -- Add item to list')
        print('edit   -- Edit list item')
        print('del    -- Remove item from list')
        print('drop   -- Clear list')
        print('search -- Search for aircraft')

    def print_planes(self):
        print('Airplanes:')
        print(self.airplanes)

    def print_flights(self):
        print('Flights:')
        print(self.flights)

    # Add
    def add_plane(self):
        airplane = self.input_and_get_plane()
        if airplane:
            self.airplanes.insert(airplane)
            print('Added:', airplane)

    def input_and_get_plane(self):
        number = input('Number: ')
        if not number:
            print('Invalid input!')
            return
        if self.airplanes.exists(number):
            print('Plane already exists!')
            return
        pilot = input('Pilot: ')
        seats = input('Seats: ')

        return Airplane(number, pilot, seats)

    def add_flight(self):
        flight = self.input_and_get_flight()
        if flight:
            self.flights.insert(flight)
            print('Added:', flight)

    def input_and_get_flight(self):
        number = input('Number: ')
        if not number:
            print('Invalid input!')
            return
        if self.flights.exists(number):
            print('Flight already exists!')
            return
        whence = input('Whence: ')
        where = input('Where: ')
        plane = input('Plane: ')
        if not self.airplanes.exists(plane):
            print('Plane does not exist!')
            return

        return Flight(number, whence, where, plane)

    # Edit
    def edit_plane(self):
        number = input('Number: ')
        if not number:
            print('Invalid input!')
            return
        if not self.airplanes.exists(number):
            print('Plane does not exist!')
            return

        pilot = input('Pilot (new): ')
        seats = input('Seats (new): ')

        updated = self.airplanes.update(number, pilot, seats)
        print('Edited:', updated)

    def edit_flight(self):
        number = input('Number: ')
        if not number:
            print('Invalid input!')
            return
        if not self.flights.exists(number):
            print('Flight does not exist!')
            return
        whence = input('Whence (new): ')
        where = input('Where  (new): ')
        plane = input('Plane  (new): ')
        if not self.airplanes.exists(plane):
            print('Plane does not exist!')
            return

        updated = self.flights.update(number, whence, where, plane)
        print('Edited:', updated)

    # Delete
    def delete_plane(self):
        number = input('Number: ')
        if not number:
            print('Invalid input!')
            return
        check = self.airplanes.remove(number)
        if check:
            self.flights.delete_planes(number)
            print('Successfully deleted!')
        else:
            print('Airplane does not exist!')

    def delete_flight(self):
        number = input('Number: ')
        if not number:
            print('Invalid input!')
            return
        check = self.flights.remove(number)
        if check:
            print('Successfully deleted!')
        else:
            print('Flight does not exist!')

    # Drop
    def drop_planes(self):
        check = self.ask('Delete the list (Airplanes)?')
        if check:
            numbers = self.airplanes.numbers()
            self.flights.delete_planes(*numbers)
            self.airplanes.drop()
            print('Successfully deleted!')

    def drop_flights(self):
        check = self.ask('Delete the list (Flights)?')
        if check:
            self.flights.drop()
            print('Successfully deleted!')

    # Search
    def search_planes(self):
        where = input('Where: ')
        if not where:
            print('Invalid input!')
            return
        numbers = self.flights.get_planes(lambda x: x.where == where)
        filtered = self.airplanes.filter(lambda x: x.number in numbers)
        print('Filtered by country:', where)
        print('\n'.join(str(x) for x in filtered))
