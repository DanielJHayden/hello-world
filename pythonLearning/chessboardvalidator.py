def chess_board_validator(board_model):
    import string
    current_piece_count = {}
    white_piece_count = 0
    black_piece_count = 0

    for coordinate, one_piece in board_model.items():

        if len(coordinate) != 2 \
        or not coordinate[0].isnumeric() \
        or int(coordinate[0]) not in range(1,9) \
        or coordinate[1] not in string.ascii_lowercase[:8] \
        or type(one_piece) != str:
            return(False)

        if one_piece[0] == 'w':
            white_piece_count += 1
        elif one_piece[0] == 'b':
            black_piece_count += 1
        else:
            return(False)

        if white_piece_count > 16 or black_piece_count > 16:
            return(False)    
        current_piece_count.setdefault(one_piece, 0)
        current_piece_count[one_piece] += 1

    current_piece_count.pop('wqueen', None) 
    current_piece_count.pop('bqueen', None)

    if current_piece_count.pop('wking', 0) != 1 \
    or current_piece_count.pop('bking', 0) != 1 \
    or current_piece_count.pop('wpawn', 0) > 8 \
    or current_piece_count.pop('bpawn', 0) > 8:
        return(False)
    #all pieces that may be above a count of 2 in a valid board have been removed from current_piece_count

    for i in current_piece_count.values():

        if i > 2:
            return(False)

    return(True)
    
board_model = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(chess_board_validator(board_model))