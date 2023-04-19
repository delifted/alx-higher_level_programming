#!/usr/bin/python3

def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    # Get the object's dictionary of attributes and methods
    attrs = dir(obj)
    # Filter out any private or special attributes
    attrs = [attr for attr in attrs if not attr.startswith('__')]
    # Return the list of attributes
    return attrs
