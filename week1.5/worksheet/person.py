# Worksheet 1.5: Person class
'''Person class returns initials and checks whether today is their birthday.'''
from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
        '''
        Creates a Person, given values for name and date of birth.
        '''
        self.name = name
        self.birth = date.fromisoformat(birth)
    def initials(self):
        '''
        Returns the initials of the Person's name.
        '''
        words = self.name.split()
        initials = ""
        for word in words:
            initials += word[0].upper()
        return initials
    def is_birthday(self):
        '''
        Returns True if today is the Person's birthday, False otherwise.
        '''
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
