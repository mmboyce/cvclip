import getopt
import os
import sys

import cli_helpers
import methods

HELP_STRING = """
Required flags:

At least one of the following must be used:
-c 'company title'
-p 'position title'

Optional flags:

-v or --verbose
    Prints the cover letter to the terminal. By default this is enabled, and is disabled if -n or
    -b are used. 
    If you still want the text printed to the terminal use this flag in conjunction with the others.

-n or --new
    Creates a new file in the cvclip folder with the the title format of 
    position_title_company_title.txt
    
    This will prevent printing to the terminal unless -v is used

-b or --clipboard
    Copies contents of the converted letter to your clipboard.

    This will prevent printing to the terminal unless -v is used 
"""

cover_path = os.path.join(os.path.dirname(__file__), "cover.txt")
cover_file = open(cover_path, "r")

cover_text = ""

for line in cover_file:
    cover_text = cover_text + line

cover_file.close()


def main():
    try:
        # req flags: -c -p
        opts, args = getopt.gnu_getopt(sys.argv[1:], "hp:c:vcn",
                                       ["help", "verbose", "clipboard", "new"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    def print_help():
        print HELP_STRING

        # Prevent any functionality when help is called
        sys.exit()

    verbose_toggled = False
    clipboard_toggled = False
    new_file_toggled = False
    company_title = ""
    position_title = ""

    used_position_flag = False
    used_company_flag = False

    for o, a in opts:
        if o in ["-v", "--verbose"]:
            verbose_toggled = True
        elif o == "-c":
            company_title = a
            used_company_flag = True
        elif o == "-p":
            position_title = a
            used_position_flag = True
        elif o in ["-h", "--help"]:
            print_help()
        elif o in ["-b", "--clipboard"]:
            clipboard_toggled = True
        elif o in ["-n", "--new"]:
            new_file_toggled = True

    if not used_company_flag and not used_position_flag:
        # This prevents any other methods from being run as at least 1 of -c and -p are required
        print_help()

    converted_cover = methods.replace_titles(company_title, position_title, cover_text)

    if verbose_toggled or (not clipboard_toggled and not new_file_toggled):
        cli_helpers.print_verbose(converted_cover)

    if clipboard_toggled:
        cli_helpers.copy_to_clipboard(converted_cover)

    if new_file_toggled:
        cli_helpers.create_new_file(position_title, company_title, converted_cover)


if __name__ == "__main__":
    main()
