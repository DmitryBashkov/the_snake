from enum import Enum

import pygame

from core.consts import DEFAULT_SPEED, DOWN_KEYS, LEFT_KEYS, RIGHT_KEY, UP_KEYS

# Настройка времени:
clock = pygame.time.Clock()


class Speed:
    """Скорость движения змейки."""

    _speed: int

    def __init__(self) -> None:
        self._speed = DEFAULT_SPEED

    def inc(self, value: int = 20) -> None:
        """Увеличение скорости. По дефолту на +20."""
        self._speed += value

    def dec(self, value: int = 20) -> None:
        """Уменьшение скорости. По дефолту на -20."""
        self._speed -= value

    def set_default(self) -> None:
        """Устанавливаем дефолтную скорость игры."""
        self._speed = DEFAULT_SPEED

    def __int__(self) -> int:
        """Возвращает скорость в виде int."""
        return self._speed

    @property
    def value(self) -> int:
        """Свойство. Возвращает скорость в виде int."""
        return self._speed


class Direction(Enum):
    """Класс для соотнесения кнопки и вектора."""

    UP = ((0, -1), UP_KEYS)
    DOWN = ((0, 1), DOWN_KEYS)
    LEFT = ((-1, 0), LEFT_KEYS)
    RIGHT = ((1, 0), RIGHT_KEY)

    def __init__(
            self,
            vector: tuple[int, int],
            keys: tuple[int, ...],
    ) -> None:
        """Инициация класса Direction."""
        self._vector = vector
        self._keys = keys

    @property
    def opp(self) -> 'Direction':
        """Вовзарщает обратное направдление."""
        return {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }[self]

    @property
    def vertical(self) -> bool:
        """True если направление по вертикали."""
        return self.vector[0] == 0

    @property
    def horizontal(self) -> bool:
        """True если направление по горизонтали."""
        return self.vector[1] == 0

    @property
    def keys(self) -> tuple[int, ...]:
        """Возвращает все кнопки соответствующего вектора направления."""
        return self._keys

    @property
    def vector(self) -> tuple[int, int]:
        """Возвращает вектор направления."""
        return self._vector

    @classmethod
    def from_keys(cls, key: int) -> 'Direction | None':
        """По кнопка определяет вектор направления."""
        for direction in cls:
            if key in direction.keys:
                return direction
        return None

    @classmethod
    def from_vector(cls, vector: tuple[int, int]) -> 'Direction | None':
        """По вектору определяет направление."""
        for direction in cls:
            if vector == direction.vector:
                return direction


speed = Speed()
