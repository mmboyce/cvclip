import StringIO
import sys
import pyperclip
import os
import __builtin__
from mock import patch
from cvclip import cli_helpers


src_path = os.path.join(os.path.dirname(__file__), '..', 'cvclip')


def test_print_verbose():
    fake_cover = "This is my cover letter"
    # Capture stdout to test!
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output

    cli_helpers.print_verbose(fake_cover)

    # clear the stdout redirect
    sys.stdout = sys.__stdout__

    # add a new line because print ends in a new line
    assert fake_cover + "\n" == captured_output.getvalue()


def test_copy_to_clipboard():
    # This will ensure the clipboard is as it was before the test after it is run
    hold_clipboard = pyperclip.paste()
    did_it_work = True

    to_copy = "This will be in the clipboard"
    cli_helpers.copy_to_clipboard(to_copy)
    if to_copy != pyperclip.paste():
        did_it_work = False

    # Reset clipboard to its state before the test
    pyperclip.copy(hold_clipboard)

    assert did_it_work


def test_create_new_file():
    test_file_path = os.path.join(src_path, "job_company.txt")
    did_it_work = True

    if os.path.exists(test_file_path):
        print "FILE SHOULD NOT EXIST YET: " + test_file_path
        assert False

    created_path = cli_helpers.create_new_file('job', 'company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_spaces_to_underscores():
    test_file_path = os.path.join(src_path, "job_title_company_title.txt")
    did_it_work = True

    if os.path.exists(test_file_path):
        print "FILE SHOULD NOT EXIST YET: " + test_file_path
        assert False

    created_path = cli_helpers.create_new_file('job title', 'company title', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_trailing_position_spaces_to_single_underscore():
    test_file_path = os.path.join(src_path, "job_company.txt")
    did_it_work = True

    if os.path.exists(test_file_path):
        print "FILE SHOULD NOT EXIST YET: " + test_file_path
        assert False

    created_path = cli_helpers.create_new_file('job ', 'company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_multiple_spaces_between_words_to_single_underscore():
    test_file_path = os.path.join(src_path, "job_company.txt")
    did_it_work = True

    if os.path.exists(test_file_path):
        print "FILE SHOULD NOT EXIST YET: " + test_file_path
        assert False

    created_path = cli_helpers.create_new_file('job ', ' company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_spaces_at_end_of_company_title_removed():
    test_file_path = os.path.join(src_path, "job_company.txt")
    did_it_work = True

    if os.path.exists(test_file_path):
        print "FILE SHOULD NOT EXIST YET: " + test_file_path
        assert False

    created_path = cli_helpers.create_new_file('job', 'company ', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_multiple_spaces_together_to_single_underscore():
    test_file_path = os.path.join(src_path, "job_company.txt")
    did_it_work = True

    if os.path.exists(test_file_path):
        print "FILE SHOULD NOT EXIST YET: " + test_file_path
        assert False

    created_path = cli_helpers.create_new_file('job', '  company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


@patch.object(__builtin__, 'raw_input')
def test_overwrite_file(mock_raw_input_value):
    # TODO: mock raw input to use "y"
    assert False


@patch.object(__builtin__, 'raw_input')
def test_file_not_overwritten():
    # TODO: mock raw input to use "n"
    assert False
