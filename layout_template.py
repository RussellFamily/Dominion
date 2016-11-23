# card sorting example
cardlist=[] # list of cards to use
sortedcardlist=sorted(cardlist,lambda x: (x.cost,x.name))
carddict={'card'+str(i+1):card for i,card in enumerate(sortedcardlist)}

# assign card piles in similar fashion

cardpiledict={key:CardPile(card) for (key,card) in carddict.iteritems()}

#Layout Template

# determine how to template the screen objects



# top row is always the same, still should be done dynamically

# lets store the locations in a dictionary, and assign to card piles
card_order=['copper',
            'silver',
            'gold',
            'estate',
            'duchy',
            'province',
            'curse']

for i,card in enumerate(card_order):
    currentcardpile=cardpiledict[card]
    currentcardpile.location=(5+i*74 +i*5,5)

# middle and bottom row will change
# will want to order the cards by cost (and if same, some tie breaker)
# the blit locations will be determined by this order
# this order will be determined upon initialization


for i in range(0,5):
    currentcardpile=cardpiledict['card'+str(i+1)]
    currentcardpile.location=(5+i*74 +i*5,5+118)
for i in range(5,10):
    currentcardpile=cardpiledict['card'+str(i+1)]
    currentcardpile.location=(5+i*74 +i*5,5+118*2)
