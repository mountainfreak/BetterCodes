class Database(object):
    def __init__(self):
        self.database = []
        self.num=0
        self.sort_key=0
    def put(self, storage):
        self.database.append(storage)
    def out(self):
        return self.database


