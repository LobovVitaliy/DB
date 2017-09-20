import pickle


class Collection:
    def __init__(self, name):
        self.list = []
        self.name = name

    def exists(self, number):
        return any(x.number == number for x in self.list)

    def insert(self, item):
        if not self.exists(item.number):
            self.list.append(item)

    def find(self, number):
        return next((x for x in self.list if x.number == number), None)

    def numbers(self, check=lambda x: True):
        return [x.number for x in self.list if check(x)]

    def filter(self, check):
        return list(filter(check, self.list))

    def remove(self, number):
        x = self.find(number)
        if x:
            self.list.remove(x)
            return True
        return False

    def drop(self):
        del self.list[:]

    def serialize(self):
        with open(self.name, 'wb') as f:
            pickle.dump(self.list, f)

    def deserialize(self):
        with open(self.name, 'rb') as f:
            self.list = pickle.load(f)

    def __str__(self):
        return '\n'.join(str(x) for x in self.list)
