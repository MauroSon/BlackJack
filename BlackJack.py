from random import randrange 



def init_round():
    draw_pile = create_draw_pile()

def game():
    User_Points = 0
    #Inicia game
        match = 1
        #inicia a partida (loop até derrota)
        
        #inicia o round (loop até parar, perder ou ganhar)
            ## player compra
            ## dealer compra
                ##decisao (compra ou para)
    

def is_bust(handValue):
    return handValue > 21

def create_draw_pile(): 
    draw_pile = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] * 4
    return draw_pile


def draw_card(hand_deck, draw_pile):
    i = randrange(len(draw_pile))
    drawn_card = draw_pile.pop(i)
    
    hand_deck.append(drawn_card)
    

deck = create_deck()