from src.task2 import varsDataTypes


def test_vars_data_types(capsys):
    """Test that varsDataTypes demonstrates all required data types"""
    varsDataTypes()
    captured = capsys.readouterr()
    
    # Test integer output
    assert "3 times 2 equals 6" in captured.out
    
    # Test float output (checking the calculation)
    assert "2.2 times 3.3 equals" in captured.out
    assert "7.26" in captured.out
    
    # Test string and boolean output
    assert "Gary failed!" in captured.out


def test_integer_type():
    """Verify integer variables work correctly"""
    number_a = 3
    number_b = 2
    product = number_a * number_b
    
    assert isinstance(number_a, int)
    assert isinstance(number_b, int)
    assert isinstance(product, int)
    assert product == 6


def test_float_type():
    """Verify float variables work correctly"""
    float_a = 2.2
    float_b = 3.3
    f_product = float_a * float_b
    
    assert isinstance(float_a, float)
    assert isinstance(float_b, float)
    assert isinstance(f_product, float)
    assert round(f_product, 2) == 7.26


def test_string_type():
    """Verify string variable works correctly"""
    student = "Gary"
    
    assert isinstance(student, str)
    assert student == "Gary"


def test_boolean_type():
    """Verify boolean variable works correctly"""
    passed = False
    
    assert isinstance(passed, bool)
    assert passed == False