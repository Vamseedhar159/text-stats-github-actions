from text_stats import word_count, char_count

def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("") == 0

def test_char_count():
    assert char_count("hello") == 5
    assert char_count("") == 0
