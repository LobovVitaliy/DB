from .Model import Model


class Plane(Model):
    def __init__(self, **kwargs):
        self.pilot = kwargs['pilot']
        self.seats = kwargs['seats']
