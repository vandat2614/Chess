from chess_piece import Chess

class King(Chess):
    def __init__(self, id):
        super().__init__(id, 'king')

class Queen(Chess):
    def __init__(self, id):
        super().__init__(id, 'queen')

class Rook(Chess):
    def __init__(self, id):
        super().__init__(id, 'rook')

class Knight(Chess):
    def __init__(self, id):
        super().__init__(id, 'knight')

class Bishop(Chess):
    def __init__(self, id):
        super().__init__(id, 'bishop')

class Pawn(Chess):
    def __init__(self, id):
        super().__init__(id, 'pawn')
