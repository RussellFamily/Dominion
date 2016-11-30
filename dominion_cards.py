
import copy

#########################
######## CLASSES ########
#########################

#########################
# Player Class
#########################

# TODO write code to handle locations of cards in handle
# It should also reset these values when card is drawn
# or when they draw a whole new hand


class Player():

	def __init__(self, game, AI=False):

		self.name = "Player"
		self.discard = []
		self.hand = []
		self.inplay = []
		self.actions = 0
		self.buys = 0
		self.game = game
		self.deck = self.newdeck()
		self.shuffledeck(self.deck)
		self.xloc = 0
		self.yloc = 0
		self.buyingpower = 0
		self.nextplayer = None
		self.points = 0
		self.selected = []
		self.toselect = False
	# creates a new deck with 7 coppers and 3 estates

	def newdeck(self):
		newlist = []
		for i in range(7):
			newlist.append(self.game.cardpiledict["copper"].gaincard())
		for i in range(3):
			newlist.append(self.game.cardpiledict["estate"].gaincard())
		return newlist

	# shuffles deck
	def shuffledeck(self):
		shuffle(self.deck)

	def drawcard(self):
		if len(self.deck) == 0:
			if len(self.discard) == 0:
				return
			else:
				for card in self.discard:
					self.deck.append(card)

				self.discard = []
		i = len(self.hand)
		self.hand.append(self.deck.pop(0))

	def playcard(self, card):


#########################
# Card Pile Class
#########################


class CardPile(object):

    def __init__(self, card, numplayers):
        self.cardtype = card
        self.numcards = self.get_numcards(numplayers)
        self.location = None

    def get_numcards(self, numplayers):

		if self.cardtype.cardname == 'Estate':
			if numplayers == 2:
				return 8 + numplayers * 3
            elif numplayers == 3 or numplayers == 4:
                return 12 + numplayers * 3
            else:
                return 0 + numplayers * 3
		elif self.cardtype.type1 == 'Victory' or self.cardtype.type2 == 'Victory':
            if numplayers == 2:
                return 8
            elif numplayers == 3 or numplayers == 4:
                return 12
            else:
                return 4
		elif self.cardtype.cardname == 'Copper':
			return 50
		elif self.cardtype.cardname == 'Silver':
			return 30
		elif self.cardtype.cardname == 'Gold':
			return 20
        else:
            return 10

	def gain_card(self):
		self.numcards -= 1
		return copy.deepcopy(self.cardtype)


#########################
# Card Class
#########################

class Card(object):

	def __init__(self):
		self.name = None
		self.type1 = None
		self.type2 = None
		self.imageloc = None
		self.card_cost = 0
		self.coins = 0
		self.victory_points = 0
		self.image = None
		self.reducedimage = None
		self.location = 0
		self.width
    def

	# This function will be overwritten
	def card_function(self):
		print 'Error: Card without a Card Function has called card_function from the Card class'
		pass

	def score_card(self):
		pass

    # TODO Dynamically resize the images based on screen size
	def set_image_loc(self):
		self.imageloc=name+".jpg"
		self.image=pygame.image.load(self.imageloc).convert()
		self.reducedimage=pygame.transform.scale(self.image,(74,118))

#########################
# Default Setup Cards
#########################
class Estate(Card):

	def __init__(self):
        super(Estate,self).__init__()
		self.name='estate'
		self.type1='Victory'
		self.card_cost=2
		self.victory_points=1
		self.set_image_loc(self)

	def card_function(self):
		pass

class Duchy(Card):

	def __init__(self):
        super(Duchy,self).__init__()
		self.name='duchy'
		self.type1='Victory'
		self.card_cost=5
		self.victory_points=3
		self.set_image_loc(self)

	def card_function(self):
		pass

class Province(Card):

	def __init__(self):
        super(Province,self).__init__()
		self.name='province'
		self.type1='Victory'
		self.card_cost=8
		self.victory_points=6
		self.set_image_loc(self)

	def card_function(self):
		pass

class Copper(Card):

	def __init__(self):
        super(Copper,self).__init__()
		self.name='copper'
		self.type1='Treasure'
		self.card_cost=0
		self.coins=1
		self.set_image_loc(self)

	def card_function(self):
		pass

