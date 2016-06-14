# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:31:46 2016

@author: Adrien
"""



import random


    
    

def pull_card():
    '''
    Be careful there might be a problem with the random attribution
    of numbers in this function.
    '''
    num_rank = random.randint(0,12)
    #num_rank = int(13*random.randrange(0,1,1000))
        
    if num_rank < 10:
        rank='0'+str(num_rank)
    else:
        rank=str(num_rank)
                    
    num_suit = random.randint(0,3)
    if num_suit == 0:
        suit='S'
    elif num_suit == 1:
        suit='H'
    elif num_suit == 2:
        suit='D'
    else:
        suit='C'
        
    return rank+suit
    
    
    
    
    
    
    
    




'''


def distribution(cards_list=[],nb_cards=7,forbidden=[]):
'''
'''
    Distribution of cards for completion of the list cards_list
    to reach a number of nb_cards cards.
    Think of adding a list of forbidden cards which cannot be pulled.
    The whole function could be re-written in a clearer way using
    if card in cards_list.
'''
'''
    
    i=len(cards_list)
    
    while i < nb_cards:
        
        
        card_already_pulled = True

        while card_already_pulled == True:
            
            # pull of a random card
            card = pull_card()
            if card in forbidden:
                card = pull_card()
            
            # need of verifying if last card pulled hasn't been already pulled or doesn't belong to the forbidden list
            j=0
            test_card_presence = False
            while j < i and test_card_presence == False:
                if cards_list[j] == card:
                    test_card_presence = True
                else:
                    test_card_presence = False
                    
                j+=1
            
            if test_card_presence == False:
                card_already_pulled = False
        
        
        cards_list += [card]
        #print(cards_list)
        
        i+=1
        
    return cards_list
    

'''






def distribution(cards_list=[],nb_cards=7,forbidden=[]):
    '''
    Distribution of cards for completion of the list cards_list
    to reach a number of nb_cards cards.
    Think of adding a list of forbidden cards which cannot be pulled.
    The whole function could be re-written in a clearer way using
    if card in cards_list.
    '''
    
    cards_list_copy = cards_list[:]
    
    i = len(cards_list_copy)
    
    while i < nb_cards:
        
        card = pull_card()
        
        while card in forbidden:
            card = pull_card()
        
        print('card:',card)
        
        cards_list_copy += [card]
        
        i+=1
    
    
    return cards_list_copy










