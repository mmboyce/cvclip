import pytest
from cvclip import methods

def test_comments_ignored():
    stripped = methods.strip_comments("#\n#\nYes")
    assert "Yes" == stripped

def test_separated_comments_not_ignored():
    stripped = methods.strip_comments("#\n\n#Yes")
    assert "\n#Yes" == stripped

def test_placeholders_replaced():
    replaced = methods.replace("Home", "Cool Guy", "#\n$CT is such a nice place. I would like to be a $PT at $CT")
    assert "Home is such a nice place. I would like to be a Cool Guy at Home" == replaced
