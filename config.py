# Author:   John Marcoux
# Date:     2019/11/28
# Version:  1.0
# Purpose:  Not yet implemented key-bind config library

"""
Name:       KeyConfig
Purpose:    See top file comment
Notes       None
"""
class KeyConfig:
    """
    Name:       __init__
    Purpose:    Initializes the KeyConfig object
    Arguments:  None
    Output:     None
    Modifies:   Creates the object and an empty dict within the object
    Returns:    The object
    Assumptions:None
    Bugs:       None
    """
    def __init__(self):
        self.key_binds = {}

    """
    Name:       add_key_bind
    Purpose:    Allows adding a key-bind to the object
    Arguments:  The key and sound name
    Output:     None
    Modifies:   Changes the key_bind dict
    Returns:    False if the key is already bound, True if the key was 
                successfully bound to the new sound
    Assumptions:Only one sound can be bound to a key, key-binds can only have a
                one key trigger
    Bugs:       None
    """
    def add_key_bind(self, key, sound_name):
        try:
            self.key_binds[key]
            return False
        except:
            self.key_binds[key] = sound_name
            return True

    """
    Name:       rem_key_bind
    Purpose:    Removes a key bind if it exists
    Arguments:  The key to unbind
    Output:     None
    Modifies:   See purpose
    Returns:    True
    Assumptions:None
    Bugs:       None
    """
    def rem_key_bind(self, key):
        try:
            del self.key_binds[key]
            return True
        except:
            return True
