#!/usr/bin/env python
# coding: utf-8

# In[16]:


def chess_board_validator(board_model):
    
    import string
    current_piece_count = {}
    white_piece_count = 0
    black_piece_count = 0

    def initial_validation(board_model):
        
        nonlocal white_piece_count
        nonlocal black_piece_count 
        
        for coordinate, one_piece in board_model.items():

            if len(coordinate) != 2             or not coordinate[0].isnumeric()             or int(coordinate[0]) not in range(1,9)             or coordinate[1] not in string.ascii_lowercase[:8]             or type(one_piece) != str:
                return(False)

            if one_piece[0] == 'w':
                 white_piece_count += 1
            elif one_piece[0] == 'b':
                 black_piece_count += 1
            else:
                return(False)
            
            current_piece_count.setdefault(one_piece, 0)
            current_piece_count[one_piece] += 1
        
        return(True)
            
    def count_validation(current_piece_count):
        
        if white_piece_count > 16         or black_piece_count > 16         or current_piece_count.pop('wking', 0) != 1         or current_piece_count.pop('bking', 0) != 1         or current_piece_count.pop('wpawn', 0) > 8         or current_piece_count.pop('bpawn', 0) > 8:
            return(False)
        
        current_piece_count.pop('wqueen', None) 
        current_piece_count.pop('bqueen', None)
        
        #all pieces that may be above a count of 2 in a valid board have been validated, then removed from current_piece_count

        for i in current_piece_count.values():

            if i > 2:
                return(False)
            
        return(True)
    
    
    #####        
            
    
    
    if initial_validation(board_model) and count_validation(current_piece_count):
        return(True)
    else:
        return(False)
    
board_model_ex = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '1e': 'wking',}

chess_board_validator(board_model_ex)


# In[ ]:




