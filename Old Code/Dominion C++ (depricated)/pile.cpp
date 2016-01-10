//
//  pile.cpp
//  
//
//  Created by Matthew Russell on 8/8/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include "pile.h"
using namespace std;


pile::pile(card* newcard, int playernumin){
    pilecard=newcard;
    if (pilecard->gettype() == "Vict"){
        if (playernumin == 2) {
            numinpile=8;
        }
        else{
            numinpile=12;
        }
    }
    else if(pilecard->gettype() == "Curse"){
        numinpile = (playernumin - 1)*10;
    }
    else if(pilecard->getname() == "Copper"){
        numinpile = 60 - (7 * playernumin);
    }
    else if(pilecard->getname() == "Silver"){
        numinpile = 40;
    }
    else if(pilecard->getname() == "Gold"){
        numinpile= 30;
    }
    else{
        numinpile = 10;
    }
    
}

pile::~pile(){
    
}

card* pile::getpilecard(){
    return pilecard;
}

void pile::printpile(){
    
    cout<<pilecard->getname()<<"\t";
    cout<<pilecard->getcost()<<"\t";
    cout<<pilecard->getpoints()<<"\t";
    cout<<pilecard->getmoney()<<"\t";
    cout<<pilecard->gettype()<<"\t";
    cout<<pilecard->getsubtype()<<"\t";
    cout<<pilecard->gettext()<<endl;
    cout<<numinpile<<" CARDS LEFT."<<endl<<endl;
    
     
}

int pile::getnuminpile(){
    return numinpile;
}

void pile::reducenuminpile(){
    numinpile=numinpile-1;
}





