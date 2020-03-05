import copy
import logging
from typing import List, Any, Dict

import numpy as np
from torch import nn
from tqdm import trange

from alphazero.alphazero.mcts import MonteCarloTreeSearch
from alphazero.alphazero.types import TrainExample
from alphazero.games import Game, Player
from .neural_net import NeuralNetTrainer
from .state_encoders import GameStateEncoder, torch

logger = logging.getLogger(__name__)


class AlphaZeroTrainer:
    def __init__(self,
                 game: Game,
                 state_encoder: GameStateEncoder,
                 mcts: MonteCarloTreeSearch,
                 config: Dict[str, Any]):
        self.game = game
        self.state_encoder = state_encoder
        self.mcts = mcts
        self.config = config

    def train(self):
        examples = []
        for i in trange(self.config['num_iters'], position=0):
            examples_iter: List[TrainExample] = []
            for ep in trange(self.config['num_episodes'], position=1):
                # logger.info('Episode %d', ep)
                self.mcts.reset()
                examples_ep = self.run_episode()
                examples_iter.extend(examples_ep)
            examples.append(examples_iter)

        examples_for_training = [e for ex_iter in examples for e in ex_iter]
        np.random.shuffle(examples_for_training)

        nn_old = copy.deepcopy(self.mcts.nn)
        nn_trainer = NeuralNetTrainer(self.mcts.nn, self.config)
        nn_trainer.train(examples_for_training)
        nn_new = self.mcts.nn

        if not self._update_nn(nn_old, nn_new):
            self.mcts.nn = nn_old

    def run_episode(self) -> List[TrainExample]:
        """
        Run an episode (full game of self-play) from the initial state
        and collect train examples throughout the game.
        :return: training examples as a list of (s_t, pi_t, z_t) triples
        """
        self.game.reset()
        examples: List[TrainExample] = []  # (s_t, pi_t, z_t) tuples
        while not self.game.is_over:
            pi = self.mcts.get_policy(self.game.state)
            # TODO: augmentation by symmetries
            examples.append((self.game.state, pi, None))
            move_index = np.random.choice(self.game.action_space_size, p=pi)
            move = self.game.index_to_move(move_index)
            self.game.play(move)

        def z(player: Player, winner):
            if winner is None:
                return 0.
            return +1. if player == winner else -1.

        # must transform to tensors for nn training
        # pylint: disable=not-callable
        examples = [(self.state_encoder.encode(s), torch.tensor(pi), z(s.player, self.game.winner))
                    for s, pi, _ in examples]
        return examples

    def _update_nn(self, nn_old: nn.Module, nn_new: nn.Module) -> bool:
        """
        Let nn_old and nn_new compete, and returns True iff nn_new wins
        more than nn_update_threshold of the time.
        :param nn_old:
        :param nn_new:
        :return: True iff nn_new wins more than nn_update_threshold of the time
        """
        self.game.reset()
        # agent_old = AlphaZeroAgent(self.game, self.state_encoder, nn_old, self.num_sim, self.c_puct)
        # agent_new = AlphaZeroAgent(self.game, self.state_encoder, nn_new, self.num_sim, self.c_puct)
        # while not self.game.is_over:
        #     break
        # TODO: implement pitting here or in separate class?
        # TODO: make human-player an agent?
        return True