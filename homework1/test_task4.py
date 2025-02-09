from task4 import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(200.0, 20) == 160.0
    assert calculate_discount(50, 50) == 25