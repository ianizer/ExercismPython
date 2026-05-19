"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args: int) -> list[int]:
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """

    # args is a tuple. Must convert to list.
    return list(args)


def fix_list_of_wagons(
    each_wagons_id: list[int], missing_wagons: list[int]
) -> list[int]:
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """

    # Shift first two elements of first list to end of first list.
    first_id, second_id, id_one, *other_ids = each_wagons_id

    corrected_ids = [id_one] + missing_wagons + other_ids + [first_id, second_id]

    return corrected_ids


def add_missing_stops(route: dict, **kwargs) -> dict:
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """

    route["stops"] = list(kwargs.values())

    return route


def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """

    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: list[list[tuple]]) -> list:
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """

    return list(list(row) for row in zip(*wagons_rows))
