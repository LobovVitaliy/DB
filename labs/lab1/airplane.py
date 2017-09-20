class Airplane:
    def __init__(self, number, pilot, seats):
        self.number = number
        self.pilot = pilot
        self.seats = seats

    def __str__(self):
        return 'Number: %s, Pilot: %s, Count of seats: %s' \
               % (self.number, self.pilot or '-', self.seats or '-')
