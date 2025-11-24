import os
from classes.cli_prompter import menu

class databases:
    """Databases Manager ."""
    def __init__(self):
        """ create menu instance """
        self.menu = menu()

    def list(self, path):
        """ list all databases available in databases folder. """
        return os.listdir(path)
    
    def show(self):
        """ prompt menu with all tables available. """
        return self.menu.select("Choose your DB: ", self.list('databases'))