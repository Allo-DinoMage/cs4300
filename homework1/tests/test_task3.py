

from src.task3 import check_number, first_10_primes, sum_1_to_100


def test_check_number_positive(capsys):
    check_number(5)
    captured = capsys.readouterr()
    assert "positive" in captured.out


def test_check_number_negative(capsys):
    check_number(-3)
    captured = capsys.readouterr()
    assert "negative" in captured.out


def test_check_number_zero(capsys):
    check_number(0)
    captured = capsys.readouterr()
    assert "zero" in captured.out


def test_first_10_primes(capsys):
    first_10_primes()
    captured = capsys.readouterr()
    
    # Check that all first 10 primes appear in output
    expected_primes = ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29"]
    for prime in expected_primes:
        assert prime in captured.out


def test_sum_1_to_100(capsys):
    sum_1_to_100()
    captured = capsys.readouterr()
    
    # 1+2+...+100 = 5050
    assert "5050" in captured.out