#!/usr/bin/python3

def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    # Get the object's dictionary of attributes and methods
    attrs = dir(obj)
    # Return the list of attributes
    return attrs
