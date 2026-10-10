from pygame import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_w, K_s, K_a, K_d,
)
GAME_NAME = 'Змейка отрывается в выходные'

# размеры экрана и игрового поля
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# дефолтная скорость змейки
DEFAULT_SPEED = 20

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Цвет стены
WALL_COLOR = (150, 150, 150)

# красный цвет 
RED = (255, 0, 0)

# зеленый цвет
GREEN = (255, 0, 0)

# синий цвет
BLUE = (255, 0, 0)

# Сколько циклов живет игровой объект
DEFAULT_GAME_OBJECT_LIFETIME = 2000

# дефолтная стартовая позиция игровых объектов
DEFAULT_START_POSITION = (0, 0)

# Максимальное количество яблок на поле
MAX_APPLES = 3

# для объектов у которых нет времени жизни -- змейка
NO_LIFETIME = -1

# Вевероятности распределены по 50% для плохих и хороших яблок
APPLE_TYPES_WEIGHTS = (40, 5, 20, 10, 25)

# Кнопки управления. Можно добавлять или убират
UP_KEYS = (K_UP, K_w)
DOWN_KEYS = (K_DOWN, K_s)
LEFT_KEYS = (K_LEFT, K_a)
RIGHT_KEY = (K_RIGHT, K_d)