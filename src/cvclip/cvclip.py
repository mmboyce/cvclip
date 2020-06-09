import pyperclip
import getopt
import methods
from os import path

cover_path = path.join(path.dirname(__file__), "cover.txt")
cover_file = open(cover_path, "r")

cover_text = ""

for line in cover_file:
    cover_text = cover_text + line

cover_file.close()