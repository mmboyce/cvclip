def strip_comments(strip_text):
    lines = strip_text.split("\n")

    stripped = ""

    # This line checks if the first line of the file is a comment.
    # This flag will be used to determine once the comment block ends.
    # Once the block is end and is set to false, then
    comment_block = lines[0][0] == "#"

    for line in lines:
        if comment_block:
            if  len(line) > 0 and line[0] == "#":
                # do nothing :)
                continue
            else:
                comment_block = False

        if len(line) == 0:
            stripped = stripped + "\n"
        else:
            stripped = stripped + line

    return stripped


def replace_titles(position_title, company_title, not_replaced):
    return False