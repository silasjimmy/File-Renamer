import os
from os import path


def main():
    file_dir = "/home/polo/Pictures/Delvis Photos/whiskey/m--->>"
    if path.exists(file_dir):
        files = os.listdir(file_dir)
        png_files = [_ for _ in files if _[-5:] == ".jpeg"]
        for file in png_files:
            print(file.lower().replace(" ", "_"))


if __name__ == '__main__':
    main()
