class Message(Exception):
    """ An exception class to pass error messages to the application
    handler, these messages can be printed into the command line.
    """

    def __init__(self, message):
        """ Initializes error message object. """
        super().__init__()
        self.message = message
