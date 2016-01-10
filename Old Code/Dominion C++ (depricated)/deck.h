//
//  deck.h
//  
//
//  Created by Matthew Russell on 8/7/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#ifndef _deck_h
#define _deck_h
#include <vector>
#include <string>
#include "card.h"
using namespace std;

class deck{
public:
    deck(int init);
    ~deck();
    void shuffle();
    void addcard(card* newcard);
    vector<card*>* getdeckptr();
    card* getcardindeck(int i);
    
    
    
private:
    
    vector<card*>* deckofcards;
    
    
    
};

#endif
