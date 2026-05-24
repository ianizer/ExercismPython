"""Functions for determining the type of triangle."""

from typing import Sequence


def is_triangle(sides: Sequence[int]) -> bool:
    """Return True if the given sides form a valid triangle, and False otherwise."""

    return (
        len(sides) == 3
        and sides[0] > 0
        and sides[1] > 0
        and sides[2] > 0
        and sides[0] + sides[1] >= sides[2]
        and sides[0] + sides[2] >= sides[1]
        and sides[1] + sides[2] >= sides[0]
    )


def equilateral(sides: Sequence[int]) -> bool:
    """Return True if the given sides form an equilateral triangle, and False otherwise."""

    return is_triangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides: Sequence[int]) -> bool:
    """Return True if the given sides form an isosceles triangle, and False otherwise."""

    return is_triangle(sides) and (sides[0] in sides[1:] or sides[1] in sides[::2])
    # If we wanted exactly two sides (how I learned isosceles), then we could do:
    # return not equilateral(sides) and (sides[0] in sides[1:] or sides[1] in sides[::2])


def scalene(sides: Sequence[int]) -> bool:
    """Return True if the given sides form a scalene triangle, and False otherwise."""

    return (
        is_triangle(sides)
        and (sides[0] not in sides[1:])
        and (sides[1] not in sides[::2])
    )


# The extra function mentioned, though not required by, the exercise.
# I have not tested this function.
def degenerate(sides: Sequence[int]) -> bool:
    """Return True if the given sides form a degenerate triangle, and False otherwise."""

    return (
        len(sides) == 3
        and sides[0] > 0
        and sides[1] > 0
        and sides[2] > 0
        and (
            sides[0] + sides[1] == sides[2]
            or sides[0] + sides[2] == sides[1]
            or sides[1] + sides[2] == sides[0]
        )
    )
