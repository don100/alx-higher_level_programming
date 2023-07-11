#!/usr/bin/python3
"""101-add_attribute.py"""


def add_attribute(obj, name, value):
    """add_attribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
