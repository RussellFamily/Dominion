//
//  gamestart.cpp
//  
//
//  Created by Matthew Russell on 8/6/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#include <iostream>

#include <fstream>
#include <vector>
#include <string>

#include "game.h"

using namespace std;


game::game(){
    cout<<"Welcome to Dominion! How many players will there be? (choose either 2, 3 or 4)"<<endl;
    cin>>playernum;
    while (playernum<2 || playernum >4) {
        cout<<"Sorry, that is an invalid number of players. The number of valid players is 2, 3, or 4."<<endl;
        cin>>playernum;
    }
    
    emptypiles=0;
    ifstream datafile;
    datafile.open("cards.txt");
    
    
    while (!datafile.eof()) {
        
        int num;
        string name;
        int cost;
        int points;
        int money;
        string type;
        string subtype;
        string text;
        datafile>>num;
        datafile>>name;
        datafile>>cost;
        datafile>>points;
        datafile>>money;
        datafile>>type;
        datafile>>subtype;
        getline (datafile, text);

        card* newcard= new card(num,name,cost,points,money,type,subtype,text);
        pile* newpile = new pile(newcard,playernum);
        pilearray.push_back(newpile);
        newpile=NULL;
        newcard=NULL;
        
    }
    
    for (int i=0; i<playernum; i++) {
        string playername;
        cout<<"What is the name of Player "<<i+1<<"?"<<endl;
        cin>>playername;
        Player* newplayer = new Player(playername);
        for (int j=0; j<7; j++) {
            newplayer->playerdeck->addcard(pilearray[0]->getpilecard());
        }
        for (int j=0; j<3; j++) {
            newplayer->playerdeck->addcard(pilearray[3]->getpilecard());
        }
        newplayer->playerdeck->shuffle();
        for (int j=0; j<5; j++) {
            newplayer->draw();
        }
        playerarray.push_back(newplayer);
        
        
    }
    
    start();
    //after game ends
    
    findwinner();
    
    
}

game::~game(){
    
    
    
    
}


void game::start(){
    bool endofgame = false;
    int currentplayernumber=0;
    currentplayer = playerarray[currentplayernumber];
    
    int cardchoice;
    
    while (endofgame == false) {
        cout<<endl<<currentplayer->playername<< "'s TURN BEGINS!"<<endl<<endl;
        currentplayer->setactions(1);
        currentplayer->setbuys(1);
        printpiles();
        bool donewithactions = false;
        bool donewithbuys = false;
        //Action Phase
        while ((currentplayer->getactions() != 0) && (donewithactions==false)) {
            cout<<endl<<endl<<"ACTION PHASE: "<<endl<<endl;
            
            
            currentplayer->printhand();
            
            cout<<"You have "<<currentplayer->getactions()<<" actions left."<<endl;
            cout<<"Choose a card's number to play, or input 0 to choose not to play any more actions."<<endl;
            cin>>cardchoice;
            if (cardchoice == 0) {
                donewithactions=true;
            }
            else if(cardchoice <= currentplayer->getplayerhand()->size()){
                if (currentplayer->getcardinhand(cardchoice-1)->gettype() == "Action") {
                    currentplayer->getcardinhand(cardchoice-1)->doaction();
                    currentplayer->cardsinplay->push_back(currentplayer->playerhand->at(cardchoice-1));
                    currentplayer->getplayerhand()->erase(currentplayer->getplayerhand()->begin() +cardchoice -1);
                    currentplayer->setactions(currentplayer->getactions()-1);
                }
                else{
                    cout<<"That is not an action card."<<endl;
                }
                
                
            }
        }
        //Buy phase
        while (currentplayer->getbuys() != 0 && donewithbuys == false) {
            cout<<endl<<endl<<"BUY PHASE: "<<endl<<endl;
            currentplayer->printhand();
            cout<<"Putting treasure cards into play."<<endl;
            for (int i=0; i<currentplayer->playerhand->size(); i++) {
                if (currentplayer->getcardinhand(i)->gettype() == "Treas") {
                    
                    currentplayer->setbuyingpower(currentplayer->getbuyingpower() + currentplayer->getcardinhand(i)->getmoney());
                    currentplayer->cardsinplay->push_back(currentplayer->getcardinhand(i));
                    currentplayer->playerhand->erase(currentplayer->playerhand->begin() + i);
                    
                    i--;

                }       
            }
            cout<<"You have "<<currentplayer->getbuys()<<" buys left and "<<currentplayer->buyingpower<<" buying power."<<endl;
            cout<<"Choose a card's number to buy, or input 0 to choose not buy any more cards."<<endl;
            cin>>cardchoice;
            if (cardchoice == 0) {
                donewithbuys=true;
            }
            else if(cardchoice <= pilearray.size()){
                
                if (pilearray[cardchoice-1]->getnuminpile() == 0) {
                    cout<<"Cannot purchase this card: There are no copies left."<<endl;
                }
                else if (pilearray[cardchoice-1]->getpilecard()->getcost() <= currentplayer->getbuyingpower()) {

                    
                    currentplayer->playerdiscard->getdeckptr()->push_back(pilearray[cardchoice-1]->getpilecard());
                    pilearray[cardchoice-1]->reducenuminpile();
                    currentplayer->setbuys(currentplayer->getbuys()-1);
                    if (pilearray[cardchoice-1]->getnuminpile() == 0) {
                        emptypiles=emptypiles+1;
                    }
                }
                else{
                    cout<<"You don't have enough buying power to purchase that card."<<endl;
                }
                
                
            }
            else{
                cout<<"That is not a valid choice."<<endl;
            }
        }
        for (int k=0; k<currentplayer->playerhand->size(); k++) {
            currentplayer->playerdiscard->getdeckptr()->push_back(currentplayer->playerhand->at(k));
        }
        for (int k=0; k<currentplayer->cardsinplay->size(); k++) {
            currentplayer->playerdiscard->getdeckptr()->push_back(currentplayer->cardsinplay->at(k));
        }
        currentplayer->playerhand->clear();
        currentplayer->cardsinplay->clear();
        currentplayer->updatenumofturns();
        for (int k=0; k<5; k++) {
            currentplayer->draw();
        }
        currentplayer->setbuyingpower(0);
        //test end of game
        if (emptypiles >= 3 || pilearray[5]->getnuminpile() == 0) {
            endofgame=true;
        }
        
        
        currentplayernumber=(currentplayernumber+1)%playernum;
        currentplayer=playerarray[currentplayernumber];
    }
    
    
}

int game::getplayernum(){
    return playernum;
}

void game::printpiles(){
    cout<<"PILES:"<<endl;
    cout<<"NAME: \t\tCOST: \tPOINT: \tMONEY: \tTYPE: \tSUBTYPE:"<<"\tTEXT:"<<endl<<endl;
    for (int i=0; i<pilearray.size(); i++) {
        cout<<i+1<<":";
        pilearray[i]->printpile();
    } 
    
    
    
}

void game::findwinner(){
    for (int i=0; i<playerarray.size(); i++) {
        cout<<playerarray[i]->playername<<": "<<playerarray[i]->pointsindeck()<<" points."<<endl;
    }
    
    
    
}










