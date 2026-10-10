from enum import Enum, auto
from random import choices, randint

from core.consts import (APPLE_COLOR, APPLE_TYPES_WEIGHTS,
                         DEFAULT_GAME_OBJECT_LIFETIME, DEFAULT_START_POSITION,
                         GRID_HEIGHT, GRID_SIZE, GRID_WIDTH)
from objects.game import GameObject


class AppleType(Enum):
    """Тип яблока, которое определяет текущее поведение змейки."""

    normal = auto()
    rotten = auto()
    drunk = auto()
    aid = auto()
    hot = auto()


APPLE_TYPES = tuple(AppleType)


class Apple(GameObject):
    """Игровой объект яблоко."""

    # Внесем принципы квантовой механики,
    # пока яблоко не съедено, оно находится в суперпозиции всех 5 типов
    type: AppleType

    def __init__(
        self,
        positions: list[tuple[int, int]] = [DEFAULT_START_POSITION],
    ) -> None:

        # у всех яблок будет один и тот же цвет,
        # чтобы пользователь не знал,
        # какое яблоко он съел, пока не съест его

        super().__init__(
            positions=positions,
            body_color=APPLE_COLOR,
        )

        self.life_time = DEFAULT_GAME_OBJECT_LIFETIME

    def randomize_position(self) -> None:
        """Устанавливает случайную позицию яблока."""
        self._positions = [(
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )]

    def detect_type(self) -> None:
        """Определение типа яблока."""
        self.type = choices(
            population=APPLE_TYPES,
            weights=APPLE_TYPES_WEIGHTS,
            k=1)[0]

    def move(self) -> None:
        """В этой игре яблоко не двигается."""
        pass

    @property
    def normal(self) -> bool:
        """Возвращает true, если яблоко нормальное."""
        return self.type is AppleType.normal

    @property
    def rotten(self) -> bool:
        """Возвращает true, если яблоко гнилое."""
        return self.type is AppleType.rotten

    @property
    def drunk(self) -> bool:
        """Возвращает true, если яблоко забродившее."""
        return self.type is AppleType.drunk

    @property
    def aid(self) -> bool:
        """Возвращает true, если яблоко целительное."""
        return self.type is AppleType.aid

    @property
    def hot(self) -> bool:
        """Возвращает true, если яблоко острое."""
        return self.type is AppleType.hot
