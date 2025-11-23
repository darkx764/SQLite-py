import os

class databases:
    def list(self, path):
        database_list = os.listdir(path)
        return database_list
    