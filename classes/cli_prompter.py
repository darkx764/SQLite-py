from InquirerPy import inquirer

class menu:
    """ Simple menu using InquirerPy package. """

    def text(self, message):
        """ prompt text menu """
        return inquirer.text(message=f"{message}").execute()

    def select(self, message, choices):
        """ prompt select menu """
        return inquirer.select(
            message=f"{message}",
                choices=choices
        ).execute()

    def confirm(self, message):
        """ prompt confirmation menu """
        return inquirer.confirm(message=f"{message}").execute()