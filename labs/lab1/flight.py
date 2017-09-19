class Flight:
    def __init__(self, number, whence, where):
        self.number = number
        self.whence = whence
        self.where = where
        self.status = False

    def __str__(self):
        return 'Number: %s, Whence: %s, Where: %s, Status: %s' \
               % (self.number, self.whence or '-', self.where or '-', self.status)
