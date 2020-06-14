import getopt
import methods
import sys
from cli_helpers import *

cover_path = os.path.join(os.path.dirname(__file__), "cover.txt")
cover_file = open(cover_path, "r")

cover_text = ""

for line in cover_file:
    cover_text = cover_text + line

cover_file.close()


def main():
    try:
        # TODO Put in opt flags!!
        # req flags: -c -p
        opts, args = getopt.gnu_getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    company_title = "input for -c"  # TODO
    position_title = "input for -p"  # TODO
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
