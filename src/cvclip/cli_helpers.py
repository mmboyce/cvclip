import pyperclip
import os


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
        title = os.path.join(os.path.dirname(__file__), title)

        new_cover_file = open(title, "w")
        new_cover_file.write(conversion)
        new_cover_file.close()

        return title

    position = convert_spaces_to_underscores(position)
    company = convert_spaces_to_underscores(company)

    file_title = position + "_" + company + ".txt"
    file_path = ""

    if os.path.exists(file_title):
        print("WARNING: FILE ALREADY EXISTS")
        response = raw_input("Overwrite file? (Y/N)")
        if response.lower() == "y":
            os.remove(file_title)
            file_path = write_cover_file(file_title)
        else:
            print "Overwrite aborted."
            file_path = "NO FILE CREATED"
    else:
        file_path = write_cover_file(file_title)

    return file_path
