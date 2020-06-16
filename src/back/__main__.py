from sys import stdin
from time import sleep

from src.back.lib import clean_text


if __name__ == "__main__":
    sleep(30)
    print(clean_text(stdin.read()))
