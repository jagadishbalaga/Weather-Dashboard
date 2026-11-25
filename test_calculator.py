def add(a, b):
    return a + b

def test_addition():
    result = add(10, 20)

    assert result == 30

def subtract(a, b):
    return a - b


def test_subtraction():
    result = subtract(30, 10)
    assert result == 20


def test_addition_failure():
    result = add(10, 20)
    assert result == 30