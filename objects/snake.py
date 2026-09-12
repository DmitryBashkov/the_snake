from core.consts import (
    SNAKE_COLOR
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
        self._positions = [(0, 0)]
        self._body_color = SNAKE_COLOR
        self._direction = (1, 0)
        self._moving_object = True
        self._is_game_over_on_interception = True

    def update_direction(self, new_direction: tuple[int, int]) -> None:
        self._direction = new_direction

    def move(self) -> None:
        '''Движение определяется путем применения
        направления на все элементы списка
        позиций по формуле: x + dx + GRID_SIZE\n
        Если позиция (20,40), а направление (0,-1),
        то новая позиция будет (20, 20)
        '''
        # dx, dy = self._direction
        # self._positions = [
        #     (x + dx * GRID_SIZE, y + dy * GRID_SIZE)
        #     for (x, y) in self._positions
        # ]

        self._positions.remove(self.last)

    @property
    def length(self) -> int:
        return len(self._positions)

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
        '''Удаляет вторую половину змейки и возвращает ее как результат'''

        # Находим середину, если нечетное,
        # то забираем от змейки больше половины
        mid_position = len(self._positions) // 2

        # Половину змейки выводим как новый лист в результат
        half = self._positions[mid_position:]

        # Удаляем половину из исходного листа
        del self._positions[mid_position:]

        return half

    def reverse_snake(self) -> None:
        self._positions.reverse

    def reverse_direction(self) -> None:
        dx, dy = self._direction
        self._direction = (-dx, -dy)

    def inc(self, new_head: tuple[int, int]):
        self._positions.insert(0, new_head)

    def heal(self):
        self.reverse_direction()

    def eat(self, apple: Apple):

        if apple.aid:
            self.heal()

        elif apple.rotten:
            return self.throw_half()

        elif apple.hot:
            self.reverse_snake()

        elif apple.drunk:
            self.reverse_direction()

        self.inc(apple.head)
