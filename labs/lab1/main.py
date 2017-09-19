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
    flight = choose_flight('Add')

    return Airplane(number, pilot, seats, flight)


def choose_flight(action):
    while True:
        check = ask(action + ' flight?')
        if not check:
            return

        numbers = flights.numbers(lambda x: not x.status)
        if numbers:
            check = ask('New flight?')
        else:
            check = True

        if check:
            flight = input_and_get_flight()
            if flight:
                flights.insert(flight)
        else:
            print('Existing flight numbers:', '; '.join(numbers))
            flight = input_and_find_flight()

        if flight:
            if flight.status:
                print('This flight belongs to another plane!')
            else:
                flight.status = True
                return flight.number


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

    return Flight(number, whence, where)


def input_and_find_flight():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    flight = flights.find(number)
    if not flight:
        print('Flight does not exist!')
    else:
        return flight


# Edit
def edit_plane():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    airplane = airplanes.find(number)
    if not airplane:
        print('Plane does not exist!')
        return

    old_number = airplane.flight

    pilot = input('Pilot (new): ')
    seats = input('Seats (new): ')
    flight = choose_flight('Edit')

    if flight and old_number:
        old_flight = flights.find(old_number)
        old_flight.status = False

    updated = airplanes.update(number, pilot, seats, flight)
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

    updated = flights.update(number, whence, where)
    print('Edited:', updated)


# Delete
def delete_plane():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    airplane = airplanes.find(number)
    if airplane:
        flight_number = airplane.flight
        if flight_number:
            check = ask('Delete flight?')
            if check:
                flights.remove(flight_number)
            else:
                flight = flights.find(flight_number)
                flight.status = False
        airplanes.remove(number)
        print('Successfully deleted!')
    else:
        print('Airplane does not exist!')


def delete_flight():
    number = input('Number: ')
    if not number:
        print('Invalid input!')
        return
    if flights.exists(number):
        airplanes.reset_flight(number)
        flights.remove(number)
        print('Successfully deleted!')
    else:
        print('Flight does not exist!')


# Drop
def drop_planes():
    check = ask('Are you sure you want to delete the list (Airplanes)?')
    if check:
        flights.reset_status()
        airplanes.drop()
        print('Successfully deleted!')


def drop_flights():
    check = ask('Are you sure you want to delete the list (Flights)?')
    if check:
        airplanes.reset_flight()
        flights.drop()
        print('Successfully deleted!')


# Search
def search_planes():
    where = input('Where: ')
    if not where:
        print('Invalid input!')
        return

    numbers = flights.numbers(lambda x: x.where == where)
    filtered = airplanes.filter(lambda x: x.flight in numbers)
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
