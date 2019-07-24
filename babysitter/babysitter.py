""" This is the babysitter class """


class Sitter:
    def __init__(self, start_time=0, end_time=0):
        self.rate = 10
        self.start_time = start_time
        self.end_time = end_time 

    def babysit(self):
        """ Main function defining a babysitting 'event' """
        if self.start_time < 0 or (4 < self.start_time < 17):
            return 'ERROR: Start time out of range'
        if self.end_time < self.start_time:
            return 'ERROR: Cannot end before start'
        total = self.rate * (self.end_time - self.start_time)
        return f'Total amount owed: ${total:.2f}'
