from collection import Collection


class Airplanes(Collection):
    def update(self, number, pilot, seats, flight):
        updated = self.find(number)
        if updated:
            if pilot:
                updated.pilot = pilot
            if seats:
                updated.seats = seats
            if flight:
                updated.flight = flight
        return updated

    def reset_flight(self, number=None):
        if number:
            for x in self.list:
                if x.flight == number:
                    x.flight = None
                    break
        else:
            for x in self.list:
                x.flight = None
