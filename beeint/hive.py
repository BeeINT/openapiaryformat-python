import beeint


class Hive(beeint.HistoryAware):

    history_attributes = [
        "name",
        "description",
        "apiary"
    ]

    def __init__(self, name=False, enable_history=False):
        super(Hive, self).__init__()
        self.type = beeint.TYPE_HIVE
        self.name = name
        self.enable_history = enable_history

    def __str__(self):
        return self.name

    def dumps(self):
        return """{
    "name" : "%s",
    "type" : "hive"
}""" % self.name


Hive.finish_initialization()
