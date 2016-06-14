# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:26:09 2016

@author: Adrien
"""




from pomal.identification import identification






def winner_determination(card_hands,board):
    '''
    Determine the best card set amongst all the sets provided as
    input using the identification function.
    card_hands must be a list containing the hands playing against
    each other (recall that a hand is a list containing 2 cards).
    board is a list containing the 5 cards of the board.
    This function outputs the index of the winning hand in the
    input list called card_hands.
    '''
    
    nb_hands = len(card_hands)
    
    combinations=[]
    values=[]
    
    i=0
    while i < nb_hands:
        comb = identification(card_hands[i]+board)['rank']
        combinations += [comb]
        
        val = identification(card_hands[i]+board)['value']
        values += [val]
        
        i+=1
    
    best_rank = max(combinations)
    nb_occurence = combinations.count(best_rank)
        
    if nb_occurence == 1:
        best_index = combinations.index(best_rank)
        return [best_index]
    
    else:
        index_list=[]
        start=0
        
        i=0
        while i < nb_occurence:
            index = start + combinations[start:].index(best_rank)
            start = index+1
            
            # index_list contains index of the players still in game
            index_list += [index]
            
            i+=1
        
        
        loop_max = len(values[index_list[0]])
        j=0
        while j < loop_max:
            # remaining_values contains the value held by each player still in game
            remaining_values = []
            
            for a in index_list:
                remaining_values += [values[a][j]]
                
            best_value = max(remaining_values)
            nb_occurence_values = remaining_values.count(best_value)
            
            if nb_occurence_values == 1:
                winner_remaining_index = remaining_values.index(best_value)
                winner_index = index_list[winner_remaining_index]
                return [winner_index]
            
            # update of index_list only keeping the best values
            start=0
            new_index_list=[]
            i=0
            while i < nb_occurence_values:
                # remaining_index contains the indexes corresponding to the max values of the list remaining_values
                print('remaining_values:',remaining_values)
                print('start:',start)
                remaining_index = start + remaining_values[start:].index(best_value)
                start = remaining_index+1
                new_index_list += [index_list[remaining_index]]
            
                i+=1
            
            index_list = new_index_list
            
            j+=1
            
        
        return index_list
        