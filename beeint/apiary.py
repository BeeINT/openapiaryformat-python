import beeint


class Apiary(beeint.HistoryAware):
    history_attributes = [
        "name",
        "description",
        "location"
    ]

    def __init__(self, name=False, id=beeint.generate_id(), enable_history=False):
        super(Apiary, self).__init__()
        self.type = beeint.TYPE_APIARY
        self.name = name
        self.id = id
        self.enable_history = enable_history

    def __str__(self):
        return self.name

    def dumps(self):
        return self.history


Apiary.finish_initialization()
