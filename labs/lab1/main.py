from airplanes import Airplanes
from airplane import Airplane
from flights import Flights
from flight import Flight

import pickle

airplanes = Airplanes()
flights = Flights()


def serialize():
    try:
        with open('airplanes', 'wb') as f:
            pickle.dump(airplanes, f)
        with open('flights', 'wb') as f:
            pickle.dump(flights, f)
    except Exception:
        print('Serialization error!')


def deserialize():
    global airplanes
    global flights
    try:
        with open('airplanes', 'rb') as f:
            airplanes = pickle.load(f)
        with open('flights', 'rb') as f:
            flights = pickle.load(f)
    except Exception:
        print('Deserialization error!')


def show_options():
    print('Press 1: Airplanes')
    print('Press 2: Flights')


def ask(question):
    while True:
        check = input(question + ' (y/n) ').lower()
        if check in ('y', 'yes'):
            return True
        elif check in ('n', 'no'):
            return False


# Print:
def print_help():
    print('help   -- Print all commands')
    print('exit   -- Exiting the program')
    print('show   -- Show list')
    print('add    -- Add item to list')
    print('edit   -- Edit list item')
    print('del    -- Remove item from list')
    print('drop   -- Clear list')
    print('search -- Search for aircraft')


def print_planes():
    print('Airplanes:')
    print(airplanes)


def print_flights():
    print('Flights:')
    print(flights)


# Add
def add_plane():
    airplane = input_and_get_plane()
    if airplane:
        airplanes.insert(airplane)
        print('Added:', airplane)


def input_and_get_plane():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    elif airplanes.exists(number):
        print('Plane already exists!')
        return
    pilot = input('Pilot: ')
    seats = input('Seats: ')

    return Airplane(number, pilot, seats)


def add_flight():
    flight = input_and_get_flight()
    if flight:
        flights.insert(flight)
        print('Added:', flight)


def input_and_get_flight():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    if flights.exists(number):
        print('Flight already exists!')
        return
    whence = input('Whence: ')
    where = input('Where: ')
    plane = input('Plane: ')
    if not airplanes.exists(plane):
        print('Plane does not exist!')
        return

    return Flight(number, whence, where, plane)


# Edit
def edit_plane():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    if not airplanes.exists(number):
        print('Plane does not exist!')
        return

    pilot = input('Pilot (new): ')
    seats = input('Seats (new): ')

    updated = airplanes.update(number, pilot, seats)
    print('Edited:', updated)


def edit_flight():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    if not flights.exists(number):
        print('Flight does not exist!')
        return
    whence = input('Whence (new): ')
    where = input('Where  (new): ')
    plane = input('Plane  (new): ')
    if not airplanes.exists(plane):
        print('Plane does not exist!')
        return

    updated = flights.update(number, whence, where, plane)
    print('Edited:', updated)


# Delete
def delete_plane():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    if airplanes.exists(number):
        flights.delete_planes(number)
        airplanes.remove(number)
        print('Successfully deleted!')
    else:
        print('Airplane does not exist!')


# - exists
def delete_flight():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    if flights.exists(number):
        flights.remove(number)
        print('Successfully deleted!')
    else:
        print('Flight does not exist!')


# Drop
def drop_planes():
    check = ask('Are you sure you want to delete the list (Airplanes)?')
    if check:
        numbers = airplanes.numbers()
        flights.delete_planes(*numbers)
        airplanes.drop()
        print('Successfully deleted!')


def drop_flights():
    check = ask('Are you sure you want to delete the list (Flights)?')
    if check:
        flights.drop()
        print('Successfully deleted!')


# Search
def search_planes():
    where = input('Where: ')
    if not where:
        print('Invalid input!')
        return

    numbers = flights.get_planes(where)
    filtered = airplanes.filter(lambda x: x.number in numbers)
    print('Filtered by country:', where)
    print('\n'.join(str(x) for x in filtered))


# Main
def main():
    deserialize()
    print('You can use command: help')

    while True:
        cmd = input('>> ').strip().lower()

        if cmd == 'help':
            print_help()

        elif cmd == 'exit':
            break

        elif cmd == 'show':
            show_options()
            print('Press 3: All')

            num = input('?: ')
            if num == '1':
                print_planes()
            elif num == '2':
                print_flights()
            elif num == '3':
                print_planes()
                print_flights()
            else:
                print('Invalid input!')

        elif cmd == 'add':
            show_options()

            num = input('?: ')
            if num == '1':
                add_plane()
            elif num == '2':
                add_flight()
            else:
                print('Invalid input!')

        elif cmd == 'edit':
            show_options()

            num = input('?: ')
            if num == '1':
                edit_plane()
            elif num == '2':
                edit_flight()
            else:
                print('Invalid input!')

        elif cmd == 'del':
            show_options()

            num = input('?: ')
            if num == '1':
                delete_plane()
            elif num == '2':
                delete_flight()
            else:
                print('Invalid input!')

        elif cmd == 'drop':
            show_options()
            print('Press 3: All')

            num = input('?: ')
            if num == '1':
                drop_planes()
            elif num == '2':
                drop_flights()
            elif num == '3':
                drop_planes()
                drop_flights()
            else:
                print('Invalid input!')

        elif cmd == 'search':
            search_planes()

    serialize()


if __name__ == "__main__":
    main()
