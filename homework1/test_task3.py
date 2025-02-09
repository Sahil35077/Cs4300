from task3 import check_number, prime_numbers, sum_numbers

def test_check_number():
    assert check_number(10) == "Positive"
    assert check_number(-5) == "Negative"
    assert check_number(0) == "Zero"

def test_prime_numbers():
    assert prime_numbers() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_numbers():
    assert sum_numbers() == 5050