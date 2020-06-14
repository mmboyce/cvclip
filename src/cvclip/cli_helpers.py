import os

import pyperclip

src_path = os.path.dirname(__file__)


def print_verbose(conversion):
    print conversion
    return conversion


def copy_to_clipboard(conversion):
    pyperclip.copy(conversion)


def create_new_file(position, company, conversion):
    def convert_spaces_to_underscores(title):
        # add check for trailing spaces and strip them
        return title.replace(" ", "_")

    def write_cover_file(title):
        # This makes sure the file is written to the cvclip directory

        new_cover_file = open(title, "w")
        new_cover_file.write(conversion)
        new_cover_file.close()

        return title

    position = convert_spaces_to_underscores(position)
    company = convert_spaces_to_underscores(company)

    file_title = position + "_" + company + ".txt"
    file_path = os.path.join(src_path, file_title)

    if os.path.exists(file_path):
        print "WARNING: FILE ALREADY EXISTS"
        response = raw_input("Overwrite file? (Y/N)")
        if response.lower() == "y":
            os.remove(file_path)
            file_path = write_cover_file(file_path)
            print "File overwritten: " + file_title
        else:
            print "Overwrite aborted."
    else:
        file_path = write_cover_file(file_path)

    return file_path
