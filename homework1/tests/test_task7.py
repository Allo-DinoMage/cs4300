import numpy as np
from src.task7 import calculateStats, multiplyArrays


def test_calculate_stats():
    numbers = [1, 2, 3, 4, 5]
    stats = calculateStats(numbers)
    
    # Check it returns a dictionary
    assert isinstance(stats, dict)
    
    # Check it has the right keys
    assert 'mean' in stats
    assert 'median' in stats
    assert 'std_dev' in stats
    
    # Check mean is correct (1+2+3+4+5 = 15, 15/5 = 3)
    assert stats['mean'] == 3.0
    
    # Check median is correct
    assert stats['median'] == 3.0


def test_calculate_stats_values():
    numbers = [10, 20, 30, 40, 50]
    stats = calculateStats(numbers)
    
    # Mean should be 30
    assert stats['mean'] == 30.0
    
    # Median should be 30
    assert stats['median'] == 30.0


def test_multiply_arrays():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    
    result = multiplyArrays(arr1, arr2)
    
    # Should get [1*4, 2*5, 3*6] = [4, 10, 18]
    assert result == [4, 10, 18]


def test_multiply_arrays_type():
    arr1 = [1, 2, 3]
    arr2 = [2, 2, 2]
    
    result = multiplyArrays(arr1, arr2)
    
    # Check it's a list
    assert isinstance(result, list)
    
    # Check correct values
    assert result == [2, 4, 6]