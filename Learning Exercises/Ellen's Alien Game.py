"""Solution to Ellen's Alien Game exercise."""

ALIEN_DEFAULT_HEALTH = 3


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        Alien.total_aliens_created += 1

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = ALIEN_DEFAULT_HEALTH

    def hit(self) -> None:
        self.health -= 1

    def is_alive(self) -> bool:
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        pass


def new_aliens_collection(alien_positions_to_spawn: list[tuple]) -> list:
    """Returns a list of new Alien objects using the given coordinate tuples."""

    new_aliens = []

    for x_pos, y_pos in alien_positions_to_spawn:
        new_aliens.append(Alien(x_pos, y_pos))

    return new_aliens
