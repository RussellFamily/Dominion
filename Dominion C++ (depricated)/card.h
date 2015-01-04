//
//  card.h
//  
//
//  Created by Matthew Russell on 8/6/13.
//  Copyright (c) 2013 University of Kansas. All rights reserved.
//

#ifndef _card_h
#define _card_h
#include <string>
#include <vector>
using namespace std;


class card{
public:
    card(int numin, string namein, int costin, int pointsin, int moneyin, string typein, string subtypein, string textin);
    ~card();
    int getcost();
    int getpoints();
    int getmoney();
    string getname();
    string gettype();
    string getsubtype();
    string gettext();
    
    void doaction();
    
    
    
private:
    int num;
    int cost;
    int points;
    int money;
    string name;
    string type;
    string subtype;
    string text;
    
    
};

#endif
