from src.fizzbuzz import fizzbuzz

def test_prints_fizz_for_three():
    results = fizzbuzz(3)
    assert results == [1, 2, "fizz"]


def test_prints_buzz_for_five():
    results = fizzbuzz(5)
    assert results == [1, 2, "fizz", 4, "buzz"]

def test_prints_buzz_for_fifteen():
    results = fizzbuzz(15)
    assert results == [
        1,
        2,
        "fizz",
        4,
        "buzz",
        "fizz",
        7,
        8,
        "fizz",
        "buzz",
        11,
        "fizz",
        13,
        14,
        "fizzbuzz"
    ]
