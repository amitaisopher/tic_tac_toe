import enum

class GameState(enum.Enum):
    NotStarted = 0
    Started = 1
    XMadeLastMove = 2
    CircleMadeLastMove = 3
    Finished = 4

class GameResult(enum.Enum):
    Draw = 0
    WinByX = 1
    WinByCircle = 2

class Shapes(enum.Enum):
    X = 0
    Circle = 1