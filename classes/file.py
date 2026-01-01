import os

class file_management:
    """ File Management Class. """
    @staticmethod
    def save(d = 'start_application'):
        #check if storage folder path exist or not
        sp = os.path.exists('storage')
        if sp is False:
            os.mkdir("storage")
        # save state into file 
        with open('storage/user.log', 'w', encoding='utf-8') as state:
            state.write(d) # write user state into file
