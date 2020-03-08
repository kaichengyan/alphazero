import logging
import sys

import torch
import yaml

from alphazero.agents.alphazero import AlphaZeroArgMaxAgent
from alphazero.alphazero.mcts import MonteCarloTreeSearch
from alphazero.alphazero.nn_modules import AlphaZeroNeuralNet
from alphazero.alphazero.nn_modules.encoders import SimpleConvNetEncoder
from alphazero.alphazero.nn_modules.policy_heads import SimpleFullyConnectedPolicyHead
from alphazero.alphazero.nn_modules.value_heads import SimpleFullyConnectedValueHead
from alphazero.alphazero.state_encoders.gomoku_state_encoder import GomokuStateEncoder
from alphazero.games.gomoku import GomokuGame, GomokuPlayer, GomokuMove

FORMAT = '%(asctime)s - %(name)-15s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format=FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')

with open('gomoku.yaml', 'r') as f:
    config = yaml.safe_load(f)

config['device'] = 'cuda' if torch.cuda.is_available() else 'cpu'


def read_move(player: GomokuPlayer) -> GomokuMove:
    x, y = input(f"{player.name} move: ").split()
    x, y = int(x), int(y)
    return GomokuMove(x, y)


if __name__ == '__main__':
    game = GomokuGame(config['game_size'])
    state_encoder = GomokuStateEncoder(config)

    # encoder = LinearEncoder(config)
    # value_head = LinearValueHead(config)
    # policy_head = LinearPolicyHead(game.action_space_size, config)

    encoder = SimpleConvNetEncoder(config)
    value_head = SimpleFullyConnectedValueHead(config)
    policy_head = SimpleFullyConnectedPolicyHead(game.action_space_size, config)

    net = AlphaZeroNeuralNet(encoder, policy_head, value_head, config)
    mcts = MonteCarloTreeSearch(game=game,
                                state_encoder=state_encoder,
                                nn=net,
                                config=config)

    net.load_state_dict(torch.load('./tmp/gomoku/best.pth'))
    net.eval()
    agent = AlphaZeroArgMaxAgent(game, state_encoder, net, config)

    while not game.is_over:
        game.show_board()
        # print(f"current state score by eval func: {agent.eval_fn(game.state, agent.player)}")
        if game.current_player == GomokuPlayer.BLACK:
            move = read_move(game.current_player)
            while not game.state.is_legal_move(move):
                print("Illegal move, try again")
                move = read_move(game.current_player)
        else:
            move = agent.select_move(game.state)
            print(f"Agent {game.current_player!s} move: {move}")
        game.play(move)

    print("--- GAME OVER ---")
    game.show_board()
    if game.winner:
        print(f"{game.winner.name} wins!")
    else:
        print("tie :(")