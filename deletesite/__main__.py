"""Main file that will be run when the command `python deletesite` is ran
"""

from .settings import load_settings

if __name__ == "__main__":
    load_settings()

    name = input("What is your name? ")

    print(f"Hello {name}")
