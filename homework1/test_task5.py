from task5 import books, students, get_first_three_books

def test_books():
    assert get_first_three_books() == [
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("1984", "George Orwell")
    ]

def test_students():
    assert students["Alice"] == 101
    assert students["Bob"] == 102
    assert students["Charlie"] == 103