import os
import functools
import unittest

import game

CURRENT_DIR = os.path.dirname(__file__)

'''
Test cases used on this file were taken from 
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns
'''


def boards_are_equal(expected_board, resulting_board):
    return functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, expected_board, resulting_board), True)


class TestGameOfLifeStillLife(unittest.TestCase):
    def test_block_evolve_to_itself(self):
        max_val, board = game.read_seed(f"{CURRENT_DIR}/test_images/still_lifes_block.pgm")

        evolved_board = game.evolve(board, max_val)

        assert boards_are_equal(board, evolved_board)

    def test_evolve_to_block_1(self):
        max_val, board = game.read_seed(f"{CURRENT_DIR}/test_images/pre_block_state.pgm")

        _, expected_board = game.read_seed(f"{CURRENT_DIR}/test_images/still_lifes_block.pgm")

        evolved_board = game.evolve(board, max_val)

        assert boards_are_equal(expected_board, evolved_board)

    def test_beehive_evolve_to_itself(self):
        max_val, board = game.read_seed(f"{CURRENT_DIR}/test_images/still_lifes_beehive.pgm")

        evolved_board = game.evolve(board, max_val)

        assert boards_are_equal(board, evolved_board)

    def test_loaf_evolve_to_itself(self):
        max_val, board = game.read_seed(f"{CURRENT_DIR}/test_images/still_lifes_loaf.pgm")

        evolved_board = game.evolve(board, max_val)

        assert boards_are_equal(board, evolved_board)

    def test_boat_evolve_to_itself(self):
        max_val, board = game.read_seed(f"{CURRENT_DIR}/test_images/still_lifes_boat.pgm")

        evolved_board = game.evolve(board, max_val)

        assert boards_are_equal(board, evolved_board)

    def test_tub_evolve_to_itself(self):
        max_val, board = game.read_seed(f"{CURRENT_DIR}/test_images/still_lifes_tub.pgm")

        evolved_board = game.evolve(board, max_val)

        assert boards_are_equal(board, evolved_board)


class TestGameOfLifeOscillators(unittest.TestCase):
    def test_blinker_state1_evolves_to_state2(self):
        max_val, board = game.read_seed(f"{CURRENT_DIR}/test_images/oscillators_blinker_state1.pgm")

        _, expected_board = game.read_seed(f"{CURRENT_DIR}/test_images/oscillators_blinker_state2.pgm")

        evolved_board = game.evolve(board, max_val)

        assert boards_are_equal(expected_board, evolved_board)

    def test_blinker_state2_evolves_to_state1(self):
        max_val, board = game.read_seed(f"{CURRENT_DIR}/test_images/oscillators_blinker_state2.pgm")

        _, expected_board = game.read_seed(f"{CURRENT_DIR}/test_images/oscillators_blinker_state1.pgm")

        evolved_board = game.evolve(board, max_val)

        assert boards_are_equal(expected_board, evolved_board)
