//
//  Player.h
//  
//
//  Created by Matthew Russell on 8/7/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#ifndef _Player_h
#define _Player_h
#include <vector>
#include <string>
#include "card.h"
#include "deck.h"
#include "pile.h"


using namespace std;

class Player{
public:
    Player(string name);
    ~Player();
    void draw();
    void discard(int number);
    int pointsindeck();
    void setbuys(int num);
    void setactions(int num);
    int getbuys();
    int getactions();
    void printhand();
    void setbuyingpower(int num);
    int getbuyingpower();
    void updatenumofturns();
    int getnumofturns();
    string playername;
    vector<card*>* getplayerhand();
    card* getcardinhand(int i);
    vector<card*>* cardsinplay;
    
    deck* playerdeck;
    deck* playerdiscard;
    vector<card*>* playerhand;
    
    int totalpoints;
    int buyingpower;
    int numofturns;
    int actions;
    int buys;
    
private:
    
    
    
    
};

#endif
