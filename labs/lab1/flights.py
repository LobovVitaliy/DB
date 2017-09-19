from collection import Collection


class Flights(Collection):
    def update(self, number, whence, where):
        updated = self.find(number)
        if updated:
            if whence:
                updated.whence = whence
            if where:
                updated.where = where
        return updated

    def reset_status(self):
        for x in self.list:
            x.status = False
