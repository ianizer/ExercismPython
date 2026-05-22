"""Functions to automate Conda airlines ticketing system."""

from typing import Generator

SEAT_LETTERS = ("A", "B", "C", "D")
ROWS_TO_SKIP = (13,)  # tuple used so more rows can be added later, if desired.


def generate_seat_letters(number: int) -> Generator[str]:
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    next_letter_number = 0

    while number > 0:
        yield SEAT_LETTERS[next_letter_number]

        # % (number of seat letters) so that we never go out of bounds of the tuple.
        # Also produces the desired cycle of letters.
        next_letter_number = (next_letter_number + 1) % len(SEAT_LETTERS)

        number -= 1


def generate_seats(number: int) -> Generator[str]:
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    row_number = 1
    num_seat_letters = len(SEAT_LETTERS)

    for loop_counter, letter in enumerate(generate_seat_letters(number), 1):
        yield f"{row_number}{letter}"

        # Every "num_seat_letters", we must increment the row number.
        # I.e. we have used all seat letters for the current row, so go to the next row.
        if loop_counter % num_seat_letters == 0:
            row_number += 1
            while row_number in ROWS_TO_SKIP:
                row_number += 1


def assign_seats(passengers: list[str]) -> dict:
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    # The zip yields an *iterator* of tuples of the form (name, seat),
    #  which is perfect for making a dictionary from
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers: list[str], flight_id: str) -> Generator[str]:
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield f"{seat + flight_id:0<12}"
