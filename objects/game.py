from core.consts import (
    BOARD_BACKGROUND_COLOR,
    DEFAULT_START_POSITION,
    NO_LIFETIME,
)


class GameObject:
    """Базовый игровой объект."""

    def __init__(
        self,
        positions: list[tuple[int, int]] = [DEFAULT_START_POSITION],
        body_color: tuple[int, int, int] = BOARD_BACKGROUND_COLOR,
    ) -> None:

        self._positions = positions
        self._body_color = body_color
        self.life_time = NO_LIFETIME
        self._moving_object = False
        self._is_game_over_on_interception = False

    def dec_lifetime(self) -> None:
        """Уменьшает lifetime объекта на 1."""
        self.life_time -= 1

    @property
    def positions(self) -> list[tuple[int, int]]:
        """Возвращает список позиций"""
        return self._positions

    @property
    def body_color(self) -> tuple[int, int, int]:
        """Возвращает цвет объекта."""
        return self._body_color

    @property
    def head(self) -> tuple[int, int]:
        """Возвращает головной элемент объекта."""
        return self._positions[0]

    @property
    def is_game_over_on_interception(self) -> bool:
        """Возвращает true, если после столкновения игра останавливаетя."""
        return self._is_game_over_on_interception

    def draw(self) -> None:
        """Отрисовывает объект на экране."""
        raise NotImplementedError(
            f'Не определен метод draw класса {type(self).__name__}',
        )

    def move(self) -> None:
        """Описывает дивжение объекта."""
        raise NotImplementedError(
            f'Не определен метод move класса {type(self).__name__}',
        )
