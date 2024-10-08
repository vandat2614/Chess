from piece import Chess, read_image, valid_position

class BlackKing(Chess):
    image = read_image('Images\\black_king.png')

    @classmethod
    def valid_positions(cls, position, grid):
        actions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        new_positions = []
        for action in actions:
            new_pos = (position[0] + action[0], position[1] + action[1])
            if valid_position(new_pos) and Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                new_positions.append(new_pos)

        if (position[0] == 0 and position[1] == 4):
            if grid[0][0] == Chess.BLACK_ROOK and grid[0][1] == grid[0][2] == grid[0][3] == 0:
                new_positions.append((0, 2))

            if grid[0][7] == Chess.BLACK_ROOK and grid[0][5] == grid[0][6] == 0:
                new_positions.append((0, 6))

        return new_positions

class BlackQueen(Chess):
    image = read_image('Images\\black_queen.png')

    @classmethod
    def valid_positions(cls, position, grid):
        new_positions = list(set(BlackRook.valid_positions(position, grid) + BlackBishop.valid_positions(position, grid)))
        return new_positions

class BlackRook(Chess):
    image = read_image('Images\\black_rook.png')

    @classmethod
    def valid_positions(cls, position, grid):
        new_positions = []

        # <-
        for dis in range(1, 8):
            new_pos = (position[0], position[1] - dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break
        
        # ->
        for dis in range(1, 8):
            new_pos = (position[0], position[1] + dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        # up
        for dis in range(1, 8):
            new_pos = (position[0] - dis, position[1])
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        # down
        for dis in range(1, 8):
            new_pos = (position[0] + dis, position[1])
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        return new_positions

class BlackKnight(Chess):
    image = read_image('Images\\black_knight.png')

    @classmethod
    def valid_positions(cls, position, grid):
        actions = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, 2), (1, -2)]
        new_positions = []
        for action in actions:
            new_pos = (position[0] + action[0], position[1] + action[1])
            if valid_position(new_pos) and Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                new_positions.append(new_pos)
        return new_positions

class BlackBishop(Chess):
    image = read_image('Images\\black_bishop.png')

    @classmethod
    def valid_positions(cls, position, grid):
        new_positions = []

        # left up
        for dis in range(1, 8):
            new_pos = (position[0] - dis, position[1] - dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break
        
        # right up
        for dis in range(1, 8):
            new_pos =(position[0] - dis, position[1] + dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        # right down
        for dis in range(1, 8):
            new_pos = (position[0] + dis, position[1] + dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        # left down
        for dis in range(1, 8):
            new_pos = (position[0] + dis, position[1] - dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.BLACK:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        return new_positions
        
class BlackPawn(Chess):
    image = read_image('Images\\black_pawn.png')

    @classmethod
    def valid_positions(cls, position, grid):
        moves = []

        if grid[position[0] + 1][position[1]] == 0:
            moves.append((position[0] + 1, position[1]))
            
            if position[0] == 1 and grid[position[0] + 2][position[1]] == 0:
                moves.append((position[0] + 2, position[1]))


        if valid_position((position[0] + 1, position[1] - 1)) and Chess.type(grid[position[0] + 1][position[1] - 1]) == Chess.WHITE:
            moves.append((position[0] + 1, position[1] - 1))
        
        if valid_position((position[0] + 1, position[1] + 1)) and Chess.type(grid[position[0] + 1][position[1] + 1]) == Chess.WHITE:
            moves.append((position[0] + 1, position[1] + 1))

        return moves


class WhiteKing(Chess):
    image = read_image('Images\\white_king.png')

    @classmethod
    def valid_positions(cls, position, grid):
        actions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        new_positions = []
        for action in actions:
            new_pos = (position[0] + action[0], position[1] + action[1])
            if valid_position(new_pos) and Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                new_positions.append(new_pos)
            
        if (position[0] == 7 and position[1] == 4):
            if grid[7][0] == Chess.WHITE_ROOK and grid[7][1] == grid[7][2] == grid[7][3] == 0:
                new_positions.append((7, 2))
            
            if grid[7][7] == Chess.WHITE_ROOK and grid[7][5] == grid[7][6] == 0:
                new_positions.append((7, 6))

        return new_positions


class WhiteQueen(Chess):
    image = read_image('Images\\white_queen.png')

    @classmethod
    def valid_positions(cls, position, grid):
        new_positions = list(set(WhiteRook.valid_positions(position, grid) + WhiteBishop.valid_positions(position, grid)))
        return new_positions

class WhiteRook(Chess):
    image = read_image('Images\\white_rook.png')

    @classmethod
    def valid_positions(cls, position, grid):
        new_positions = []

        # <-
        for dis in range(1, 8):
            new_pos = (position[0], position[1] - dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break
        
        # ->
        for dis in range(1, 8):
            new_pos = (position[0], position[1] + dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        # up
        for dis in range(1, 8):
            new_pos = (position[0] - dis, position[1])
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        # down
        for dis in range(1, 8):
            new_pos = (position[0] + dis, position[1])
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        return new_positions

class WhiteKnight(Chess):
    image = read_image('Images\\white_knight.png')

    @classmethod
    def valid_positions(cls, position, grid):
        actions = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, 2), (1, -2)]
        new_positions = []
        for action in actions:
            new_pos = (position[0] + action[0], position[1] + action[1])
            if valid_position(new_pos) and Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                new_positions.append(new_pos)
        return new_positions
    
class WhiteBishop(Chess):
    image = read_image('Images\\white_bishop.png')

    @classmethod
    def valid_positions(cls, position, grid):
        new_positions = []

        # left up
        for dis in range(1, 8):
            new_pos = (position[0] - dis, position[1] - dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break
        
        # right up
        for dis in range(1, 8):
            new_pos = (position[0] - dis, position[1] + dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        # right down
        for dis in range(1, 8):
            new_pos = (position[0] + dis, position[1] + dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        # left down
        for dis in range(1, 8):
            new_pos = (position[0] + dis, position[1] - dis)
            if valid_position(new_pos):
                value = grid[new_pos[0]][new_pos[1]]
                if Chess.type(grid[new_pos[0]][new_pos[1]]) != Chess.WHITE:
                    new_positions.append(new_pos)
                if value != 0:
                    break
            else: break

        return new_positions


    
class WhitePawn(Chess):
    image = read_image('Images\\white_pawn.png')

    @classmethod
    def valid_positions(cls, position, grid):
        new_positions = []

        if grid[position[0]-1][position[1]] == 0:
            new_positions.append((position[0] - 1, position[1]))

            if position[0] == 6 and grid[position[0] - 2][position[1]] == 0:
                new_positions.append((position[0] - 2, position[1]))

        if valid_position((position[0] - 1, position[1] - 1)) and  Chess.type(grid[position[0] - 1][position[1] - 1]) == Chess.BLACK:
            new_positions.append((position[0] - 1, position[1] - 1))
        
        if valid_position((position[0] - 1, position[1] + 1)) and Chess.type(grid[position[0] - 1][position[1] + 1]) == Chess.BLACK:
            new_positions.append((position[0] - 1, position[1] + 1))

        return new_positions