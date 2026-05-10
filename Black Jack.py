"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

ACE_MIN_VALUE = 1
ACE_MAX_VALUE = 11
FACE_CARD_VALUE = 10


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    match card:
        case "A":
            return ACE_MIN_VALUE
        case "J" | "Q" | "K":
            return FACE_CARD_VALUE
        case _:
            return int(card)
        # assuming card will be a number if not in ('A', 'J', 'Q', 'K').


def higher_card(card_one: str, card_two: str) -> str | tuple:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value == card_two_value:
        return card_one, card_two  # returns tuple, (card_one, card_two)
    if card_one_value > card_two_value:
        return card_one
    return card_two  # card_two necessarily greater than card_one at this point.


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    hand_value = value_of_card(card_one) + value_of_card(card_two)

    # ("A" in (card_one, card_two)) is necessary because value_of_card() returns 1 for Ace cards.
    if (hand_value + ACE_MAX_VALUE > 21) or ("A" in (card_one, card_two)):
        return ACE_MIN_VALUE
    return ACE_MAX_VALUE


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    hand = (card_one, card_two)
    ten_cards = ("J", "Q", "K", "10")

    return (
        hand[0] != hand[1]
        and "A" in hand
        and (hand[0] in ten_cards or hand[1] in ten_cards)
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    hand_sum = value_of_card(card_one) + value_of_card(card_two)

    return 9 <= hand_sum <= 11
