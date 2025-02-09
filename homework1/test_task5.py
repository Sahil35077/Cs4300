from task5 import books, students

def test_books():
    assert books[:3] == ["Book1", "Book2", "Book3"]

def test_students():
    assert students["Alice"] == 101
    assert students["Bob"] == 102