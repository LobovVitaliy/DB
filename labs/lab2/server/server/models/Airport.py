from .Model import Model


class Airport(Model):
    def __init__(self, **kwargs):
        self.id_city = kwargs['id_city']
        self.name = kwargs['name']
