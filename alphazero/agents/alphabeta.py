import random
from typing import Callable, TypeVar, Generic

from alphazero.games.game_state import GameState
from alphazero.games.move import Move
from alphazero.games.player import Player
from .base import Agent

S = TypeVar('S', bound=GameState)
M = TypeVar('M', bound=Move)
P = TypeVar('P', bound=Player)


class AlphaBetaAgent(Agent, Generic[S, M, P]):
    def __init__(self,
                 player: P,
                 depth: int,
                 eval_fn: Callable[[S, P], float]) -> None:
        super().__init__()
        self.player = player
        self.depth = depth
        self.eval_fn = eval_fn

    def select_move(self, state: S) -> M:
        best_value, best_move = float('-inf'), None
        alpha, beta = float('-inf'), float('+inf')
        legal_moves = state.get_legal_moves()
        random.shuffle(legal_moves)
        for move in legal_moves:
            next_state = state.next(move)
            value = self._value(next_state, self.depth - 1, alpha, beta)
            if value > best_value:
                best_move = move
                best_value = value
            alpha = max(alpha, value)
        return best_move

    def _value(self, state: S, depth: int, alpha: float, beta: float) -> float:
        if state.is_terminal() or depth == 0:
            return self.eval_fn(state, self.player)
        if state.current_player == self.player:
            return self._max_value(state, depth, alpha, beta)
        else:
            return self._min_value(state, depth, alpha, beta)

    def _max_value(self, state: S, depth: int, alpha: float, beta: float) -> float:
        v = float('-inf')
        legal_moves = state.get_legal_moves()
        random.shuffle(legal_moves)
        for move in legal_moves:
            next_state = state.next(move)
            branch_value = self._value(next_state, depth - 1, alpha, beta)
            v = max(v, branch_value)
            if v > beta:
                return v
            alpha = max(alpha, v)
        return v

    def _min_value(self, state: S, depth: int, alpha: float, beta: float) -> float:
        v = float('+inf')
        legal_moves = state.get_legal_moves()
        random.shuffle(legal_moves)
        for move in legal_moves:
            next_state = state.next(move)
            branch_value = self._value(next_state, depth - 1, alpha, beta)
            v = min(v, branch_value)
            if v < alpha:
                return v
            beta = min(beta, v)
        return v
