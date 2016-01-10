//
//  pile.h
//  
//
//  Created by Matthew Russell on 8/8/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#ifndef _pile_h
#define _pile_h
#include <vector>
#include <string>
#include "card.h"
using namespace std;

class pile{
    
public:
    pile(card* newcard, int playernumin);
    ~pile();
    card* getpilecard();
    void printpile();
    int getnuminpile();
    void reducenuminpile();
    
private:
    card* pilecard;
    int numinpile;
    
    
};

#endif
