""" This is the babysitter class """


class Sitter:
    def __init__(self):
        self.rate = 10

    def babysit(self, hour_start=17, hour_end=17):
        """ Main function defining a babysitting 'event' """
        if hour_start < 0 or (4 < hour_start < 17):
            return 'ERROR: Start time out of range'
        total = self.rate * (hour_end - hour_start)
        return f'Total amount owed: ${total:.2f}'
