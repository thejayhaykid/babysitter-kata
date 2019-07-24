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
    e1 = Sitter()
    # Before custom rates are added, using standard $10/hr.
    assert expected == e1.babysit(17, 18)
