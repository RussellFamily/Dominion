//
//  deck.cpp
//  
//
//  Created by Matthew Russell on 8/7/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stdlib.h>
#include <time.h>
#include <string>
#include "deck.h"



deck::deck(int init){
    
    
    deckofcards = new vector<card*>;

    
    if (init == 1) {
        
        
    }
    
}

deck::~deck(){
    
    
}
//this shuffles the deck by finding a random card in the deck, switching it with the back, adding it to a new vector, and then removing the element from the first array
void deck::shuffle(){
    vector<card*>* shuffleddeck = new vector<card*>;
    
    card* tempcard;
    int seed = time(NULL);
    int randnum;
    while (deckofcards->size() != 0) {
        randnum=rand()%(deckofcards->size());
        tempcard=deckofcards->at(randnum);
        deckofcards->at(randnum)=deckofcards->back();
        deckofcards->back()=tempcard;
        
        shuffleddeck->push_back(tempcard);
        deckofcards->pop_back();
    }

    delete deckofcards;
    deckofcards=shuffleddeck;
    
}

void deck::addcard(card* newcard){
    deckofcards->push_back(newcard);
}


vector<card*>* deck::getdeckptr(){
    return deckofcards;
}

card* deck::getcardindeck(int i){
    return deckofcards->at(i);
}





