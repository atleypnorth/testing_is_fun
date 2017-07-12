import os


def format_name(first, middle, last, title=''):
    return '%s %s %s %s' % (first, middle, last, title)


def name_and_user_id():
    return os.getlogin()
    