import copy
import random 

# Students will write
def create_initial_board():
    """
        Creates an empty board of 4 rows, 4 columns with all empty tiles
    """
    board = []

    # Create 4 empty rows
    for row_num in range(4):
        row = []
        # Fill each row with 4 empty columns
        for column_num in range(4):
            row.append(0)
        
        board.append(row) # Add row to board

    return board

# Students will write
def return_empty_tiles(board):
    """
        Searches the board for empty tiles and returns a list
    """
    empty_tiles = []

    # go through each row and column
    for row_index in range(4): 
        for column_index in range(4):
            # check for an empty tile and add to list
            if board[row_index][column_index] == 0: 
                empty_tiles.append((row_index, column_index))      
                
    return empty_tiles

# Prewritten function
def insert_random_tile(board):
    """
        Randomly picks an empty tile on the board to insert 2 into.
        Returns False if there are no empty tiles left, and True otherwise.
    """

    empty_tiles = return_empty_tiles(board)       
     
    if (len(empty_tiles) > 0): 
        # Pick an empty tile randomly
        random_index = random.randint(0, len(empty_tiles)-1) 
        empty_tile = empty_tiles[random_index]

        # Set the empty tile's value to 2
        board[empty_tile[0]][empty_tile[1]] = 2  
        # Additional challenge - can a student make it so sometimes a 4 can spawn? 

        return True
    else: 
        # No more empty tiles
        return False
    
# Prewritten function
def display_board(board):
    """
        Prints the board with improved readbility.
    """

    for row in board:
        print("[", end="")
        for item in row:
            print(' %3d ' % item, end = "") 
        print("]")

    print()


# Prewritten function
def push(direction, board):  
    """
        Given a direction, the tiles on the board will first compress 
        (values slide across empty tiles), merge (any matching pairs are doubled),
        and then compress again.
    """

    # Pushing is done recursively.
    board = push_recurse(direction, board, create_initial_board(), "compress")
    board = push_recurse(direction, board, create_initial_board(), "merge")
    return push_recurse(direction, board, create_initial_board(), "compress")


# Prewritten function
def push_recurse(direction, current_board, past_board, mode):
    """
        Recursively goes through the board in order to compress or merge tiles, 
        depending on the mode.
    """

    if(current_board == past_board): # no further changes can be made
        return current_board
    
    else:
        # Set the past board to the current board before any changes
        past_board = copy.deepcopy(current_board)

        # Go through each tile and 
        # check if tile pairs in the corresponding direction can be combined
        # Direction is determined by the range() function and adding/subtracting for a row or colum
        if(direction == "left"):
            for row_index in range(0, 4, 1):
                for col_index in range(0, 3, 1):
                    combine_tiles(current_board, 
                                  (row_index, col_index), 
                                  (row_index, col_index + 1), mode)
        elif(direction == "right"):
            for row_index in range(0, 4, 1):
                for col_index in range(3, 0, -1):
                    combine_tiles(current_board, 
                                  (row_index, col_index), 
                                  (row_index, col_index - 1), mode)
        elif (direction=="up"):
            for row_index in range(1, 4, 1):
                for col_index in range(0, 4, 1):
                    combine_tiles(current_board, 
                                  (row_index - 1, col_index), 
                                  (row_index, col_index), mode)
        elif (direction=="down"):
            for row_index in range(2, -1, -1):
                for col_index in range(0, 4, 1):
                    combine_tiles(current_board, 
                                  (row_index + 1, col_index), 
                                  (row_index, col_index), mode)
        
        push_recurse(direction, current_board, past_board, mode)

    return board

# Prewritten function
def combine_tiles(board, current_tile, pushed_tile, mode):
    global high_score
    current_tile_value = board[current_tile[0]][current_tile[1]]
    pushed_tile_value = board[pushed_tile[0]][pushed_tile[1]]

    if mode == "merge": # values slide across empty tiles
        if (current_tile_value == pushed_tile_value and current_tile_value!=0):
            board[current_tile[0]][current_tile[1]] = current_tile_value * 2
            board[pushed_tile[0]][pushed_tile[1]] = 0
            
            # update the high score variable accordingly
            if (current_tile_value * 2 > high_score):
                high_score = current_tile_value *2 
    if mode == "compress":  # any matching pairs are "added together"
        if (current_tile_value == 0 and pushed_tile_value!=0):
            # the current tile takes on double it's value
            board[current_tile[0]][current_tile[1]] = pushed_tile_value 
            # the tile that was just "pushed" becomes empty
            board[pushed_tile[0]][pushed_tile[1]] = 0
    

print("Let's play 2048")
board = create_initial_board()
insert_random_tile(board)

high_score = 0
while(insert_random_tile(board) != False):
    print()
    display_board(board)

    move = input("Use w,a,s,d to pick a direction to move or q to quit")
    while move not in ("w", "a", "s", "d", "q"):
        print("Error. Please re-enter a proper direction")
        move = input("Use w,a,s,d to pick a direction to move")
    if(move == "w"):
        push("up", board)
    elif(move == "a"):
        push("left", board)
    elif(move == "s"):
        push("down", board)
    elif(move == "d"):
        push("right", board)
    elif(move=="q"):
        print("User has quit game")
        break

print("Game over")
print(f"High score: {high_score}")
