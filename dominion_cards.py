#########################
######## CLASSES ########
#########################
 
#########################
# Card Class
#########################

class Card(object):
	
	def __init__(self):
		self.name=None
		self.type1=None
		self.type2=None
		self.imageloc=None#+name+".jpg"
		self.function=None#allcardfunctions[name]
		self.card_cost=None
		self.coins=None
		self.victory_points=None
		self.image=None #pygame.image.load(self.imageloc).convert()
		self.reducedimage=None #pygame.transform.scale(self.image,(74,118))

	# This function will be overwritten
	def card_function(self):
		print 'Error: Card without a Card Function has called card_function from the Card class'
		pass

	def score_card(self):
		pass

	def set_image_loc(self):
		self.imageloc=name+".jpg"
		self.image=pygame.image.load(self.imageloc).convert()
		self.reducedimage=pygame.transform.scale(self.image,(74,118))

#########################
# Default Setup Cards
#########################
class Estate(Card):
	
	def __init__(self):
		self.name='estate'
		self.type1='Victory'
		self.card_cost=2
		self.victory_points=1
		self.set_image_loc(self)

	def card_function(self):
		pass

class Duchy(Card):
	
	def __init__(self):
		self.name='duchy'
		self.type1='Victory'
		self.card_cost=5
		self.victory_points=3
		self.set_image_loc(self)

	def card_function(self):
		pass

class Province(Card):
	
	def __init__(self):
		self.name='province'
		self.type1='Victory'
		self.card_cost=8
		self.victory_points=6
		self.set_image_loc(self)

	def card_function(self):
		pass

class Copper(Card):
	
	def __init__(self):
		self.name='adventurer'
		self.type1='Treasure'
		self.card_cost=0
		self.coins=1
		self.set_image_loc(self)

	def card_function(self):
		pass

class Silver(Card):
	
	def __init__(self):
		self.name='adventurer'
		self.type1='Treasure'
		self.card_cost=3
		self.coins=2
		self.set_image_loc(self)

	def card_function(self):
		pass

class Gold(Card):
	
	def __init__(self):
		self.name='adventurer'
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
		self.name='adventurer'
		self.type1='Action'
		self.card_cost=6
		self.set_image_loc(self)

	def card_function(self):
		pass

class Bureaucrat(Card):

	def __init__(self):
		self.name='bureaucrat'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):


class Cellar(Card):

	def __init__(self):
		self.name='cellar'
		self.type1='Action'
		self.card_cost=2
		self.set_image_loc(self)

	def card_function(self):

class Chancellor(Card):

	def __init__(self):
		self.name='chancellor'
		self.type1='Action'
		self.card_cost=3
		self.set_image_loc(self)
	def card_function(self):
		
class Chapel(Card):

	def __init__(self):
		self.name='chapel'
		self.type1='Action'
		self.card_cost=2
		self.set_image_loc(self)
	def card_function(self):
		
class CouncilRoom(Card):

	def __init__(self):
		self.name='councilroom'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):
		
class Feast(Card):

	def __init__(self):
		self.name='feast'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):
		
class Festival(Card):

	def __init__(self):
		self.name='festival'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):

class Garden(Card):

	def __init__(self):
		self.name='garden'
		self.type1='Victory'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):

class Laboratory(Card):

	def __init__(self):
		self.name='laboratory'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):
		
class Library(Card):

	def __init__(self):
		self.name='library'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):
		
class Market(Card):

	def __init__(self):
		self.name='market'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):
		
class Militia(Card):

	def __init__(self):
		self.name='militia'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):
		
class Mine(Card):

	def __init__(self):
		self.name='mine'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):
		
class Moat(Card):

	def __init__(self):
		self.name='moat'
		self.type1='Action'
		self.card_cost=2
		self.set_image_loc(self)
	def card_function(self):
		
class Moneylender(Card):

	def __init__(self):
		self.name='moneylender'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):
		
class Remodel(Card):

	def __init__(self):
		self.name='remodel'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):
		
class Smithy(Card):

	def __init__(self):
		self.name='smithy'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):
		
class Spy(Card):

	def __init__(self):
		self.name='spy'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):
		
class Thief(Card):

	def __init__(self):
		self.name='thief'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):
		
class ThroneRoom(Card):

	def __init__(self):
		self.name='throneroom'
		self.type1='Action'
		self.card_cost=4
		self.set_image_loc(self)
	def card_function(self):
		
class Village(Card):

	def __init__(self):
		self.name='village'
		self.type1='Action'
		self.card_cost=3
		self.set_image_loc(self)
	def card_function(self):
		
class Witch(Card):

	def __init__(self):
		self.name='witch'
		self.type1='Action'
		self.card_cost=5
		self.set_image_loc(self)
	def card_function(self):
		
class Woodcutter(Card):

	def __init__(self):
		self.name='woodcutter'
		self.type1='Action'
		self.card_cost=3
		self.set_image_loc(self)
	def card_function(self):
		
class Workshop(Card):

	def __init__(self):
		self.name='workshop'
		self.type1='Action'
		self.card_cost=3
		self.set_image_loc(self)
	def card_function(self):

		
