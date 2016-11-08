import pygame as pg
import pygame.locals a pgl
from sys import exit


class Game():

	#here are some placeholders for variables to be used:
	self.currentplayer
	self.gamephase
	self.cardpiledict

	##################################
	# Check Events
	##################################
	def check_for_events():
		phase=self.gamephase
		actionable_event=False]
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
		#next we need to se if the event button was pushed down.
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

				if ... :
				#check to see if it clicked the end phase button
					return None,'endphase'
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
