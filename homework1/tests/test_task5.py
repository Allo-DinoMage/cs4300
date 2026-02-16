from src.task5 import my_fav_books, first_three_books, student_database


def test_my_fav_books():
    """Test that the book list is created correctly"""
    books = my_fav_books()
    
    # Check it's a list
    assert isinstance(books, list)
    
    # Check it has 5 books
    assert len(books) == 5
    
    # Check first book is correct
    assert "Frankenstein" in books[0]


def test_first_three_books():
    """Test list slicing works correctly"""
    first_three = first_three_books()
    
    # Check it's a list
    assert isinstance(first_three, list)
    
    # Check it has exactly 3 items
    assert len(first_three) == 3
    
    # Check they're the first three
    assert "Frankenstein" in first_three[0]
    assert "Soul Eater" in first_three[1]
    assert "Grim Reaper" in first_three[2]


def test_student_database():
    """Test dictionary is created correctly"""
    students = student_database()
    
    # Check it's a dictionary
    assert isinstance(students, dict)
    
    # Check it's not empty
    assert len(students) > 0
    
    # Check a student exists
    assert "Alice" in students
    
    # Check the ID is correct type
    assert isinstance(students["Alice"], int)


def test_student_lookup():
    """Test we can look up student IDs"""
    students = student_database()
    
    # Test specific lookups
    assert students["Alice"] == 12345
    assert students["Bob"] == 67890