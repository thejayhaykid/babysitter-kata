""" The test module for the babysitter class """

from babysitter import Sitter


def test_event_occurred():
    """ First test similuating a babysitting event occurred. """
    expected = "Successful event."
    e1 = Sitter()
    assert expected == e1.babysit()
