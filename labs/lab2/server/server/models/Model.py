from .. import db


class Model:
    @classmethod
    def table(cls):
        return cls.__name__.lower()

    @classmethod
    def all(cls):
        return db.all(cls.table())

    @classmethod
    def get(cls, id):
        return db.get(cls.table(), id)

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        return db.create(cls.table(), obj.__dict__)

    @classmethod
    def update(cls, id, **kwargs):
        obj = cls(**kwargs)
        db.update(cls.table(), id, obj.__dict__)

    @classmethod
    def delete(cls, id):
        db.delete(cls.table(), id)

    @classmethod
    def drop(cls):
        db.truncate(cls.table())
