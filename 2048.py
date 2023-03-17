import random 

# Students will be using
def display_board(board):
    for row in board:
        print(row)
    print()

# Students will be using
def insert_random_tile(board):
    empty_tiles = return_empty_tiles(board)            
    if (len(empty_tiles) !=0):
        random_index = random.randint(0, len(empty_tiles)-1) 
        empty_tile = empty_tiles[random_index]
        board[empty_tile[0]][empty_tile[1]] = 2
        return True
    return False

# Students will be using
def create_initial_board():
    board = []
    for row_index in range(4):
        row = []
        for column_index in range(4):
            row.append(0)
        board.append(row)
    return board

# Students will be using
def push(direction, board):  
    if(direction == "left"):
        for row_index in range(0, 4, 1):
            for col_index in range(0, 3, 1):
                combineTiles(board, (row_index, col_index), (row_index, col_index + 1))
    elif(direction == "right"):
        for row_index in range(0, 4, 1):
            for col_index in range(3, 0, -1):
                combineTiles(board, (row_index, col_index), (row_index, col_index - 1))
    elif (direction=="up"):
        for row_index in range(1, 4, 1):
            for col_index in range(0, 4, 1):
                combineTiles(board, (row_index - 1, col_index), (row_index, col_index))
    elif (direction=="down"):
        for row_index in range(2, 0, -1):
            for col_index in range(0, 4, 1):
                combineTiles(board, (row_index + 1, col_index), (row_index, col_index))
    else: 
        print("Invalid Direction")               
    return board

# INTERNAL FUNCTION
def combineTiles(board, current_tile, pushed_tile):
    current_tile_value = board[current_tile[0]][current_tile[1]]
    pushed_tile_value = board[pushed_tile[0]][pushed_tile[1]]
    if (current_tile_value == pushed_tile_value):
        board[current_tile[0]][current_tile[1]] = current_tile_value * 2
        board[pushed_tile[0]][pushed_tile[1]] = 0

    if (current_tile_value == 0 and pushed_tile_value!=0):
        board[current_tile[0]][current_tile[1]] = pushed_tile_value
        board[pushed_tile[0]][pushed_tile[1]] = 0
    
# INTERNAL FUNCTION
def return_empty_tiles(board):
    empty_tiles = []
    for row_index in range(4): 
        for column_index in range(4):
            if board[row_index][column_index] == 0: 
                empty_tiles.append((row_index, column_index))      
    return empty_tiles

board = [[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 2], [0, 0, 0, 0]]
display_board(board)
push("down", board)
display_board(board)
push("left", board)
display_board(board)

