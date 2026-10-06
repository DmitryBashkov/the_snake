from enum import Enum, auto
from random import choices, randint

from core.consts import (APPLE_COLOR, DEFAULT_GAME_OBJECT_LIFETIME,
                         GRID_HEIGHT, GRID_SIZE, GRID_WIDTH)
from objects.game import GameObject


class AppleType(Enum):
    r"""Тип яблока, которое определяет текущее поведение змейки.\n
    :normal: обычное, яблоко +1 к длине змейки\n
    :rotten: гнилое, змейка теряет половину длины, которая становится стеной\n
    :drunk: забродившее, змейка меняет направление инверсивно\n
    :hot: горячее, змейка убегает в обратном
    направлении с удвоенной скоростью\n
    :aid: целительное, отменяет действие drunk
    """

    normal = auto()
    rotten = auto()
    drunk = auto()
    aid = auto()
    hot = auto()


APPLE_TYPES = tuple(AppleType)

# Вевероятности распределены по 50% для плохих и хороших яблок
APPLE_TYPES_WEIGHTS = (40, 5, 20, 10, 25)


class Apple(GameObject):
    """Игровой объект яблоко."""

    # Внесем принципы квантовой механики,
    # пока яблоко не съедено, оно находится в суперпозиции всех 5 типов
    _type: AppleType

    def __init__(
        self, positions: list[tuple[int, int]] | None = None,
    ) -> None:

        # у всех яблок будет один и тот же цвет,
        # чтобы пользователь не знал, какое яблоко он съел, пока не съест его
        self._body_color = APPLE_COLOR
        if positions is None:
            self.randomize_position()
        else:
            self._positions = positions
        self.life_time = DEFAULT_GAME_OBJECT_LIFETIME
        self._is_game_over_on_interception = False

    def randomize_position(self) -> None:
        """Устанавливает случайную позицию яблока."""
        self._positions = [(
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )]

    def detect_type(self) -> None:
        """Определение типа яблока"""
        self._type = choices(
            population=APPLE_TYPES,
            weights=APPLE_TYPES_WEIGHTS,
            k=1)[0]

    def move(self) -> None:
        """В этой игре яблоко не двигается."""
        pass

    @property
    def normal(self) -> bool:
        """Возвращает true, если яблоко нормальное."""
        return self._type is AppleType.normal

    @property
    def rotten(self) -> bool:
        """Возвращает true, если яблоко гнилое."""
        return self._type is AppleType.rotten

    @property
    def drunk(self) -> bool:
        """Возвращает true, если яблоко забродившее."""
        return self._type is AppleType.drunk

    @property
    def aid(self) -> bool:
        """Возвращает true, если яблоко целительное."""
        return self._type is AppleType.aid

    @property
    def hot(self) -> bool:
        """Возвращает true, если яблоко острое."""
        return self._type is AppleType.hot
