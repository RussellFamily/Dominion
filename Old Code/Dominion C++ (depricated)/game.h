//
//  gamestart.h
//  
//
//  Created by Matthew Russell on 8/6/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#ifndef _game_h
#define _game_h
#include <vector>
#include <string>

#include "Player.h"
#include "deck.h"
#include "pile.h"
#include "card.h"

using namespace std;

class game{
public:
    game();
    ~game();
    void start();
    int getplayernum();
    void printpiles();
    void findwinner();
    
private:
    int playernum;
    
    vector<Player*> playerarray;
    vector<pile*> pilearray;
    Player* currentplayer;
    int emptypiles;
    vector<Player*> winners;
    
    
};

#endif
