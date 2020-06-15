"""
Many of the tests in this file are written such that a boolean "did_it_work" will determine if the test
failed. This is to make sure that in the instance of a failed test, a reason will be supplied at the
check that caused it to fail and that any created files will be cleared before the failure is triggered.

If this was not done, a failed test after checking a file would leave the file created for the test
still in the folder. This would prevent re-runs of tests until the file wsa manually removed.
"""

import StringIO
import os
import sys

import mock
import pyperclip

from cvclip import cli_helpers

# The path to the src folder where cover letters are saved
cvclip_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cvclip')


def mock_input(entry):
    """
    This helper will be used as a mock patch side effect to represent user input for overwrite tests.
    It will print the prompt that the user encounters when overwriting for clarity when viewing test
    results.

    :type entry: str
    :param entry: A string representing user input
    :rtype: str
    :return: A string simulating user input
    """
    print "Overwrite file? (Y/N): " + entry
    return entry


# These constants are used for repeated statements in the print_except_receive to make sure spelling
# and formatting is always consistent.

CREATION_OF = "Creation of: "
FILE_DOES_NOT_EXIST = "File path does not exist"


def print_expect_receive(expected, received):
    """
    This helper will be used whenever the test has indicated that something failed. It will notify the
    tester the expected value and what was received in this format

    Expected: {expected}
    Received: {received}

    :type expected:  str
    :param expected: A string representing what the expected outcome was
    :type received: str
    :param received: A string representing what the received outcome was
    """

    print "Expected: " + expected
    print "Received: " + received


def check_if_path_already_exists(file_path):
    """
    This helper will be used to check if file paths are already being used.
    It will immediately assert false in that case.
    It must be assigned so that it will convert the path to absolute.

    We cannot perform a test if a file is occupying the path needed for the test, and we do not
    want to assume it is accidentally there.

    If the path does not exist yet, we will return it.

    :type file_path: str
    :param file_path: A string representing the filename to check
    :rtype: str
    :return: A string representing the file path if the path does not exist yet
    """
    # This path is unambiguous as to the absolute location of the text file.
    test_file_path = os.path.join(cvclip_path, file_path)

    if os.path.exists(file_path):
        print "FILE SHOULD NOT EXIST YET: " + file_path
        assert False

    return test_file_path


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
        print "Text was not copied correctly"
        print_expect_receive(to_copy, pyperclip.paste())
        did_it_work = False

    # Reset clipboard to its state before the test
    pyperclip.copy(hold_clipboard)

    assert did_it_work


def test_create_new_file():
    test_file_path = check_if_path_already_exists('job_company.txt')
    did_it_work = True

    created_path = cli_helpers.create_new_file('job', 'company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        print_expect_receive(CREATION_OF + test_file_path, FILE_DOES_NOT_EXIST)
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_spaces_to_underscores():
    test_file_path = check_if_path_already_exists("job_title_company_title.txt")
    did_it_work = True

    created_path = cli_helpers.create_new_file('job title', 'company title', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        print_expect_receive(CREATION_OF + test_file_path, CREATION_OF + created_path)
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_trailing_position_spaces_to_single_underscore():
    test_file_path = check_if_path_already_exists("job_company.txt")
    did_it_work = True

    created_path = cli_helpers.create_new_file('job ', 'company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        print_expect_receive(CREATION_OF + test_file_path, CREATION_OF + created_path)
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_multiple_spaces_between_words_to_single_underscore():
    test_file_path = check_if_path_already_exists("job_company.txt")
    did_it_work = True

    created_path = cli_helpers.create_new_file('job ', ' company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        print_expect_receive(CREATION_OF + test_file_path, CREATION_OF + created_path)
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_spaces_at_end_of_company_title_removed():
    test_file_path = check_if_path_already_exists("job_company.txt")
    did_it_work = True

    created_path = cli_helpers.create_new_file('job', 'company ', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        print_expect_receive(CREATION_OF + test_file_path, CREATION_OF + created_path)
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_multiple_spaces_together_to_single_underscore():
    test_file_path = check_if_path_already_exists("job_company_title.txt")
    did_it_work = True

    created_path = cli_helpers.create_new_file('job', 'company   title', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        print_expect_receive(CREATION_OF + test_file_path, CREATION_OF + created_path)
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_correct_content():
    test_file_path = check_if_path_already_exists("job_company.txt")
    did_it_work = True

    created_path = cli_helpers.create_new_file('job', 'company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        print_expect_receive(CREATION_OF + test_file_path, CREATION_OF + created_path)
        did_it_work = False

    created_file = open(created_path, 'r')

    content = created_file.read()

    created_file.close()

    if 'content' != content and did_it_work:
        print "FILE CONTENTS NOT MATCHING INPUT"
        print_expect_receive("'content'", "'" + content + "'")
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_overwrite_file():
    with mock.patch('__builtin__.raw_input', side_effect=mock_input('y')):
        test_file_path = check_if_path_already_exists("job_company.txt")
        did_it_work = True

        created_path = cli_helpers.create_new_file('job', 'company', 'content')
        print "\ncreated file: " + created_path

        created_file = open(created_path, 'r')

        content1 = created_file.read()

        created_file.close()

        if not os.path.exists(test_file_path):
            print_expect_receive(CREATION_OF + test_file_path, CREATION_OF + created_path)
            did_it_work = False

        cli_helpers.create_new_file('job', 'company', 'content2')

        created_file = open(created_path, 'r')

        content2 = created_file.read()

        created_file.close()

        if content1 == content2 and did_it_work:
            print "FILE WAS NOT OVERWRITTEN"
            print_expect_receive(content2, content1)
            did_it_work = False

        os.remove(created_path)

        assert did_it_work


def test_file_not_overwritten():
    with mock.patch('__builtin__.raw_input', side_effect=mock_input('n')):
        test_file_path = check_if_path_already_exists("job_company.txt")
        did_it_work = True

        created_path = cli_helpers.create_new_file('job', 'company', 'content')
        print "\ncreated file: " + created_path

        created_file = open(created_path, 'r')
        content1 = created_file.read()
        created_file.close()

        if not os.path.exists(test_file_path):
            print_expect_receive(CREATION_OF + test_file_path, CREATION_OF + created_path)
            did_it_work = False

        cli_helpers.create_new_file('job', 'company', 'content2')

        created_file = open(created_path, 'r')
        content2 = created_file.read()
        created_file.close()

        if content1 != content2 and did_it_work:
            print "FILE WAS OVERWRITTEN"
            did_it_work = False
        os.remove(created_path)

        assert did_it_work
