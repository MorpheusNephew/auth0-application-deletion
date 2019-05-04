"""Main file that will be run when the command `python .` is ran
"""

from deletesite.utilities import load_settings

if __name__ == "__main__":
    load_settings()

    name = input("What is your name? ")

    print(f"Hello {name}")
