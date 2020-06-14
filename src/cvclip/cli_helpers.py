import os

import pyperclip

# The path to the src folder where cover letters are saved
src_path = os.path.dirname(__file__)


def print_verbose(conversion):
    """
    This method prints the converted text to the terminal. This is mostly here for readability purposes.

    -v or --verbose

    print_verbose will run by default if no options besides the required options are included.
    If a flag such as clipboard or new is used then this will only run if its option is used as well.

    :param conversion: A string representing text to be printed
    :return: A string represented the printed text.
    """
    print conversion
    return conversion


def copy_to_clipboard(conversion):
    """
    This method will copy the converted text to the user's clipboard. This is mostly here for readability
    purposes.

    -c or --clipboard

    copy_to_clipboard will prevent verbose from running unless it is specifically included with user input.

    :param conversion: A string to copy to the clipboard.
    """
    pyperclip.copy(conversion)


def create_new_file(position, company, conversion):
    """
    This method will create a file with the format of position_company.txt

    -n or --new

    create_new_file will prevent verbose from running unless it is specifically included with user input.

    :param position: A string representing the title of the position
    :param company: A string representing the title of the company
    :param conversion: A string representing the contents of the cover letter
    :return: A string representing the path to the newly created file
    """

    def convert_spaces_to_underscores(title):
        """
        This helper method will convert spaces in the title (company or position) to underscores.

        It will also remove spaces on the ends of position titles, as well as convert multiple neighboring
        spaces in the titles to single underscores.

        :param title: A string representing the title of either a company or position
        :return: A string that has been formatted to convert spaces to underscores.
        """
        # TODO: handle leading, trailing and repeated spaces
        title = title.replace(" ", "_")

        return title

    def write_cover_file(title):
        """
        This helper method will create a new file with the converted contents of the cover letter
        and name it the provided title.

        :param title: A string representing the title of the file
        :return: The path to the newly created file
        """

        new_cover_file = open(title, "w")
        new_cover_file.write(conversion)
        new_cover_file.close()

        return title

    position = convert_spaces_to_underscores(position)
    company = convert_spaces_to_underscores(company)

    file_title = position + "_" + company + ".txt"

    # This makes sure the file is written to the cvclip directory
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
