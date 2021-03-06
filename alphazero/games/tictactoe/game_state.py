from typing import List, Optional

from alphazero.games import GameState, Player
from .board import TicTacToeBoard
from .exception import IllegalTicTacToeMoveException
from .move import TicTacToeMove
from .player import TicTacToePlayer


class TicTacToeGameState(GameState[TicTacToeMove, TicTacToePlayer, TicTacToeBoard]):

    def __init__(self, board: TicTacToeBoard, player: TicTacToePlayer) -> None:
        super().__init__()
        self._board = board
        self._player = player

    @property
    def player(self) -> TicTacToePlayer:
        return self._player

    @property
    def board(self) -> TicTacToeBoard:
        return self._board

    @classmethod
    def get_initial_state(cls, size: int = 3) -> 'TicTacToeGameState':
        return TicTacToeGameState(TicTacToeBoard(size), TicTacToePlayer.X)

    @property
    def current_player(self) -> Player:
        return self.player

    def next(self, move: TicTacToeMove) -> 'TicTacToeGameState':
        if self.is_terminal():
            raise IllegalTicTacToeMoveException("Game has ended.")
        next_board = self.board.copy()
        next_board.apply_move(self.player, move)
        return TicTacToeGameState(next_board, self.player.opponent)

    def get_legal_moves(self) -> List[TicTacToeMove]:
        return self.board.get_legal_moves()

    def is_legal_move(self, move: TicTacToeMove) -> bool:
        return self.board.is_legal_move(move)

    def winner(self) -> Optional[TicTacToePlayer]:
        if self.board.has_won(TicTacToePlayer.X):
            return TicTacToePlayer.X
        elif self.board.has_won(TicTacToePlayer.O):
            return TicTacToePlayer.O
        else:
            return None

    def is_terminal(self) -> bool:
        return self.is_win() or self.is_lose() or self.is_tie()

    def is_win(self) -> bool:
        return self.winner() == self.player

    def is_lose(self) -> bool:
        return self.winner() == self.player.opponent

    def is_tie(self) -> bool:
        return self.winner() is None and self.board.full()

    def canonical(self) -> 'TicTacToeGameState':
        if self.player == TicTacToePlayer.X:
            return self
        rev_board = self.board.copy()
        for point, player in self.board.grid.items():
            rev_board.grid[point] = player.opponent
        return TicTacToeGameState(rev_board, self.player.opponent)
