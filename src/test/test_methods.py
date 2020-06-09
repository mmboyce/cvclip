from cvclip import methods


def test_comments_ignored():
    stripped = methods.strip_comments("#\n#\nYes")
    assert stripped == "Yes"


def test_separated_comments_not_ignored():
    stripped = methods.strip_comments("#\n\n#Yes")
    assert stripped == "\n#Yes"


def test_placeholders_replaced():
    replaced = methods.replace_titles("Home", "Cool Guy", "#\n$CT is such a nice place. I would like to be a $PT at $CT")
    assert replaced == "Home is such a nice place. I would like to be a Cool Guy at Home"
