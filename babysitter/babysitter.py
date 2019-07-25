""" This is the babysitter class """

import time

class Sitter:
    def __init__(self, start_time="0000", end_time="0000"):
        self.rate = 10
        self.start_time = start_time
        self.end_time = end_time

    def babysit(self):
        """ Main function defining a babysitting 'event' """

        # Check for valid times
        _, start_pass = self.validate_time(self.start_time)
        _, end_pass = self.validate_time(self.end_time)

        if not start_pass or not end_pass:
            return 'ERROR: Please enter a valid time'
        
        # Converting strings to ints to satisfy current testing
        self.start_time = int(self.start_time) / 100
        self.end_time = int(self.end_time) / 100

        print(f'{self.start_time}, {self.end_time}')

        if self.start_time < 0 or (4 < self.start_time < 17):
            return 'ERROR: Start time out of range'
        if self.end_time < self.start_time:
            return 'ERROR: Cannot end before start'
        total = self.rate * (self.end_time - self.start_time)
        return f'Total amount owed: ${total:.2f}'


    def validate_time(self, input_time):
        """ Method to validate time. """
        try:
            ret_time = time.strptime(input_time, '%H%M')
            return ret_time, True
        except ValueError:
            return None, False
