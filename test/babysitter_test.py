""" The test module for the babysitter class """

from babysitter import Sitter


def test_event_occurred():
    """ First test simulating a babysitting event occurred. """
    expected = "Total amount owed: $0.00"
    e1 = Sitter()
    assert expected == e1.babysit()


def test_event_occurred_with_hours():
    """ Putting the time babysitting by giving the start and end time. """
    expected = "Total amount owed: $15.00"
    e1 = Sitter("1700", "1800")
    # Updated after custom rates were implemented
    assert expected == e1.babysit()


def test_event_started_before_time_allowed():
    """ Attempting to start and event before 5 PM should return an error. """
    expected = "ERROR: Start time out of range"
    e1 = Sitter("1600", "1700")
    assert expected == e1.babysit()


def test_event_started_after_midnight():
    """ Babysitting events can start after midnight as long as they end before 4 AM. """
    expected = "Total amount owed: $20.00" # Updated after variable rates were entered.
    e1 = Sitter("0000", "0100")
    assert expected == e1.babysit()


def test_end_time_earlier_than_start_time():
    """ Ensuring that you cannot complete an event before it is started. """
    expected = "ERROR: Cannot end before start"
    e1 = Sitter("1900", "1700")
    assert expected == e1.babysit()

def test_input_time_must_be_valid_hour():
    """ Ensuring that time inputs where hour > 23 is not accepted. """
    expected = "ERROR: Please enter a valid time"
    e1 = Sitter("2400", "2600")
    assert expected == e1.babysit()

def test_start_time_before_midnight_end_time_after_midnight():
    """ Making sure babysitter still gets paid if they are not done until after midnight."""
    expected = "Total amount owed: $95.00" # Updated after variable rates were entered.
    e1 = Sitter("2200", "0300")
    assert expected == e1.babysit()

def test_end_time_is_within_valid_range():
    """ Ensuring that the end time is within a valid range. The same as the start time. """
    expected = "ERROR: End time out of range"
    e1 = Sitter("0300", "0500")
    assert expected == e1.babysit()

def test_time_rounding_up_when_past_half_the_hour():
    """ Fufilling the requirement 'gets paid for full hours (no fractional hours)' """
    expected = "Total amount owed: $95.00" # Updated after variable rates were entered.
    e1 = Sitter("2200", "0235")
    assert expected == e1.babysit()

def test_time_rounding_up_to_four_still_works():
    """ Ensuring a time can be rounded up to four without failing. """
    expected = "Total amount owed: $40.00" # Updated after variable rates were entered.
    e1 = Sitter("0223", "0345")
    assert expected == e1.babysit()