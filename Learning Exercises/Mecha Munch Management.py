"""Functions to manage a users shopping cart items."""

from typing import Iterable


def add_item(current_cart: dict, items_to_add: Iterable) -> dict:
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart


def read_notes(notes: Iterable) -> dict:
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    return {}.fromkeys(notes, 1)


def update_recipes(ideas: dict, recipe_updates: Iterable[tuple]) -> dict:
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    ideas |= recipe_updates

    return ideas


def sort_entries(cart: dict) -> dict:
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict) -> dict:
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    # Create extra dictionary so that only necesseary information is returned.
    # Surely there is a better way I can't think of right now.
    store_mapping = {}

    for item in cart:
        aisle_mapping[item].insert(0, cart[item])
        store_mapping[item] = aisle_mapping[item]

    return dict(reversed(sorted(store_mapping.items())))


def update_store_inventory(fulfillment_cart: dict, store_inventory: dict) -> dict:
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for item_name in fulfillment_cart:
        quantity_in_stock = store_inventory[item_name][0]
        number_purchased = fulfillment_cart[item_name][0]

        if quantity_in_stock - number_purchased <= 0:
            # Update actual quantiy to be "Out of Stock"
            store_inventory[item_name][0] = "Out of Stock"
        else:
            store_inventory[item_name][0] -= number_purchased

    return store_inventory
