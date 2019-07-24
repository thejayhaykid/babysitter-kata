""" The test module for the babysitter class """

from babysitter import Sitter


def test_event_occurred():
    """ First test simulating a babysitting event occurred. """
    expected = "Total amount owed: $0.00"
    e1 = Sitter()
    assert expected == e1.babysit()
