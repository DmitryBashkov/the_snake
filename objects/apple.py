from enum import Enum, auto
from objects.game import GameObject
from random import choices


class AppleType(Enum):
    '''
    Тип яблока, которое определяет текущее поведение змейки.\n
    :normal: обычное, яблоко +1 к длине змейки\n
    :rotten: гнилое, змейка теряет половину длины, которая становится стеной\n
    :drunk: забродившее, змейка меняет направление инверсивно\n
    :hot: горячее, змейка убегает в обратном
    направлении с удвоенной скоростью\n
    :aid: целительное, отменяет действие drunk
    '''

    normal = auto()
    rotten = auto()
    drunk = auto()
    aid = auto()
    hot = auto()


APPLE_TYPES = tuple(AppleType)

# Вевероятности распределены по 50% для плохих и хороших яблок
APPLE_TYPES_WEIGHTS = (40, 5, 20, 10, 25)


class Apple(GameObject):
    '''Игровой объект яблоко.'''

    # Внесем принципы квантовой механики,
    # пока яблоко не съедено, оно находится в суперпозиции всех 5 типов
    _type: AppleType

    def __init__(self) -> None:
        self._body_color = (255, 0, 0)
        self._positions = self._randomize_position()
        self.life_time = 500
        self._is_game_over_on_interception = False

    def detect_type(self) -> AppleType:
        '''Определение типа яблока'''
        self._type = choices(
            population=APPLE_TYPES,
            weights=APPLE_TYPES_WEIGHTS,
            k=1)[0]
        return self._type

    def move(self) -> None:
        '''Яблоко не двигается'''
        pass

    @property
    def normal(self) -> bool:
        return self._type is AppleType.normal

    @property
    def rotten(self) -> bool:
        return self._type is AppleType.rotten

    @property
    def drunk(self) -> bool:
        return self._type is AppleType.drunk

    @property
    def aid(self) -> bool:
        return self._type is AppleType.aid

    @property
    def hot(self) -> bool:
        return self._type is AppleType.hot
