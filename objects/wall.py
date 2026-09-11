from objects.game import GameObject
from core.consts import WALL_COLOR, DEFAULT_WALL_LIFETIME


class Wall(GameObject):
    '''Игровой объект стена.'''

    def __init__(self, positions: list[tuple[int, int]] | None):
        if positions is None:
            return None
        self._positions = positions
        self._body_color = WALL_COLOR
        self.life_time = DEFAULT_WALL_LIFETIME
        self._is_game_over_on_interception = True

    def move(self):
        pass
