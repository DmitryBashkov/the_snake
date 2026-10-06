from core.consts import (
    SNAKE_COLOR,
    GRID_SIZE,
    SCREEN_WIDTH, SCREEN_HEIGHT
)
from objects.apple import Apple, AppleType
from objects.game import GameObject


class Snake(GameObject):
    '''Игровой объект змейка.'''

    # игра начинается с обычной змейкой
    last_apple: AppleType = AppleType.normal
    direction: tuple[int, int]

    def __init__(self) -> None:
        self._length = 1
        self.grow = False
        self.reverse = False
        self._positions = [(0, 0)]
        self._body_color = SNAKE_COLOR
        self.direction = (1, 0)
        self._moving_object = True
        self._is_game_over_on_interception = True
        self.life_time = -1

    def update_direction(self, new_direction: tuple[int, int]) -> None:
        '''Обновляет направление движения змейки.'''
        self.direction = new_direction

    def get_head_position(self) -> tuple[int, int]:
        '''Возвращает позицию головы змейки.'''
        return self.head

    def reset(self) -> None:
        '''Сбрасывает змейку в начальное состояние.'''
        self._positions = [(0, 0)]
        self.direction = (1, 0)
        self.grow = False
        self.reverse = False

    def move(self) -> None:
        '''
        Движение определяется путем добавления новой головы в направлении движения
        и удаления последнего элемента змейки, если она не растет (grow == False).
        '''
        new_head = (
            (self.head[0] + self.direction[0] * GRID_SIZE) % SCREEN_WIDTH,
            (self.head[1] + self.direction[1] * GRID_SIZE) % SCREEN_HEIGHT
        )

        self._positions.insert(0, new_head)

        if not self.grow:
            self._positions.pop(-1)

        # когда змейка подросла, онап перестает расти, пока не съест новое яблоко
        self.grow = False

    @property
    def length(self) -> int:
        return len(self._positions)

    @property
    def axis_horizontal(self) -> bool:
        '''Возвращает true, если змейка движется по горизонтали.'''
        return self.direction[0] != 0

    @property
    def axis_vertical(self) -> bool:
        '''Возвращает true, если змейка движется по вертикали.'''
        return self.direction[1] != 0

    def is_last(self, position: tuple[int, int]) -> bool:
        return position == (self._positions[self.length - 1])

    @property
    def last(self) -> tuple[int, int]:
        return self._positions[self.length - 1]

    def intercepts(self, obj_list: list[GameObject]) -> bool:
        '''
        Определение столкновения.\n
        Для этого достаточно понять, попала ли голова змейки в другой объект
        '''
        for obj in obj_list:
            return self.head == obj.head

        # Отдельная проверка, столкнулась ли змейка сама с собой
        return self.head in self._positions

    def throw_half(self) -> list[tuple[int, int]] | None:
        '''
        Удаляет вторую половину змейки и возвращает ее как результат
        Применимо для тухлого яблока
        '''

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
        '''Меняет направление змейки на противоположное.'''
        self._positions.reverse()
        self.update_direction(
            (
                -self.direction[0] if self.axis_horizontal else self.direction[0],
                -self.direction[1] if self.axis_vertical else self.direction[1]
            )
        )

    def drunk(self) -> None:
        '''Меняет местами кнпки управления движением змейки.'''
        self.reverse = True

    def heal(self):
        self.reverse = False

    def eat(self, apple: Apple):

        if apple.aid:
            self.last_apple = AppleType.aid
            self.heal()

        elif apple.rotten:
            self.last_apple = AppleType.rotten
            self.grow = True
            return self.throw_half()

        elif apple.hot:
            self.last_apple = AppleType.hot
            self.reverse_snake()

        elif apple.drunk:
            self.last_apple = AppleType.drunk
            self.drunk()

        elif apple.normal:
            self.last_apple = AppleType.normal

        self.grow = True
