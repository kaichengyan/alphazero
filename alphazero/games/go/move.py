from typing import Optional

from alphazero.games.move import Move
from .point import GoPoint


class GoMove(Move):
    def __init__(self,
                 point: Optional[GoPoint] = None,
                 is_pass: bool = False,
                 is_resign: bool = False):
        if point is not None and (is_pass or is_resign):
            raise Exception
        elif is_pass and is_resign:
            raise Exception
        self.point = point
        self.is_pass = is_pass
        self.is_resign = is_resign

    @property
    def is_play(self) -> bool:
        return self.point is not None

    @property
    def x(self) -> int:
        if self.point is None:
            raise Exception('Move is resign or pass')
        return self.point.x

    @property
    def y(self) -> int:
        if self.point is None:
            raise Exception('Move is resign or pass')
        return self.point.y

    @classmethod
    def play(cls, x, y) -> 'GoMove':
        return GoMove(GoPoint(x, y))

    @classmethod
    def pass_turn(cls) -> 'GoMove':
        return GoMove(is_pass=True)

    @classmethod
    def resign(cls) -> 'GoMove':
        return GoMove(is_resign=True)

    def __repr__(self):
        if self.is_pass:
            return 'GoMove.pass_turn'
        elif self.is_resign:
            return 'GoMove.resign'
        return f'GoMove({self.x}, {self.y})'

    @classmethod
    def from_string(cls, string: str) -> 'GoMove':
        string = string.lower().strip()
        if string == 'resign':
            return GoMove.resign()
        elif string == 'pass':
            return GoMove.pass_turn()
        x, y = string.split()
        return GoMove.play(int(x), int(y))
