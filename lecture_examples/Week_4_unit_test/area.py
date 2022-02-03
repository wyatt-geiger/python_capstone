"""
Functions for computing areas of various shapes
"""

def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError('Base and height must be greater than 0')
        # this if statement is coded to raise a ValueError message
        # used for the test_negative_base_height_raises_value_error function
    return height * base * 0.5