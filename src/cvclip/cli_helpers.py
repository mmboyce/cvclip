import os
import re
import sys

import pyperclip

# The path to the src folder where cover letters are saved
src_path = os.path.dirname(__file__)


def print_verbose(conversion):
    """
    This method prints the converted text to the terminal. This is mostly here for readability purposes.

    -v or --verbose

    print_verbose will run by default if no options besides the required options are included.
    If a flag such as clipboard or new is used then this will only run if its option is used as well.

    :type conversion: str
    :param conversion: A string representing text to be printed
    :rtype: str
    :return: A string represented the printed text.
    """
    print conversion
    return conversion


def copy_to_clipboard(conversion):
    """
    This method will copy the converted text to the user's clipboard. This is mostly here for readability
    purposes.

    -b or --clipboard

    copy_to_clipboard will prevent verbose from running unless it is specifically included with user input.

    :type conversion: str
    :param conversion: A string to copy to the clipboard.
    """
    pyperclip.copy(conversion)


def create_new_file(position, company, conversion):
    """
    This method will create a file with the format of position_company.txt

    -n or --new

    create_new_file will prevent verbose from running unless it is specifically included with user input.

    :type company: str
    :param company: A string representing the title of the company
    :type position: str
    :param position: A string representing the title of the position
    :type conversion: str
    :param conversion: A string representing the contents of the cover letter
    :rtype: str
    :return: A string representing the path to the newly created file
    """

    def convert_spaces_to_underscores(title):
        """
        This helper method will convert spaces in the title (company or position) to underscores.

        It will also remove spaces on the ends of position titles, as well as convert multiple neighboring
        spaces in the titles to single underscores.

        :type title: str
        :param title: A string representing the title of either a company or position
        :rtype: str
        :return: A string that has been formatted to convert spaces to underscores.
        """

        # Strip leading and trailing spaces
        title = title.lstrip()
        title = title.rstrip()

        # Regex to reduce repeated spaces to a single space
        title = re.sub(' +', ' ', title)
        title = title.replace(" ", "_")

        return title

    def write_cover_file(title):
        """
        This helper method will create a new file with the converted contents of the cover letter
        and name it the provided title.

        :type title: str
        :param title: A string representing the title of the
        :rtype: str
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
        print "Overwrite file? (Y/N)"

        # Fixes issue with prompt appearing before any information is printed
        sys.stdout.flush()

        response = raw_input()

        if response.lower() == "y":
            os.remove(file_path)
            file_path = write_cover_file(file_path)
            print "\nFile overwritten: " + file_title
        else:
            print "\nOverwrite aborted."
    else:
        file_path = write_cover_file(file_path)

    return file_path
