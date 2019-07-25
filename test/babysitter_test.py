""" The test module for the babysitter class """

from babysitter import Sitter


def test_event_occurred():
    """ First test simulating a babysitting event occurred. """
    expected = "Total amount owed: $0.00"
    e1 = Sitter()
    assert expected == e1.babysit()


def test_event_occurred_with_hours():
    """ Putting the time babysitting by giving the start and end time. """
    expected = "Total amount owed: $10.00"
    e1 = Sitter("1700", "1800")
    # Before custom rates are added, using standard $10/hr.
    assert expected == e1.babysit()


def test_event_started_before_time_allowed():
    """ Attempting to start and event before 5 PM should return an error. """
    expected = "ERROR: Start time out of range"
    e1 = Sitter("1600", "1700")
    assert expected == e1.babysit()


def test_event_started_after_midnight():
    """ Babysitting events can start after midnight as long as they end before 4 AM. """
    expected = "Total amount owed: $10.00"
    e1 = Sitter("0000", "0100")
    assert expected == e1.babysit()


def test_end_time_earlier_than_start_time():
    """ Ensuring that you cannot complete an event before it is started. """
    expected = "ERROR: Cannot end before start"
    e1 = Sitter("1900", "1700")
    assert expected == e1.babysit()
