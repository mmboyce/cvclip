import pyperclip
import getopt
import methods
import sys
import os

cover_path = os.path.join(os.path.dirname(__file__), "cover.txt")
cover_file = open(cover_path, "r")

cover_text = ""

for line in cover_file:
    cover_text = cover_text + line

cover_file.close()


def main():
    def print_verbose(conversion):
        print conversion

    def copy_to_clipboard(conversion):
        pyperclip.copy(conversion)

    def create_new_file(position, company, conversion):
        def convert_spaces_to_underscores(title):
            # add check for trailing spaces and strip them
            return title.replace(" ", "_")

        def write_cover_file(title):
            new_cover_file = open(title, "w")
            new_cover_file.write(conversion)
            new_cover_file.close()

        position = convert_spaces_to_underscores(position)
        company = convert_spaces_to_underscores(company)

        file_title = position + "_" + company + ".txt"

        if os.path.exists(file_title):
            print("WARNING: FILE ALREADY EXISTS")
            response = raw_input("Overwrite file? (Y/N)")
            if response.lower() == "y":
                write_cover_file(file)
            else:
                print "Overwrite aborted."
                return
        else:
            write_cover_file(file_title)

    try:
        # TODO Put in opt flags!!
        # req flags: -c -p
        opts, args = getopt.gnu_getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)


    company_title =  "input for -c" #TODO
    position_title = "input for -p" #TODO
    converted_cover = methods.replace_titles(company_title, position_title, cover_text)

    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    # ...


if __name__ == "__main__":
    main()
