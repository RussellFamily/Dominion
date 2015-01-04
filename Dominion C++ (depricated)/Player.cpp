//
//  Player.cpp
//  
//
//  Created by Matthew Russell on 8/7/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>

#include "Player.h"

using namespace std;


Player::Player(string name){
    
    playername=name;
    playerdeck = new deck(1);
    playerhand = new vector<card*>;
    playerdiscard = new deck(0);
    cardsinplay=new vector<card*>;
    totalpoints=0;
    buyingpower=0;
    numofturns=0;
    actions=0;
    buys=0;
    
}

Player::~Player(){
    
}

void Player::draw(){
    if (playerdeck->getdeckptr()->size() !=0) {
        playerhand->push_back(playerdeck->getdeckptr()->back());
        playerdeck->getdeckptr()->pop_back();
    }
    else if(playerdiscard->getdeckptr()->size() !=0){
        
        deck* temp=playerdeck;
        playerdeck=playerdiscard;
        playerdiscard=temp;
        
        playerdeck->shuffle();
        draw();
    }
    
    
    
}


void Player::discard(int number){
    if (playerhand->size() !=0) {
        playerdiscard->getdeckptr()->push_back(playerhand->at(number));
        playerhand->erase(playerhand->begin() + number);
    }
    
    
    
}

int Player::pointsindeck(){
    for (int i=0; i<playerdeck->getdeckptr()->size(); i++) {
        totalpoints = totalpoints + playerdeck->getcardindeck(i)->getpoints();
    }
    for (int i=0; i<playerhand->size(); i++) {
        totalpoints = totalpoints + playerhand->at(i)->getpoints();
    }
    
    for (int i=0; i<playerdiscard->getdeckptr()->size(); i++) {
        totalpoints = totalpoints + playerdiscard->getcardindeck(i)->getpoints();
    }
    
}

void Player::setbuys(int num){
    buys=num;
}
void Player::setactions(int num){
    actions=num;
}

int Player::getbuys(){
    return buys;
}
int Player::getactions(){
    return actions;
}

void Player::printhand(){
    cout<<playername<<"'s HAND:"<<endl;
    cout<<"Name: \tCost: \tPoints: \tMoney: \tType: \tSubtype:"<<endl<<"Text:"<<endl;
    for (int i=0; i<playerhand->size(); i++) {
        cout<<i+1<<":";
        cout<<playerhand->at(i)->getname()<<"\t";
        cout<<playerhand->at(i)->getcost()<<"\t";
        cout<<playerhand->at(i)->getpoints()<<"\t";
        cout<<playerhand->at(i)->getmoney()<<"\t";
        cout<<playerhand->at(i)->gettype()<<"\t";
        cout<<playerhand->at(i)->getsubtype()<<endl;
        cout<<playerhand->at(i)->gettext()<<endl;
    } 
    
}

void Player::setbuyingpower(int num){
    buyingpower=num;
}

int Player::getbuyingpower(){
    return buyingpower;
}

void Player::updatenumofturns(){
    numofturns=numofturns+1;
}

int Player::getnumofturns(){
    return numofturns;
}

vector<card*>* Player::getplayerhand(){
    return playerhand;

    
}

card* Player::getcardinhand(int i){
    return playerhand->at(i);
    
    
    
    
}

