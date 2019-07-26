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

def test_with_family_b_rate():
    """ Testing to make sure Family B rate is applied successfully. """
    expected = "Total amount owed: $20.00"
    e1 = Sitter("2100", "2300", "B")
    assert expected == e1.babysit()

def test_with_family_c_rate():
    """ Testing to make sure Family C rate is applied successfully. """
    expected = "Total amount owed: $189.00"
    e1 = Sitter("1700", "0359", "C")
    assert expected == e1.babysit()

def test_with_undefined_family():
    """ Setting an error message if the family chose is not A, B, or C """
    expected = "ERROR: Valid families are A, B, or C. Family chosen invalid."
    e1 = Sitter(family="TEST")
    assert expected == e1.babysit()