class Silver(Card):

	def __init__(self):
        super(Silver,self).__init__()
		self.name='silver'
		self.type1='Treasure'
		self.card_cost=3
		self.coins=2
		self.set_image_loc(self)

	def card_function(self):
		pass

class Gold(Card):

	def __init__(self):
        super(Gold,self).__init__()
		self.name='gold'
		self.type1='Treasure'
		self.card_cost=6
		self.coins=3
		self.set_image_loc(self)

	def card_function(self):
		pass


#########################
# Individual Action Card Classes
#########################

class Adventurer(Card):

	def __init__(self):
        super(Adventurer,self).__init__()
		self.name='adventurer'
		self.type1='Action'
		self.card_cost=6
		self.set_image_loc(self)

	def card_function(self):
		pass

class Bureaucrat(Card):

	def __init__(self):
        super(Bureaucrat,self).__init__()
		self.name='bureaucrat'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):


class Cellar(Card):

	def __init__(self):
        super(Cellar,self).__init__()
		self.name='cellar'
		self.type1='Action'
		self.card_cost=2
		self.set_image_loc(self)

	def card_function(self):

class Chancellor(Card):

	def __init__(self):
        super(Chancellor,self).__init__()
		self.name='chancellor'
		self.type1='Action'
		self.card_cost=3
		self.set_image_loc(self)
	def card_function(self):

class Chapel(Card):

	def __init__(self):
        super(Chapel,self).__init__()
		self.name='chapel'
		self.type1='Action'
		self.card_cost=2
		self.set_image_loc(self)
	def card_function(self):

class CouncilRoom(Card):

	def __init__(self):
        super(CouncilRoom,self).__init__()
		self.name='councilroom'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):

class Feast(Card):

	def __init__(self):
        super(Feast,self).__init__()
		self.name='feast'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Festival(Card):

	def __init__(self):
        super(Festival,self).__init__()
		self.name='festival'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):

class Garden(Card):

	def __init__(self):
        super(Garden,self).__init__()
		self.name='garden'
		self.type1='Victory'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Laboratory(Card):

	def __init__(self):
        super(Laboratory,self).__init__()
		self.name='laboratory'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):

class Library(Card):

	def __init__(self):
        super(Library,self).__init__()
		self.name='library'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):

class Market(Card):

	def __init__(self):
        super(Market,self).__init__()
		self.name='market'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):

class Militia(Card):

	def __init__(self):
        super(Militia,self).__init__()
		self.name='militia'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Mine(Card):

	def __init__(self):
        super(Mine,self).__init__()
		self.name='mine'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):

class Moat(Card):

	def __init__(self):
        super(Moat,self).__init__()
		self.name='moat'
		self.type1='Action'
		self.card_cost=2
		self.set_image_loc(self)
	def card_function(self):

class Moneylender(Card):

	def __init__(self):
        super(Moneylender,self).__init__()
		self.name='moneylender'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Remodel(Card):

	def __init__(self):
        super(Remodel,self).__init__()
		self.name='remodel'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Smithy(Card):

	def __init__(self):
        super(Smithy,self).__init__()
		self.name='smithy'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Spy(Card):

	def __init__(self):
        super(Spy,self).__init__()
		self.name='spy'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Thief(Card):

	def __init__(self):
        super(Thief,self).__init__()
		self.name='thief'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class ThroneRoom(Card):

	def __init__(self):
        super(ThroneRoom,self).__init__()
		self.name='throneroom'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Village(Card):

	def __init__(self):
        super(Village,self).__init__()
		self.name='village'
		self.type1='Action'
		self.card_cost=3
		self.set_image_loc(self)
	def card_function(self):

class Witch(Card):

	def __init__(self):
        super(Witch,self).__init__()
		self.name='witch'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):

class Woodcutter(Card):

	def __init__(self):
        super(Woodcutter,self).__init__()
		self.name='woodcutter'
		self.type1='Action'
		self.card_cost=3
		self.set_image_loc(self)
	def card_function(self):

class Workshop(Card):

	def __init__(self):
        super(Workshop,self).__init__()
		self.name='workshop'
		self.type1='Action'
		self.card_cost=3
		self.set_image_loc(self)
	def card_function(self):
