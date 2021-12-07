"""word filter"""
from logging import getLogger

logger = getLogger(__name__)


class WordFilter:
    """
    WordFilter class
    """

    def __init__(self, word: str):
        self.word = word

    def detect(self, detected_word: str) -> bool:
        """Return a detected result"""
        logger.info("detecting...")
        return detected_word in self.word
