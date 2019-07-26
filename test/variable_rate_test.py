""" A separate file for testing the variable rates per family """

from babysitter import Sitter

def test_with_family_and_zero_hours_worked():
    """ First test simulating a babysitting event occurred with a family selected. """
    expected = "Total amount owed: $0.00"
    e1 = Sitter(family="A")
    assert expected == e1.babysit()