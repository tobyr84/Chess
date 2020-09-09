"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        if self.player == Player.WHITE:
            square = board.find_piece(self)

            if square.row == 1:
                next_square_1 = Square.at(square.row + 1, square.col)
                next_square_2 = Square.at(square.row + 2, square.col)
                results = [next_square_1, next_square_2]
            else:
                next_square_1 = Square.at(square.row + 1, square.col)
                results = [next_square_1]

        elif self.player == Player.BLACK:
            square = board.find_piece(self)
            if square.row == 6:
                next_suqare_6 = Square.at(square.row - 1, square.col)
                next_square_5 = Square.at(square.row - 2, square.col)
                results = [next_suqare_6, next_square_5]
            else:
                next_square = Square.at(square.row - 1, square.col)
                results = [next_square]
        new_results = [] 
        for square in results:
            piece = board.get_piece(square)
            if piece == None:
                new_results.append(square)   
        return new_results


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []