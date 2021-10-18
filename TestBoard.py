import ipytest
import pytest
ipytest.autoconfig()

%%ipytest

def test_markPlayer():
    board = Board()
    player = Player(1)

    board.markPlayer(0, 0, player)
    assert board[0][0] == player

def test_update():
    board = Board()
    player1 = Player(1)
    player2 = Player(2)

    for col in range(3):
        for row in range(3):
            assert board.update(col, row, player1) == True
            assert board.update(col, row, player2) == False

def test_noMoreMoves():
    board = Board()
    player1 = Player(1)
    player2 = Player(2)

    for row in range(3):
        assert board.noMoreMoves() == False
        board.update(0, row, player1)
        board.update(1, row, player2)
        board.update(2, row, player1)    

    assert board.noMoreMoves() == True

def test_over():
    board = Board()
    player1 = Player(1)
    player2 = Player(2)

    assert board.over() == Result.NO_RESULT

    # Column winningconditions
    for col in range(3):
        board = Board()
        board.update(col, 0, player1)
        board.update(col, 1, player1)
        board.update(col, 2, player1)

    # Row winningconditions
    for row in range(3):
        board = Board()
        board.update(0, row, player1)
        board.update(1, row, player1)
        board.update(2, row, player1)
        assert board.over() == player1

    # Diagonal winningcondition \
    board = Board()
    board.update(0, 0, player1)
    board.update(1, 1, player1)
    board.update(2, 2, player1)
    assert board.over() == player1

    # Diagonal winningcondition /
    board = Board()
    board.update(2, 0, player1)
    board.update(1, 1, player1)
    board.update(0, 2, player1)
    assert board.over() == player1

    # Draw
    board = Board()
    board.update(0, 0, player1)
    board.update(0, 1, player2)
    board.update(0, 2, player1)
    board.update(1, 0, player2)
    board.update(1, 1, player1)
    board.update(1, 2, player2)
    board.update(2, 0, player2)
    board.update(2, 1, player1)
    board.update(2, 2, player2)
    assert board.over() == Result.GAME_DRAW