import random 

def display_board(board):
    for row in board:
        print(row)

def create_initial_board():
    board = []
    for row_index in range(4):
        row = []
        for column_index in range(4):
            row.append(0)
        board.append(row)
    return board

def push(direction, board):        
    # if (direction=="left"):
    #     for row_index in range(0, 4, 1): # start (inclusive), stop (exclusive), step
    #         for column_index in range(2, -1, -1):
    #             combineTiles(board, (row_index, column_index), (row_index, column_index + 1))
    # if (direction=="right"):
    #     for row_index in range(0, 4, 1):
    #         for column_index in range(0, 3, 1):
    #             combineTiles(board, (row_index, column_index), (row_index, column_index - 1))
    # elif (direction=="up"):
    #     for row_index in range(1, 4, 1):
    #         for column_index in range(0, 4, 1):
    #             combineTiles(board, (row_index, column_index), (row_index+1, column_index))
    # elif (direction=="down"):
    #     for row_index in range(4, -1, -1):
    #         for column_index in range(0, 4, 1):
    #             combineTiles(board, (row_index, column_index), (row_index-1, column_index))
    return 

def combineTiles(board, current_tile, pushed_tile):
    current_tile_value = board[current_tile[0]][current_tile[1]]
    pushed_tile_value = board[pushed_tile[0]][pushed_tile[1]]
    if (current_tile_value == pushed_tile_value):
        board[current_tile[0]][current_tile[1]] = current_tile_value * 2
        board[pushed_tile[0]][pushed_tile[1]] = 0

    if (current_tile_value == 0 and pushed_tile_value!=0):
        board[current_tile[0]][current_tile[1]] = pushed_tile_value
        board[pushed_tile[0]][pushed_tile[1]] = 0
    

def insert_random_tile(board):
    empty_tiles = return_empty_tiles(board)            
    if (len(empty_tiles) !=0):
        random_index = random.randint(0, len(empty_tiles)-1) 
        empty_tile = empty_tiles[random_index]
        board[empty_tile[0]][empty_tile[1]] = 2
        return True
    return False
    

def return_empty_tiles(board):
    empty_tiles = []
    for row_index in range(4): 
        for column_index in range(4):
            if board[row_index][column_index] == 0: 
                empty_tiles.append((row_index, column_index))      
    return empty_tiles

board = []
board = create_initial_board()
display_board(board)
