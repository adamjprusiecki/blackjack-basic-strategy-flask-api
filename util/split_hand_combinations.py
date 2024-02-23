split_hand_combinations = (
    #Dealer_Card, Player_Card_1, Player_Card_2, Expected_Move
    
    ('2', 'A', 'A', 'y'), 
    ('2', 'K', 'K', 'n'), 
    ('2', 'Q', 'Q', 'n'), 
    ('2', 'J', 'J', 'n'), 
    ('2', '10', '10', 'n'), 
    ('2', 'T', 'T', 'n'), 
    ('2', '9', '9', 'y'), 
    ('2', '8', '8', 'y'), 
    ('2', '7', '7', 'y'), 
    ('2', '6', '6', 'yn'),
    ('2', '5', '5', 'n'), 
    ('2', '4', '4', 'n'), 
    ('2', '3', '3', 'yn'),
    ('2', '2', '2', 'yn'),
    
    ('3', 'A', 'A', 'y'), 
    ('3', 'K', 'K', 'n'), 
    ('3', 'Q', 'Q', 'n'), 
    ('3', 'J', 'J', 'n'), 
    ('3', '10', '10', 'n'), 
    ('3', 'T', 'T', 'n'), 
    ('3', '9', '9', 'y'), 
    ('3', '8', '8', 'y'), 
    ('3', '7', '7', 'y'), 
    ('3', '6', '6', 'y'),
    ('3', '5', '5', 'n'), 
    ('3', '4', '4', 'n'), 
    ('3', '3', '3', 'yn'),
    ('3', '2', '2', 'yn'),
    
    ('4', 'A', 'A', 'y'),
    ('4', 'K', 'K', 'n'), 
    ('4', 'Q', 'Q', 'n'), 
    ('4', 'J', 'J', 'n'), 
    ('4', '10', '10', 'n'),
    ('4', 'T', 'T', 'n'), 
    ('4', '9', '9', 'y'), 
    ('4', '8', '8', 'y'), 
    ('4', '7', '7', 'y'), 
    ('4', '6', '6', 'y'),
    ('4', '5', '5', 'n'), 
    ('4', '4', '4', 'n'), 
    ('4', '3', '3', 'y'),
    ('4', '2', '2', 'y'),
    
    ('5', 'A', 'A', 'y'),
    ('5', 'K', 'K', 'n'), 
    ('5', 'Q', 'Q', 'n'), 
    ('5', 'J', 'J', 'n'), 
    ('5', '10', '10', 'n'), 
    ('5', 'T', 'T', 'n'), 
    ('5', '9', '9', 'y'), 
    ('5', '8', '8', 'y'), 
    ('5', '7', '7', 'y'), 
    ('5', '6', '6', 'y'),
    ('5', '5', '5', 'n'), 
    ('5', '4', '4', 'yn'), 
    ('5', '3', '3', 'y'),
    ('5', '2', '2', 'y'),
    
    ('6', 'A', 'A', 'y'), 
    ('6', 'K', 'K', 'n'), 
    ('6', 'Q', 'Q', 'n'), 
    ('6', 'J', 'J', 'n'), 
    ('6', '10', '10', 'n'),
    ('6', 'T', 'T', 'n'), 
    ('6', '9', '9', 'y'), 
    ('6', '8', '8', 'y'), 
    ('6', '7', '7', 'y'), 
    ('6', '6', '6', 'y'),
    ('6', '5', '5', 'n'), 
    ('6', '4', '4', 'yn'), 
    ('6', '3', '3', 'y'),
    ('6', '2', '2', 'y'),
    
    ('7', 'A', 'A', 'y'),
    ('7', 'K', 'K', 'n'), 
    ('7', 'Q', 'Q', 'n'), 
    ('7', 'J', 'J', 'n'), 
    ('7', '10', '10', 'n'), 
    ('7', 'T', 'T', 'n'), 
    ('7', '9', '9', 'n'), 
    ('7', '8', '8', 'y'), 
    ('7', '7', '7', 'y'), 
    ('7', '6', '6', 'n'),
    ('7', '5', '5', 'n'), 
    ('7', '4', '4', 'n'), 
    ('7', '3', '3', 'y'),
    ('7', '2', '2', 'y'),

    ('8', 'A', 'A', 'y'),
    ('8', 'K', 'K', 'n'), 
    ('8', 'Q', 'Q', 'n'), 
    ('8', 'J', 'J', 'n'), 
    ('8', '10', '10', 'n'),
    ('8', 'T', 'T', 'n'), 
    ('8', '9', '9', 'y'), 
    ('8', '8', '8', 'y'), 
    ('8', '7', '7', 'n'), 
    ('8', '6', '6', 'n'),
    ('8', '5', '5', 'n'), 
    ('8', '4', '4', 'n'), 
    ('8', '3', '3', 'n'),
    ('8', '2', '2', 'n'),
    
    ('9', 'A', 'A', 'y'),
    ('9', 'K', 'K', 'n'), 
    ('9', 'Q', 'Q', 'n'), 
    ('9', 'J', 'J', 'n'), 
    ('9', '10', '10', 'n'),
    ('9', 'T', 'T', 'n'), 
    ('9', '9', '9', 'y'), 
    ('9', '8', '8', 'y'), 
    ('9', '7', '7', 'n'), 
    ('9', '6', '6', 'n'),
    ('9', '5', '5', 'n'), 
    ('9', '4', '4', 'n'), 
    ('9', '3', '3', 'n'),
    ('9', '2', '2', 'n'),
    
    ('10', 'A', 'A', 'y'),
    ('10', 'K', 'K', 'n'), 
    ('10', 'Q', 'Q', 'n'), 
    ('10', 'J', 'J', 'n'), 
    ('10', '10', '10', 'n'),
    ('10', 'T', 'T', 'n'), 
    ('10', '9', '9', 'n'), 
    ('10', '8', '8', 'y'), 
    ('10', '7', '7', 'n'), 
    ('10', '6', '6', 'n'),
    ('10', '5', '5', 'n'), 
    ('10', '4', '4', 'n'), 
    ('10', '3', '3', 'n'),
    ('10', '2', '2', 'n'),

    ('T', 'A', 'A', 'y'), 
    ('T', 'K', 'K', 'n'), 
    ('T', 'Q', 'Q', 'n'), 
    ('T', 'J', 'J', 'n'), 
    ('T', '10', '10', 'n'),
    ('T', 'T', 'T', 'n'), 
    ('T', '9', '9', 'n'), 
    ('T', '8', '8', 'y'), 
    ('T', '7', '7', 'n'), 
    ('T', '6', '6', 'n'),
    ('T', '5', '5', 'n'), 
    ('T', '4', '4', 'n'), 
    ('T', '3', '3', 'n'),
    ('T', '2', '2', 'n'),

    ('J', 'A', 'A', 'y'),
    ('J', 'K', 'K', 'n'), 
    ('J', 'Q', 'Q', 'n'), 
    ('J', 'J', 'J', 'n'), 
    ('J', '10', '10', 'n'),
    ('J', 'T', 'T', 'n'), 
    ('J', '9', '9', 'n'), 
    ('J', '8', '8', 'y'), 
    ('J', '7', '7', 'n'), 
    ('J', '6', '6', 'n'),
    ('J', '5', '5', 'n'), 
    ('J', '4', '4', 'n'), 
    ('J', '3', '3', 'n'),
    ('J', '2', '2', 'n'),

    ('Q', 'A', 'A', 'y'),
    ('Q', 'K', 'K', 'n'), 
    ('Q', 'Q', 'Q', 'n'), 
    ('Q', 'J', 'J', 'n'), 
    ('Q', '10', '10', 'n'),
    ('Q', 'T', 'T', 'n'), 
    ('Q', '9', '9', 'n'), 
    ('Q', '8', '8', 'y'), 
    ('Q', '7', '7', 'n'), 
    ('Q', '6', '6', 'n'),
    ('Q', '5', '5', 'n'), 
    ('Q', '4', '4', 'n'), 
    ('Q', '3', '3', 'n'),
    ('Q', '2', '2', 'n'),

    ('K', 'A', 'A', 'y'),
    ('K', 'K', 'K', 'n'), 
    ('K', 'Q', 'Q', 'n'), 
    ('K', 'J', 'J', 'n'), 
    ('K', '10', '10', 'n'),
    ('K', 'T', 'T', 'n'), 
    ('K', '9', '9', 'n'), 
    ('K', '8', '8', 'y'), 
    ('K', '7', '7', 'n'), 
    ('K', '6', '6', 'n'),
    ('K', '5', '5', 'n'), 
    ('K', '4', '4', 'n'), 
    ('K', '3', '3', 'n'),
    ('K', '2', '2', 'n'),

    ('A', 'A', 'A', 'y'), 
    ('A', 'K', 'K', 'n'), 
    ('A', 'Q', 'Q', 'n'), 
    ('A', 'J', 'J', 'n'), 
    ('A', '10', '10', 'n'),
    ('A', 'T', 'T', 'n'), 
    ('A', '9', '9', 'n'), 
    ('A', '8', '8', 'y'), 
    ('A', '7', '7', 'n'), 
    ('A', '6', '6', 'n'),
    ('A', '5', '5', 'n'), 
    ('A', '4', '4', 'n'), 
    ('A', '3', '3', 'n'),
    ('A', '2', '2', 'n'),
    
    ('2', '10', 'T', 'n'), 
    ('3', '10', 'T', 'n'), 
    ('4', '10', 'T', 'n'), 
    ('5', '10', 'T', 'n'), 
    ('6', '10', 'T', 'n'), 
    ('7', '10', 'T', 'n'), 
    ('8', '10', 'T', 'n'), 
    ('9', '10', 'T', 'n'), 
    ('10', '10', 'T', 'n'), 
    ('T', '10', 'T', 'n'), 
    ('J', '10', 'T', 'n'), 
    ('Q', '10', 'T', 'n'), 
    ('K', '10', 'T', 'n'), 
    ('A', '10', 'T', 'n'),
    
    ('2', '10', 'J', 'n'), 
    ('3', '10', 'J', 'n'), 
    ('4', '10', 'J', 'n'), 
    ('5', '10', 'J', 'n'), 
    ('6', '10', 'J', 'n'), 
    ('7', '10', 'J', 'n'), 
    ('8', '10', 'J', 'n'), 
    ('9', '10', 'J', 'n'), 
    ('10', '10', 'J', 'n'), 
    ('T', '10', 'J', 'n'), 
    ('J', '10', 'J', 'n'), 
    ('Q', '10', 'J', 'n'), 
    ('K', '10', 'J', 'n'), 
    ('A', '10', 'J', 'n'), 
    
    ('2', '10', 'Q', 'n'), 
    ('3', '10', 'Q', 'n'), 
    ('4', '10', 'Q', 'n'), 
    ('5', '10', 'Q', 'n'), 
    ('6', '10', 'Q', 'n'), 
    ('7', '10', 'Q', 'n'), 
    ('8', '10', 'Q', 'n'), 
    ('9', '10', 'Q', 'n'), 
    ('10', '10', 'Q', 'n'), 
    ('T', '10', 'Q', 'n'), 
    ('J', '10', 'Q', 'n'), 
    ('Q', '10', 'Q', 'n'), 
    ('K', '10', 'Q', 'n'), 
    ('A', '10', 'Q', 'n'), 

    ('2', '10', 'K', 'n'), 
    ('3', '10', 'K', 'n'), 
    ('4', '10', 'K', 'n'), 
    ('5', '10', 'K', 'n'), 
    ('6', '10', 'K', 'n'), 
    ('7', '10', 'K', 'n'), 
    ('8', '10', 'K', 'n'), 
    ('9', '10', 'K', 'n'), 
    ('10', '10', 'K', 'n'), 
    ('T', '10', 'K', 'n'), 
    ('J', '10', 'K', 'n'), 
    ('Q', '10', 'K', 'n'), 
    ('K', '10', 'K', 'n'), 
    ('A', '10', 'K', 'n'), 
    
    ('2', 'T', '10', 'n'), 
    ('3', 'T', '10', 'n'), 
    ('4', 'T', '10', 'n'), 
    ('5', 'T', '10', 'n'), 
    ('6', 'T', '10', 'n'), 
    ('7', 'T', '10', 'n'), 
    ('8', 'T', '10', 'n'), 
    ('9', 'T', '10', 'n'), 
    ('10', 'T', '10', 'n'), 
    ('T', 'T', '10', 'n'), 
    ('J', 'T', '10', 'n'), 
    ('Q', 'T', '10', 'n'), 
    ('K', 'T', '10', 'n'), 
    ('A', 'T', '10', 'n'), 
    
    ('2', 'T', 'J', 'n'), 
    ('3', 'T', 'J', 'n'), 
    ('4', 'T', 'J', 'n'), 
    ('5', 'T', 'J', 'n'), 
    ('6', 'T', 'J', 'n'), 
    ('7', 'T', 'J', 'n'), 
    ('8', 'T', 'J', 'n'), 
    ('9', 'T', 'J', 'n'), 
    ('10', 'T', 'J', 'n'), 
    ('T', 'T', 'J', 'n'), 
    ('J', 'T', 'J', 'n'), 
    ('Q', 'T', 'J', 'n'), 
    ('K', 'T', 'J', 'n'), 
    ('A', 'T', 'J', 'n'), 
    
    ('2', 'T', 'Q', 'n'), 
    ('3', 'T', 'Q', 'n'), 
    ('4', 'T', 'Q', 'n'), 
    ('5', 'T', 'Q', 'n'), 
    ('6', 'T', 'Q', 'n'), 
    ('7', 'T', 'Q', 'n'), 
    ('8', 'T', 'Q', 'n'), 
    ('9', 'T', 'Q', 'n'), 
    ('10', 'T', 'Q', 'n'), 
    ('T', 'T', 'Q', 'n'), 
    ('J', 'T', 'Q', 'n'), 
    ('Q', 'T', 'Q', 'n'), 
    ('K', 'T', 'Q', 'n'), 
    ('A', 'T', 'Q', 'n'), 

    ('2', 'T', 'K', 'n'), 
    ('3', 'T', 'K', 'n'), 
    ('4', 'T', 'K', 'n'), 
    ('5', 'T', 'K', 'n'), 
    ('6', 'T', 'K', 'n'), 
    ('7', 'T', 'K', 'n'), 
    ('8', 'T', 'K', 'n'), 
    ('9', 'T', 'K', 'n'), 
    ('10', 'T', 'K', 'n'), 
    ('T', 'T', 'K', 'n'), 
    ('J', 'T', 'K', 'n'), 
    ('Q', 'T', 'K', 'n'), 
    ('K', 'T', 'K', 'n'), 
    ('A', 'T', 'K', 'n'),

    ('2', 'J', '10', 'n'), 
    ('3', 'J', '10', 'n'), 
    ('4', 'J', '10', 'n'), 
    ('5', 'J', '10', 'n'), 
    ('6', 'J', '10', 'n'), 
    ('7', 'J', '10', 'n'), 
    ('8', 'J', '10', 'n'), 
    ('9', 'J', '10', 'n'), 
    ('10', 'J', '10', 'n'), 
    ('T', 'J', '10', 'n'), 
    ('J', 'J', '10', 'n'), 
    ('Q', 'J', '10', 'n'), 
    ('K', 'J', '10', 'n'), 
    ('A', 'J', '10', 'n'), 
    
    ('2', 'J', 'T', 'n'), 
    ('3', 'J', 'T', 'n'), 
    ('4', 'J', 'T', 'n'), 
    ('5', 'J', 'T', 'n'), 
    ('6', 'J', 'T', 'n'), 
    ('7', 'J', 'T', 'n'), 
    ('8', 'J', 'T', 'n'), 
    ('9', 'J', 'T', 'n'), 
    ('10', 'J', 'T', 'n'), 
    ('T', 'J', 'T', 'n'), 
    ('J', 'J', 'T', 'n'), 
    ('Q', 'J', 'T', 'n'), 
    ('K', 'J', 'T', 'n'), 
    ('A', 'J', 'T', 'n'),

    ('2', 'J', 'Q', 'n'), 
    ('3', 'J', 'Q', 'n'), 
    ('4', 'J', 'Q', 'n'), 
    ('5', 'J', 'Q', 'n'), 
    ('6', 'J', 'Q', 'n'), 
    ('7', 'J', 'Q', 'n'), 
    ('8', 'J', 'Q', 'n'), 
    ('9', 'J', 'Q', 'n'), 
    ('10', 'J', 'Q', 'n'), 
    ('T', 'J', 'Q', 'n'), 
    ('J', 'J', 'Q', 'n'), 
    ('Q', 'J', 'Q', 'n'), 
    ('K', 'J', 'Q', 'n'), 
    ('A', 'J', 'Q', 'n'), 

    ('2', 'J', 'K', 'n'), 
    ('3', 'J', 'K', 'n'), 
    ('4', 'J', 'K', 'n'), 
    ('5', 'J', 'K', 'n'), 
    ('6', 'J', 'K', 'n'), 
    ('7', 'J', 'K', 'n'), 
    ('8', 'J', 'K', 'n'), 
    ('9', 'J', 'K', 'n'), 
    ('10', 'J', 'K', 'n'), 
    ('T', 'J', 'K', 'n'), 
    ('J', 'J', 'K', 'n'), 
    ('Q', 'J', 'K', 'n'), 
    ('K', 'J', 'K', 'n'), 
    ('A', 'J', 'K', 'n'), 

    ('2', 'Q', '10', 'n'), 
    ('3', 'Q', '10', 'n'), 
    ('4', 'Q', '10', 'n'), 
    ('5', 'Q', '10', 'n'), 
    ('6', 'Q', '10', 'n'), 
    ('7', 'Q', '10', 'n'), 
    ('8', 'Q', '10', 'n'), 
    ('9', 'Q', '10', 'n'), 
    ('10', 'Q', '10', 'n'), 
    ('T', 'Q', '10', 'n'), 
    ('J', 'Q', '10', 'n'), 
    ('Q', 'Q', '10', 'n'), 
    ('K', 'Q', '10', 'n'), 
    ('A', 'Q', '10', 'n'),

    ('3', 'Q', 'T', 'n'), 
    ('2', 'Q', 'T', 'n'), 
    ('4', 'Q', 'T', 'n'), 
    ('5', 'Q', 'T', 'n'), 
    ('6', 'Q', 'T', 'n'), 
    ('7', 'Q', 'T', 'n'), 
    ('8', 'Q', 'T', 'n'), 
    ('9', 'Q', 'T', 'n'), 
    ('10', 'Q', 'T', 'n'), 
    ('T', 'Q', 'T', 'n'), 
    ('J', 'Q', 'T', 'n'), 
    ('Q', 'Q', 'T', 'n'), 
    ('K', 'Q', 'T', 'n'), 
    ('A', 'Q', 'T', 'n'),

    ('2', 'Q', 'J', 'n'), 
    ('3', 'Q', 'J', 'n'), 
    ('4', 'Q', 'J', 'n'), 
    ('5', 'Q', 'J', 'n'), 
    ('6', 'Q', 'J', 'n'), 
    ('7', 'Q', 'J', 'n'), 
    ('8', 'Q', 'J', 'n'), 
    ('9', 'Q', 'J', 'n'), 
    ('10', 'Q', 'J', 'n'), 
    ('T', 'Q', 'J', 'n'), 
    ('J', 'Q', 'J', 'n'), 
    ('Q', 'Q', 'J', 'n'), 
    ('K', 'Q', 'J', 'n'), 
    ('A', 'Q', 'J', 'n'),

    ('2', 'Q', 'K', 'n'), 
    ('3', 'Q', 'K', 'n'), 
    ('4', 'Q', 'K', 'n'), 
    ('5', 'Q', 'K', 'n'), 
    ('6', 'Q', 'K', 'n'), 
    ('7', 'Q', 'K', 'n'), 
    ('8', 'Q', 'K', 'n'), 
    ('9', 'Q', 'K', 'n'), 
    ('10', 'Q', 'K', 'n'), 
    ('T', 'Q', 'K', 'n'), 
    ('J', 'Q', 'K', 'n'), 
    ('Q', 'Q', 'K', 'n'), 
    ('K', 'Q', 'K', 'n'), 
    ('A', 'Q', 'K', 'n'), 

    ('2', 'K', '10', 'n'), 
    ('3', 'K', '10', 'n'), 
    ('4', 'K', '10', 'n'), 
    ('5', 'K', '10', 'n'), 
    ('6', 'K', '10', 'n'), 
    ('7', 'K', '10', 'n'), 
    ('8', 'K', '10', 'n'), 
    ('9', 'K', '10', 'n'), 
    ('10', 'K', '10', 'n'), 
    ('T', 'K', '10', 'n'), 
    ('J', 'K', '10', 'n'), 
    ('Q', 'K', '10', 'n'), 
    ('K', 'K', '10', 'n'), 
    ('A', 'K', '10', 'n'),

    ('2', 'K', 'T', 'n'), 
    ('3', 'K', 'T', 'n'), 
    ('4', 'K', 'T', 'n'), 
    ('5', 'K', 'T', 'n'), 
    ('6', 'K', 'T', 'n'), 
    ('7', 'K', 'T', 'n'), 
    ('8', 'K', 'T', 'n'), 
    ('9', 'K', 'T', 'n'), 
    ('10', 'K', 'T', 'n'), 
    ('T', 'K', 'T', 'n'), 
    ('J', 'K', 'T', 'n'), 
    ('Q', 'K', 'T', 'n'), 
    ('K', 'K', 'T', 'n'), 
    ('A', 'K', 'T', 'n'),
    
    ('2', 'K', 'J', 'n'), 
    ('3', 'K', 'J', 'n'), 
    ('4', 'K', 'J', 'n'), 
    ('5', 'K', 'J', 'n'), 
    ('6', 'K', 'J', 'n'), 
    ('7', 'K', 'J', 'n'), 
    ('8', 'K', 'J', 'n'), 
    ('9', 'K', 'J', 'n'), 
    ('10', 'K', 'J', 'n'), 
    ('T', 'K', 'J', 'n'), 
    ('J', 'K', 'J', 'n'), 
    ('Q', 'K', 'J', 'n'), 
    ('K', 'K', 'J', 'n'), 
    ('A', 'K', 'J', 'n'),

    ('2', 'K', 'Q', 'n'), 
    ('3', 'K', 'Q', 'n'), 
    ('4', 'K', 'Q', 'n'), 
    ('5', 'K', 'Q', 'n'), 
    ('6', 'K', 'Q', 'n'), 
    ('7', 'K', 'Q', 'n'), 
    ('8', 'K', 'Q', 'n'), 
    ('9', 'K', 'Q', 'n'), 
    ('10', 'K', 'Q', 'n'), 
    ('T', 'K', 'Q', 'n'), 
    ('J', 'K', 'Q', 'n'), 
    ('Q', 'K', 'Q', 'n'), 
    ('K', 'K', 'Q', 'n'), 
    ('A', 'K', 'Q', 'n'),
)