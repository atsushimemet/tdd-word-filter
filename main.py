"""main"""
from logging import config

from word_filter.word_filter import WordFilter

config.fileConfig("logging.conf", disable_existing_loggers=False)

if __name__ == "__main__":
    WordFilter("test")
