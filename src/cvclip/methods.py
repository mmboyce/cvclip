def strip_comments(strip_text):
    """
    This method will remove the comments from the text provided

    :type strip_text: str
    :param strip_text: A string representing the text to remove comments from
    :rtype: str
    :return: A string with all comments removed
    """
    lines = strip_text.split("\n")

    stripped = ""

    # This line checks if the first line of the file is a comment.
    # This flag will be used to determine once the comment block ends.
    # Once the block is end and is set to false, then
    comment_block = lines[0][0] == "#"

    for line in lines:
        if comment_block:
            if len(line) > 0 and line[0] == "#":
                # do nothing :)
                continue
            else:
                comment_block = False

        if len(line) == 0:
            stripped = stripped + "\n"
        else:
            stripped = stripped + line + "\n"

    return stripped


def replace_titles(company_title, position_title, not_replaced):
    """
    This method will replace company title placeholders ($CT) and position title placeholders ($PT)
    found in the text. It will first strip it of comments and then alter what is left.

    :type company_title: str
    :param company_title: A string representing the title of the company to replace instances of $CT
    :type position_title: str
    :param position_title: A string representing the title of the position to replace instances of $PT
    :type not_replaced: str
    :param not_replaced: A string representing the text that needs its placeholders replaced
    :rtype: str
    :return: A string with all placeholders replaced
    """
    stripped = strip_comments(not_replaced)
    replaced = ""

    replaced_position = stripped.replace("$PT", position_title)
    replaced_title = replaced_position.replace("$CT", company_title)

    replaced = replaced + replaced_title

    return replaced
