from collection import Collection


class Airplanes(Collection):
    def update(self, number, pilot, seats):
        updated = self.find(number)
        if updated:
            if pilot:
                updated.pilot = pilot
            if seats:
                updated.seats = seats
        return updated
