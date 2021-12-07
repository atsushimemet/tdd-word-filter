from word_filter.word_filter import WordFilter


class TestWordFilter:
    def test_detect(self):
        word_filter = WordFilter("I am atsushi.")
        actual = word_filter.detect("atsushi")
        expected = True
        assert actual == expected
