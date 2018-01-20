from .Model import Model


class City(Model):
    def __init__(self, **kwargs):
        self.country = kwargs['country']
        self.city = kwargs['city']
