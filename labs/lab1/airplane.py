class Airplane:
    def __init__(self, number, pilot, seats, flight):
        self.number = number
        self.pilot = pilot
        self.seats = seats
        self.flight = flight

    def __str__(self):
        return 'Number: %s, Pilot: %s, Count of seats: %s, Flight: %s' \
               % (self.number, self.pilot or '-', self.seats or '-', self.flight or '-')
