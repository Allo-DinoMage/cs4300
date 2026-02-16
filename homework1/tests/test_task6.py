from src.task6 import countWords


def test_count_words():
    wordCount = countWords("task6_read_me.txt")
    
    # The Lorem Ipsum text has 127 words
    assert wordCount == 127


def test_count_words_positive():
    wordCount = countWords("task6_read_me.txt")
    assert wordCount > 0


def test_count_words_is_integer():
    wordCount = countWords("task6_read_me.txt")
    assert isinstance(wordCount, int)