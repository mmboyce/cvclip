import StringIO
import os
import sys

import mock
import pyperclip

from cvclip import cli_helpers

src_path = os.path.join(os.path.dirname(__file__), '..', 'cvclip')


# TODO: Put setup and tear down functions up here

def mock_input(entry):
    print "Overwrite file? (Y/N): " + entry
    return entry


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
        print "Expected: " + to_copy
        print "Received: " + pyperclip.paste()
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
        print "Expected: Creation of " + test_file_path
        print "Received: File path does not exist"
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
        print "Expected: Creation of " + test_file_path
        print "Received: Creation of " + created_path
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
        print "Expected: Creation of " + test_file_path
        print "Received: Creation of " + created_path
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
        print "Expected: Creation of " + test_file_path
        print "Received: Creation of " + created_path
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
        print "Expected: Creation of " + test_file_path
        print "Received: Creation of " + created_path
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
        print "Expected: Creation of " + test_file_path
        print "Received: Creation of " + created_path
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_correct_content():
    test_file_path = os.path.join(src_path, "job_company.txt")
    did_it_work = True

    if os.path.exists(test_file_path):
        print "FILE SHOULD NOT EXIST YET: " + test_file_path
        assert False

    created_path = cli_helpers.create_new_file('job', 'company', 'content')
    print "\ncreated file: " + created_path

    if not os.path.exists(test_file_path):
        print "Expected: Creation of " + test_file_path
        print "Received: Creation of " + created_path
        did_it_work = False

    created_file = open(created_path, 'r')

    content = created_file.read()

    created_file.close()

    if 'content' != content and did_it_work:
        print "FILE CONTENTS NOT MATCHING INPUT"
        print "Expected: 'content'"
        print "Received: '" + content + "'"
        did_it_work = False

    os.remove(created_path)
    print "removed file: " + created_path

    assert did_it_work


def test_overwrite_file():
    with mock.patch('__builtin__.raw_input', side_effect=mock_input('y')):
        test_file_path = os.path.join(src_path, "job_company.txt")
        did_it_work = True

        if os.path.exists(test_file_path):
            print "FILE SHOULD NOT EXIST YET: " + test_file_path
            assert False

        created_path = cli_helpers.create_new_file('job', 'company', 'content')
        print "\ncreated file: " + created_path

        created_file = open(created_path, 'r')

        content1 = created_file.read()

        created_file.close()

        if not os.path.exists(test_file_path):
            print "Expected: Creation of " + test_file_path
            print "Received: Creation of " + created_path
            did_it_work = False

        cli_helpers.create_new_file('job', 'company', 'content2')

        created_file = open(created_path, 'r')

        content2 = created_file.read()

        created_file.close()

        if content1 == content2 and did_it_work:
            print "FILE WAS NOT OVERWRITTEN"
            print "Expected: " + content2
            print "Received: " + content1
            did_it_work = False

        os.remove(created_path)

        assert did_it_work


def test_file_not_overwritten():
    with mock.patch('__builtin__.raw_input', side_effect=mock_input('n')):
        test_file_path = os.path.join(src_path, "job_company.txt")
        did_it_work = True

        if os.path.exists(test_file_path):
            print "FILE SHOULD NOT EXIST YET: " + test_file_path
            assert False

        created_path = cli_helpers.create_new_file('job', 'company', 'content')
        print "\ncreated file: " + created_path

        created_file = open(created_path, 'r')
        content1 = created_file.read()
        created_file.close()

        if not os.path.exists(test_file_path):
            print "Expected: Creation of " + test_file_path
            print "Received: Creation of " + created_path
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
