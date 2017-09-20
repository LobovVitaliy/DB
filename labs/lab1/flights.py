from collection import Collection


class Flights(Collection):
    def update(self, number, whence, where, plane):
        updated = self.find(number)
        if updated:
            if whence:
                updated.whence = whence
            if where:
                updated.where = where
            if plane:
                updated.plane = plane
        return updated

    def get_planes(self, check):
        return [x.plane for x in self.list if check(x)]

    def delete_planes(self, *numbers):
        for x in self.list:
            if x.plane in numbers:
                x.plane = None
