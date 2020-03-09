class GroupLimitException(ValueError):
    """
    Group seats limit exception
    """
    def __init__(self):
        self.message = 'Group limit exception'

    def __str__(self):
        return self.message
