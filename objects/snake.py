from core.consts import GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_COLOR
from core.mechanics import Direction
from objects.apple import AppleType
from objects.game import GameObject


class Snake(GameObject):
    """Игровой объект змейка."""

    def __init__(self) -> None:

        # аттрибуты родительского класса
        super().__init__(
            body_color=SNAKE_COLOR,
        )

        self._moving_object: bool = True
        self._is_game_over_on_interception: bool = True

        # атрибуты, относящиеся к конкретному классу
        self._length: int = 1
        self.grow: bool = False
        self.reverse: bool = False
        self.direction = Direction.RIGHT
        self.last_apple: AppleType = AppleType.normal

    def update_direction(self, direction: Direction) -> None:
        """Обновляет направление движения змейки."""
        if self.axis_horizon == direction.horizontal:
            return None

        if self.axis_vert == direction.vertical:
            return None

        self.direction = direction.opp if self.reverse else direction

    def get_head_position(self) -> tuple[int, int]:
        """Возвращает позицию головы змейки."""
        return self.head

    def move(self) -> None:
        """Движение определяется путем добавления
        новой головы в направлении движения
        и удаления последнего элемента змейки,
        если она не растет (grow == False).
        """
        new_head = (
            (
                self.head[0]
                + self.direction.vector[0] * GRID_SIZE
            ) % SCREEN_WIDTH,
            (
                self.head[1]
                + self.direction.vector[1] * GRID_SIZE
            ) % SCREEN_HEIGHT,
        )

        self._positions.insert(0, new_head)

        if not self.grow:
            self._positions.pop(-1)

        # когда змейка подросла, онап перестает расти,
        # пока не съест новое яблоко
        self.grow = False

    @property
    def length(self) -> int:
        """Возвращает длину змейки."""
        return len(self._positions)

    @property
    def axis_horizon(self) -> bool:
        """Возвращает true, если змейка движется по горизонтали."""
        return self.direction.vector[0] != 0

    @property
    def axis_vert(self) -> bool:
        """Возвращает true, если змейка движется по вертикали."""
        return self.direction.vector[1] != 0

    def is_last(self, position: tuple[int, int]) -> bool:
        """Возвращает true,
        если переданная позиция является последним элементом змейки.
        """
        return position == (self._positions[self.length - 1])

    @property
    def last(self) -> tuple[int, int]:
        """Возвращает позицию последнего элемента змейки."""
        return self._positions[self.length - 1]

    def intercepts(self, obj_list: list[GameObject]) -> bool:
        """Определение столкновения.
        Для этого достаточно понять, попала ли голова змейки в другой объект
        """
        for obj in obj_list:
            return self.head == obj.head

        # Отдельная проверка, столкнулась ли змейка сама с собой
        return self.head in self._positions

    def throw_half(self) -> list[tuple[int, int]] | None:
        """Удаляет вторую половину змейки и возвращает ее как результат
        Применимо для тухлого яблока
        """
        if self.length < 3:
            return None

        # Находим середину, если нечетное,
        # то забираем от змейки больше половины
        mid_position = len(self._positions) // 2

        # Половину змейки выводим как новый лист в результат
        half = self._positions[mid_position:]

        # Удаляем половину из исходного листа
        del self._positions[mid_position:]

        return half

    def reverse_snake(self) -> None:
        """Меняет направление змейки на противоположное."""
        self._positions.reverse()
        self.direction = self.direction.opp

    def drunk(self) -> None:
        """Меняет местами кнпки управления движением змейки."""
        self.reverse = True

    def heal(self) -> None:
        """Восстанавливает здоровье змейки,
        если она была повреждена тухлым яблоком.
        """
        self.reverse = False

    def eat(self, apple_type: AppleType) -> list[tuple[int, int]] | None:
        """Определяет, что происходит со змейкой после поедания яблока.
        Если съел гнилое яблоко, то выозвращает половину тела.
        В остальнух случаях вовзращает None.
        """
        match apple_type:

            case AppleType.aid:
                self.last_apple = AppleType.aid
                self.heal()

            case AppleType.rotten:
                self.last_apple = AppleType.rotten
                self.grow = True
                return self.throw_half()

            case AppleType.hot:
                self.last_apple = AppleType.hot
                self.reverse_snake()

            case AppleType.drunk:
                self.last_apple = AppleType.drunk
                self.drunk()

            case AppleType.normal:
                self.last_apple = AppleType.normal

        self.grow = True
        return None
