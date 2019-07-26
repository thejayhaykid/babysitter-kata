""" This is the babysitter class """

import time

# Families rates will be global variables
FAMILY_A = [15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20]
FAMILY_B = [12, 12, 12, 12, 12,  8,  8, 16, 16, 16, 16]
FAMILY_C = [21, 21, 21, 21, 15, 15, 15, 15, 15, 15, 15]
WORKED_START = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class Sitter:
    def __init__(self, start_time="0000", end_time="0000", family="A"):
        self.start_time = start_time
        self.end_time = end_time
        self.hours_worked = 0
        self.family = family
        self.hours_worked_list = WORKED_START

    def babysit(self):
        """ Main function defining a babysitting 'event' """
        families = {"A": FAMILY_A, "B": FAMILY_B, "C": FAMILY_C}
        rate = families[self.family]

        # Check for valid times
        start_pass = self._validate_time(self.start_time)
        end_pass = self._validate_time(self.end_time)

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

        total = sum([i*j for i,j in zip(rate,self.hours_worked_list)])
        return f'Total amount owed: ${total:.2f}'


    def _validate_time(self, input_time):
        """ Method to validate time. """
        try:
            time.strptime(input_time, '%H%M')
            return True
        except ValueError:
            return False

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
        start_index = temp_start_time - 17
        self.hours_worked_list = [1 if i in range(start_index, start_index + self.hours_worked) else e for i, e in enumerate(self.hours_worked_list)]
        print(f'Hours worked list: {self.hours_worked_list}')

    def _round_hours(self):
        """ Private method to make sure there are no partial hours.  """
        self.start_time = int(self.start_time)
        self.end_time = int(self.end_time)
        start_round = (self.start_time % 100) // 30
        end_round = (self.end_time % 100) // 30
        self.start_time = (self.start_time // 100) + start_round
        self.end_time = (self.end_time // 100) + end_round