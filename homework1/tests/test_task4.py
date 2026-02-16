import pytest
from src.task4 import calculate_discount


def test_with_integers():
    """Duck typing: Both are integers"""
    result = calculate_discount(100, 10)
    assert result == 90.0


def test_with_floats():
    """Duck typing: Both are floats"""
    result = calculate_discount(100.0, 10.0)
    assert result == 90.0


def test_mixed_int_and_float():
    """Duck typing: Mix of int and float"""
    # Integer price, float discount
    result = calculate_discount(100, 10.5)
    assert result == 89.5
    
    # Float price, integer discount
    result = calculate_discount(100.5, 10)
    assert result == 90.45


def test_zero_discount():
    """Edge case: No discount"""
    result = calculate_discount(100, 0)
    assert result == 100


def test_full_discount():
    """Edge case: 100% discount"""
    result = calculate_discount(100, 100)
    assert result == 0


def test_invalid_price_type():
    """Should reject non-numeric price"""
    with pytest.raises(TypeError):
        calculate_discount("100", 10)


def test_invalid_discount_type():
    """Should reject non-numeric discount"""
    with pytest.raises(TypeError):
        calculate_discount(100, "10")