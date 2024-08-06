# The code provided is supposed return a person's Full Name given their first and last names.
#
# But it's not working properly.
#
# Notes
#
# The first and/or last names are never null, but may be empty.
#
# Task
#
# Fix the bug so we can all go home early.


class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        if not self.first_name:
            return self.last_name
        if not self.last_name:
            return self.first_name


class Dinglemouse2(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        return (self.first_name + ' ' + self.last_name).strip()