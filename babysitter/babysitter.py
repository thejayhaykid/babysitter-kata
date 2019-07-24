""" This is the babysitter class """


class Sitter:
    def __init__(self):
        self.rate = 10

    def babysit(self, hour_start=0, hour_end=0):
        """ Main function defining a babysitting 'event' """
        total = self.rate * (hour_end - hour_start)
        return f'Total amount owed: ${total:.2f}'
