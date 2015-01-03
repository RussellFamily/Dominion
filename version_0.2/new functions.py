import pygame
from pygame.locals import *
from sys import exit
import cardfuncs0.2


############

def selectcards(game,n):
	done_selecting=False
	selected=0
	while not done_selecting:
		for event in pygame.event.get():
			if event.type != MOUSEBUTTONDOWN:
				testexit(event)
			else:
				if event.button ==3:
					for card in game.piles:
						
						rightclick()
				elif event.button == 1:

############

def rightclick():
	

###########

def gaincard(game, card, destination, position):
	if game.availablecardquantities[game.availablecards[card].name]>0:
		game.currentplayer.destination.insert(position, game.availablecards[card])
		game.availablecardquantities[game.availablecards[card].name]-=1
		if game.availablecardquantities[game.availablecards[card].name]==0:
			game.emptypiles+=1

	else:
		pass
		#send message to console that there aren't enough quantities available of the card
#############
def testexit(event):
	if event.type == QUIT:
		exit()
	elif event.type == KEYDOWN:
		if event.key==K_ESCAPE:
			exit()
	
#############

def actionphase():
	while True:
		for event in pygame.event.get():
			if event.type != MOUSEBUTTONDOWN:
				testexit(event)
			else:
				#test if click collides with objects in display
				pass
				
##########

def buyphase():		
		
		
		
###########		
def choosecards(rand=False):		
	list=[]
	if rand ==True:
		for i in range(10):
			list.append(random.choice(originalcardfunctions.values()))
	else:
		pass
		
	return list
		
##################
def sortlist(cardlist):
	newlist=[]
	for i in range(10)		
		newlist.append(findmin(cardlist))
	return newlist
	
####################
def findmin(cardlist):
	minval=0
	mincardindex=0
	for i in range(len(cardlist)):
		if originalcardfunctions[cardlist[i]][2]>minval:
			minval=originalcardfunctions[cardlist[i]][2]
			mincardindex=i
	card=cardlist[i]
	cardlist.pop(i)
	return card
		
		
		
		
		
		
		
		
		
		
		
		