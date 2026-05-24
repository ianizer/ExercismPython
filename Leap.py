"""Module for determining leap years."""


def leap_year(year: int) -> bool:
    """Returns true if given year is a leap year, or false otherwise"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
