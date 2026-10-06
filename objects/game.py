class GameObject:
    """Базовый игровой объект."""

    _positions: list[tuple[int, int]]
    _body_color: tuple[int, int, int]
    life_time: int
    _moving_object: bool
    _is_game_over_on_interception: bool

    def __init__(
        self,
        position: tuple[int, int] | None = None,
        body_color: tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        if position is None:
            position = (0, 0)
        self._positions = [position]
        self._body_color = body_color
        self.life_time = -1
        self._moving_object = False
        self._is_game_over_on_interception = False

    def dec_lifetime(self) -> None:
        """Уменьшает lifetime объекта на 1."""
        self.life_time -= 1

    @property
    def position(self) -> tuple[int, int]:
        """Возвращает позицию объекта."""
        return self._positions[0]

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
        pass

    def move(self):
        """Описывает дивжение объекта."""
        pass
