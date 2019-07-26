""" This is the babysitter class """

import time

class Sitter:
    def __init__(self, start_time="0000", end_time="0000"):
        self.rate = 10
        self.start_time = start_time
        self.end_time = end_time
        self.hours_worked = 0

    def babysit(self):
        """ Main function defining a babysitting 'event' """

        # Check for valid times
        _, start_pass = self._validate_time(self.start_time)
        _, end_pass = self._validate_time(self.end_time)

        if not start_pass or not end_pass:
            return 'ERROR: Please enter a valid time'
        
        # Check to make sure start time is valid
        if int(self.start_time) < 0 or (400 < int(self.start_time) < 1700):
            return 'ERROR: Start time out of range'

        # Check to make sure end time is valid
        if int(self.end_time) < 0 or (400 < int(self.end_time) < 1700):
            return 'ERROR: End time out of range'

        # Converting strings to ints to satisfy current testing and rounding them correctly
        self._round_hours()

        # Calculate hours worked
        self._calculate_time_worked()

        # Check to make sure start time is before end time
        if self.hours_worked < 0:
            print(f'Hours worked: {self.hours_worked}')
            return 'ERROR: Cannot end before start'

        total = self.rate * self.hours_worked
        return f'Total amount owed: ${total:.2f}'


    def _validate_time(self, input_time):
        """ Method to validate time. """
        try:
            ret_time = time.strptime(input_time, '%H%M')
            return ret_time, True
        except ValueError:
            return None, False

    def _calculate_time_worked(self):
        """ Private method to calculate the time worked to make babysit() smaller."""
        if self.start_time <= 4 and self.start_time >= 0:
            temp_start_time = self.start_time + 24
        else:
            temp_start_time = self.start_time

        if self.end_time <= 4 and self.end_time >= 0:
            temp_end_time = self.end_time + 24
        else:
            temp_end_time = self.end_time
        
        self.hours_worked = temp_end_time - temp_start_time

    def _round_hours(self):
        """ Private method to make sure there are no partial hours.  """
        self.start_time = int(self.start_time)
        self.end_time = int(self.end_time)
        start_round = (self.start_time % 100) // 30
        end_round = (self.end_time % 100) // 30
        self.start_time = (self.start_time // 100) + start_round
        self.end_time = (self.end_time // 100) + end_round