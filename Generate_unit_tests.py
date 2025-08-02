# TODO: Ask Amazon Q to write unit tests.

def sum(a, b):
    """
    Function to sum two numbers.

    Args:
    - a: First number.
    - b: Second number.

    Returns:
    - Sum of the two numbers.
    """
    return a + b

# Write a test case for the above function.
def test_sum():
    assert sum(1, 2) == 3
    assert sum(0, 0) == 0
    assert sum(-1, 1) == 0
    assert sum(-1, -1) == -2
    assert sum(1, -1) == 0
    assert sum(1, 0) == 1
    assert sum(0, 1) == 1
    assert sum(1, 1) == 2
    assert sum(2, 1) == 3
    assert sum(1, 2) == 3
    
    