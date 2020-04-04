import os
from os import path


def main():
    file_dir = "/home/polo/Pictures/rename"
    if path.exists(file_dir):
        files = os.listdir(file_dir)
        png_files = [_ for _ in files if _[-4:] == ".png"]
        for file in png_files:
            print(file)


if __name__ == '__main__':
    main()
