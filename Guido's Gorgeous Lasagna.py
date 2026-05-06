"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40  # minutes to bake lasagna
PREPARATION_TIME = 2  # minutes to prep a layer of the lasagna


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate prep time.

    :param number_of_layers: int - number of layers to prepare.
    :return: int - time in minutes to prepare layers for baking, derived from `PREPARATION_TIME`.

    Function that takes the number of layers to be made as an argument and returns the number of minutes preparing all layers will take based on the `PREPARATION_TIME`.
    """

    return number_of_layers * PREPARATION_TIME


# TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate total elapsed time.

    :param number_of_layers: int - number of layers already prepped.
    :param elapsed_bake_time: int - time spent baking in oven so far.

    Function that takes number of layers and time spent baking, and computes the total time spent producing lasagna, utilizing the preparation_time_in_minutes() function.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time