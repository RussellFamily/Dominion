import pygame as pg
import pygame.locals as pgl
from sys import exit
import dominion_cards as dc

class Game():

	def __init__(self):
		self.empytpiles=0 # end game condition!
		#TODO: Vary Screensize and Add FullScreen
		self.screensize=(1200,800)
		self.screen=pygame.display.set_mode(self.screensize,0,32)

		#TODO Determine the number of players
		self.players=self.get_players()
		self.numplayers=len(self.players)

		self.cardpiledict=self.get_card_piledict()



	#here are some placeholders for variables to be used:
	self.currentplayer
	self.gamephase
	self.cardpiledict=self.get_card_piledict()

	#TODO: Dynamically get players
	def get_players(self):
		playerlist=[Player(name='Player1'),Player(name='Player2')]
		return playerlist

	#TODO: Allow Players to choose which cards will be used
	#TODO: Add in option to generate random selection of cards
	def get_card_piledict(self):
		#determine action cards
		card1=dc.Cellar()
		card2=dc.Festival()
		card3=dc.Gardens()
		card4=dc.Laboratory()
		card5=dc.Market()
		card6=dc.Militia()
		card7=dc.Smithy()
		card8=dc.ThroneRoom()
		card9=dc.Village()
		card10=dc.Woodcutter()
		cardlist=[card1,card2,card3,card4,card5,
				  card6,card7,card8,card9,card10]
		sortedcardlist=sorted(cardlist,lambda x: (x.cost,x.name))
		carddict={'card'+str(i+1):card for i,card in enumerate(sortedcardlist)}

		#get predtermined cards
		setcarddict={'copper':gc.Copper(),
					 'silver':gc.Silver(),
					 'gold':gc.Gold(),
					 'estate':gc.Estate(),
					 'duchy':gc.Duchy(),
					 'province':gc.Province(),
					 'curse':gc.Curse()}

		#append dicts
		carddict.update(setcarddict)

		# create dict of card piles
		cardpiledict={name:CardPile(card, self.numplayers) for (name,card) in carddict.iteritems()}

		# determine card order of set cards
		card_order=['copper',
		            'silver',
		            'gold',
		            'estate',
		            'duchy',
		            'province',
		            'curse']

		# for each row, set a blit location for the card piles
		# top row (set cards)
		for i,card in enumerate(card_order):
		    currentcardpile=cardpiledict[card]
		    currentcardpile.location=(5+i*74 +i*5,5)
		# middle row (first 5 action cards)
		for i in range(0,5):
		    currentcardpile=cardpiledict['card'+str(i+1)]
		    currentcardpile.location=(5+i*74 +i*5,5+118)
		# bottom row (second 5 action cards)
		for i in range(5,10):
		    currentcardpile=cardpiledict['card'+str(i+1)]
		    currentcardpile.location=(5+i*74 +i*5,5+118*2)

		return cardpiledict











	##################################
	# Check Events
	##################################
	def check_for_events():
		phase=self.gamephase
		actionable_event=False
		event_queue=[]
		while not actionable_event:
			self.blitscreen()
			for event in pg.event.get():
				event_result,event_location=self.event_handler(event)
				if event_location=='endphase':
					actionable_event=True
					event_queue.append([event_result,event_location])
	##################################
	# Determine the effect of an event
	##################################
	def event_handler(event,location):

		#need to determine select type! action/buy, hand/cardpile/deck/discard/other?


		#first, lets test if the program is quit, or if the escape key is pressed
		if event.type == pgl.QUIT:
			exit()
		elif event.type==pgl.KEYDOWN:
			if event.key==pgl.K_ESCAPE:
				exit()
		#next we need to se if the ev ent button was pushed down.
		elif event.type == pgl.MOUSEBUTTONDOWN:

			# if the event is button one, multiple things may happen
			# we need to check each
			if event.button == 1:

				#now depending on what kind of card/area is clicked affects what happens

				#first, check to see if its in one of the deck piles, which only matters for buy phase
				cardpile=self.check_collision(self.cardpiledict)
				if cardpile != None:
					return cardpile,'cardpile'

				#next, see if its one of the cards in the players hand
				card=self.check_collision(self.currentplayer.hand)
				if card != None and phase == 'Action':
					return card,'hand'

				# if ... :
				# #check to see if it clicked the end phase button
				# 	return None,'endphase'
			# if the event is button 3, we
			elif event.button == 3:
				pass

			elif event.button == 2:
				pass
			else:
				#wtf just happened?
				print 'MOUSE ERROR'
				pass


	def check_collision(cardlist):





###############



	def action_phase():
		self.action_phase_end=False
		while not self.action_phase_end:
			event_queue=check_for_events()

			for eventobject,event in event_queue:
				if event=='endphase':
					self.action_phase_end=True
					break
				#play card
				elif event=='hand':
					self.currentplayer.play(card)
					if currentplayer.actions==0:
						self.action_phase_end=True
						break



	def buy_phase():
		self.buy_phase_end=False
		while not self.buy_phase_end:
			event_queue=check_for_events()

			for eventobject,event in event_queue:
				if event=='endphase':
					self.buy_phase_end=True
					break
				#play card
				elif event=='cardpile':
					self.currentplayer.acquire(card)
					if currentplayer.buys==0:
						self.buy_phase_end=True
						break
