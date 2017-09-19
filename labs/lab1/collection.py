class Collection:
    def __init__(self):
        self.list = []

    def exists(self, number):
        return any(x.number == number for x in self.list)

    def insert(self, item):
        if not self.exists(item.number):
            self.list.append(item)

    def find(self, number):
        return next((x for x in self.list if x.number == number), None)

    def numbers(self, check):
        return [x.number for x in self.list if check(x)]

    def filter(self, check):
        return list(filter(check, self.list))

    def remove(self, number):
        x = self.find(number)
        if x:
            self.list.remove(x)

    def drop(self):
        del self.list[:]

    def __str__(self):
        return '\n'.join(str(x) for x in self.list)
