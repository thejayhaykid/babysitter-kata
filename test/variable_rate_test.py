""" A separate file for testing the variable rates per family """

from babysitter import Sitter

def test_with_family_and_zero_hours_worked():
    """ First test simulating a babysitting event occurred with a family selected. """
    expected = "Total amount owed: $0.00"
    e1 = Sitter(family="A")
    assert expected == e1.babysit()

def test_with_family_a_rate():
    """ Testing with a variable rate with Family A to make sure rate is applied correctly. """
    expected = "Total amount owed: $15.00"
    e1 = Sitter("1717", "1745", "A")
    assert expected == e1.babysit()