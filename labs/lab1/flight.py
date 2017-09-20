class Flight:
    def __init__(self, number, whence, where, plane):
        self.number = number
        self.whence = whence
        self.where = where
        self.plane = plane

    def __str__(self):
        return 'Number: %s, Whence: %s, Where: %s, Airplane (number): %s' \
               % (self.number, self.whence or '-', self.where or '-', self.plane or '-')
