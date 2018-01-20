from .Model import Model


class Flight(Model):
    def __init__(self, **kwargs):
        self.id_from_airport = kwargs['id_from_airport']
        self.id_to_airport = kwargs['id_to_airport']
        self.id_plane = kwargs['id_plane']
        self.date = kwargs['date']
        self.status = kwargs['status']
