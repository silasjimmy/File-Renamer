import os
from os import path


def main():
    if path.exists("Navigation.png"):
        src = path.realpath("Navigation.png")
        os.rename("Navigation.png", "Navigation Xyz.png")


if __name__ == '__main__':
    main()
