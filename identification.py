# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:27:39 2016

@author: Adrien
"""

 
    






def identification(hand_and_board):
    
    if len(hand_and_board) != 7:
        print('Error: length of hand_and_board inadapted (in identification)')
        return 1
    
    ranks = 13*[0]
    
    i=0
    while i < 7:
        card_rank = int(hand_and_board[i][0:2])
        
        ranks[card_rank] += 1
        
        i+=1
    
    straight_flush = False
    test_straight = False
    i=-1
    stop = False
    while i < 9 and stop == False:
        straight_count=0
        if ranks[i] == 0:
            i+=1
        else:
            straight_count+=1
            index_range_ok = True
            j=i+1
            while index_range_ok == True and ranks[j]!=0:
                straight_count+=1
                j+=1
                if j>=13:
                    index_range_ok = False
                    j=12
            
            if index_range_ok == False:
                j=13
            
            if straight_count >= 5:
                test_straight = True
                rank_straight = j-1
                
            i=j+1
    
    
    if test_straight == True:
        suit=4*[0]
        
        i=0
        while i < 7:
            if int(hand_and_board[i][0:2])>=j-5 and int(hand_and_board[i][0:2])<=j-1:
                if hand_and_board[i][2]=='S':
                    suit[0]+=1
                if hand_and_board[i][2]=='H':
                    suit[1]+=1
                if hand_and_board[i][2]=='D':
                    suit[2]+=1
                if hand_and_board[i][2]=='C':
                    suit[3]+=1
            i+=1
            
        if suit[0]==5 or suit[1]==5 or suit[2]==5 or suit[3]==5:
            straight_flush = True
    
    
    if straight_flush == True:
        return {'comb':'straight_flush','rank':8,'value':[rank_straight]}
    
    # Quads
    else:
        quads=False
        i=0
        while i < 13:
            if ranks[i]==4:
                quads=True
                rank_quads=[i]
            
            i+=1
        
        if quads == True:
            return {'comb':'quads','rank':7,'value':rank_quads}
        
        # Full
        else:
            nb_pairs=0
            rank_highest_pair=0
            rank_second_pair=0
            
            nb_trips=0
            rank_highest_trips=0
            
            i=0
            while i < 13:
                if ranks[i]==3:
                    nb_trips+=1
                    
                    if rank_highest_trips < i:
                        rank_highest_trips=i
                
                if ranks[i]==2:
                    nb_pairs+=1
                    
                    if rank_highest_pair < i:
                        rank_second_pair=rank_highest_pair
                        rank_highest_pair=i
                
                i+=1
                
                
                
            if nb_trips >= 1 and nb_pairs >= 1:
                
                value_full = [rank_highest_trips,rank_highest_pair]
                
                return {'comb':'full','rank':6,'value':value_full}
            
            # Flush
            else:
                
                flush = False
                
                suit=4*[0]
                rank_suit=4*[7*[0]]
                i=0
                while i < 7:
                    if hand_and_board[i][2]=='S':
                        suit[0]+=1
                        if int(hand_and_board[i][0:2]) > rank_suit[0][0]:
                            rank_suit[0][4] = rank_suit[0][3]
                            rank_suit[0][3] = rank_suit[0][2]
                            rank_suit[0][2] = rank_suit[0][1]
                            rank_suit[0][1] = rank_suit[0][0]
                            rank_suit[0][0] = int(hand_and_board[i][0:2])
                            
                    elif hand_and_board[i][2]=='H':
                        suit[1]+=1
                        if int(hand_and_board[i][0:2]) > rank_suit[1][0]:
                            rank_suit[1][4] = rank_suit[1][3]
                            rank_suit[1][3] = rank_suit[1][2]
                            rank_suit[1][2] = rank_suit[1][1]
                            rank_suit[1][1] = rank_suit[1][0]
                            rank_suit[1][0] = int(hand_and_board[i][0:2])
                        
                    elif hand_and_board[i][2]=='D':
                        suit[2]+=1
                        if int(hand_and_board[i][0:2]) > rank_suit[2][0]:
                            rank_suit[2][4] = rank_suit[2][3]
                            rank_suit[2][3] = rank_suit[2][2]
                            rank_suit[2][2] = rank_suit[2][1]
                            rank_suit[2][1] = rank_suit[2][0]
                            rank_suit[2][0] = int(hand_and_board[i][0:2])
                    else:
                        suit[3]+=1
                        if int(hand_and_board[i][0:2]) > rank_suit[3][0]:
                            rank_suit[3][4] = rank_suit[3][3]
                            rank_suit[3][3] = rank_suit[3][2]
                            rank_suit[3][2] = rank_suit[3][1]
                            rank_suit[3][1] = rank_suit[3][0]
                            rank_suit[3][0] = int(hand_and_board[i][0:2])
                            
                    i+=1   
                    
                    
            
                if suit[0]>=5:
                    flush = True
                    rank_flush = rank_suit[0]
                    
                elif suit[1]>=5:
                    flush = True
                    rank_flush = rank_suit[1]
                
                elif suit[2]>=5:
                    flush = True
                    rank_flush = rank_suit[2]
                
                elif suit[3]>=5:
                    flush = True
                    rank_flush = rank_suit[3]
    
                if flush == True:
                    return {'comb':'flush','rank':5,'value':rank_flush}
                
                # Straight
                else:
                    
                    if test_straight == True:
                        return {'comb':'straight','rank':4,'value':[rank_straight]}
                    
                    # Trips
                    else:
                    
                        if nb_trips >= 1:
                            
                            '''
                            highest_single_cards = []
                                
                            i=12
                            # test_single_cards is here to control the length of the highest_single_cards list
                            test_single_cards = 0
                            while i>0 and test_single_cards != 2:
                                if ranks[i] == 1:
                                    highest_single_cards += [i]
                                    test_single_cards += 1
                                
                                i-=1
                            '''
                            
                            forbidden_trips = [rank_highest_trips]
                            
                            value_trips = [rank_highest_trips] + highest_single_cards(ranks,2,forbidden_trips)
                            
                            return {'comb':'trips','rank':3,'value':value_trips}
                        
                        # Two pairs
                        else:
                            
                            if nb_pairs >= 2:
                                
                                '''
                                highest_single_cards = []
                                
                                i=12
                                # test_single_cards is here to control the length of the highest_single_cards list
                                test_single_cards = 0
                                while i>0 and test_single_cards != 1:
                                    if ranks[i] == 1:
                                        highest_single_cards += [i]
                                        test_single_cards += 1
                                    
                                    i-=1
                                '''
                                
                                forbidden_two_pairs = [rank_highest_pair,rank_second_pair]
                                    
                                value_two_pairs = [rank_highest_pair,rank_second_pair] + highest_single_cards(ranks,1,forbidden_two_pairs)
                                
                                return {'comb':'two_pairs','rank':2,'value':value_two_pairs}
                                
                            # Pair
                            else:
                                 if nb_pairs == 1:
                                     
                                     
                                     '''
                                     highest_single_cards = []
                                
                                     i=12
                                     # test_single_cards is here to control the length of the highest_single_cards list
                                     test_single_cards = 0
                                     while i>0 and test_single_cards != 3:
                                         if ranks[i] == 1:
                                             highest_single_cards += [i]
                                             test_single_cards += 1
                                         i-=1
                                     '''
                                     
                                     forbidden_pair = [rank_highest_pair]
                                    
                                     value_pair = [rank_highest_pair] + highest_single_cards(ranks,3,forbidden_pair)
                                     
                                     return {'comb':'pair','rank':1,'value':value_pair}
                                
                                 # High card
                                 else:
                                     
                                     value_high_card = highest_single_cards(ranks,5,[])
                                     
                                     '''
                                     highest_single_cards = []
                                
                                     i=12
                                     # test_single_cards is here to control the length of the highest_single_cards list
                                     test_single_cards = 0
                                     while i>0 and test_single_cards != 5:
                                         if ranks[i] == 1:
                                             highest_single_cards += [i]
                                             test_single_cards += 1
                                         i-=1
                                    
                                     value_high_card = highest_single_cards
                                     '''
                                     
                                     return {'comb':'high_card','rank':0,'value':value_high_card}
                                    
    
    
    
    
    
    
    
    
    
    
    
    
def highest_single_cards(ranks,nb_cards_needed,forbidden):
    
    print('ranks:',ranks)
    print('forbidden:',forbidden)
    
    highest_single_cards = []
                                
    i=12
    # test_single_cards is here to control the length of the highest_single_cards list
    test_single_cards = 0
    while i>=0 and test_single_cards != nb_cards_needed:
        if ranks[i] != 0 and i not in forbidden:
            highest_single_cards += [i]
            test_single_cards += 1
        
        print(i)
        i-=1
                                    
    return highest_single_cards
    
    
    
    
    
    