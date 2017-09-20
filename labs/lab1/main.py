from menu import Menu


def main():
    menu = Menu()
    menu.deserialize()
    print('You can use command: help')

    while True:
        cmd = input('>> ').strip().lower()

        if cmd == 'help':
            Menu.print_help()

        elif cmd == 'exit':
            break

        elif cmd == 'show':
            Menu.show_options()
            print('Press 3: All')

            num = input('?: ')
            if num == '1':
                menu.print_planes()
            elif num == '2':
                menu.print_flights()
            elif num == '3':
                menu.print_planes()
                menu.print_flights()
            else:
                print('Invalid input!')

        elif cmd == 'add':
            Menu.show_options()

            num = input('?: ')
            if num == '1':
                menu.add_plane()
            elif num == '2':
                menu.add_flight()
            else:
                print('Invalid input!')

        elif cmd == 'edit':
            Menu.show_options()

            num = input('?: ')
            if num == '1':
                menu.edit_plane()
            elif num == '2':
                menu.edit_flight()
            else:
                print('Invalid input!')

        elif cmd == 'del':
            Menu.show_options()

            num = input('?: ')
            if num == '1':
                menu.delete_plane()
            elif num == '2':
                menu.delete_flight()
            else:
                print('Invalid input!')

        elif cmd == 'drop':
            Menu.show_options()
            print('Press 3: All')

            num = input('?: ')
            if num == '1':
                menu.drop_planes()
            elif num == '2':
                menu.drop_flights()
            elif num == '3':
                menu.drop_planes()
                menu.drop_flights()
            else:
                print('Invalid input!')

        elif cmd == 'search':
            menu.search_planes()

    menu.serialize()


if __name__ == "__main__":
    main()
