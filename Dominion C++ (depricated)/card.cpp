//
//  card.cpp
//  
//
//  Created by Matthew Russell on 8/7/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#include <iostream>
#include "card.h"
#include <vector>
#include <string>

card::card(int numin, string namein, int costin, int pointsin, int moneyin, string typein, string subtypein, string textin){
    cost=costin;
    points=pointsin;
    name=namein;
    type=typein;
    subtype=subtypein;
    text=textin;
    money=moneyin;
    num=numin;
    
    
}

card::~card(){
    
}

int card::getcost(){
    return cost;
}

int card::getpoints(){
    return points;
}

int card::getmoney(){
    return money;
}

string card::getname(){
    return name;
    
}

string card::gettype(){
    return type;
}

string card::getsubtype(){
    return subtype;
}

string card::gettext(){
    return text;
}

void card::doaction(){
    if (name=="Cellar") {
        ;
    } 
    else if (name=="Festival") {
        ;
    } 
    else if (name=="Gardens") {
        ;
    } 
    else if (name=="Laboratory") {
        ;
    } 
    else if (name=="Market") {
        ;
    } 
    else if (name=="Militia") {
        ;
    } 
    else if (name=="Smithy") {
        ;
    } 
    else if (name=="Throne Room") {
        ;
    } 
    else if (name=="Village") {
        ;
    } 
    else if (name=="Woodcutter") {
        ;
    } 
    else{
        ;
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}