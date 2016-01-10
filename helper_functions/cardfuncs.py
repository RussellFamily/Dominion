import pygame
from pygame.locals import *
from sys import exit
#from cardfuncs import *
#from random import shuffle


def Cellar(game,player):
	player.actions+=1
def Festival(game,player):
	player.actions+=2
	player.buys+=1
	player.buyingpower+=2
def Gardens(game,player):
	pass
def Laboratory(game,player):
	player.drawcard(game)
	player.drawcard(game)
	player.actions+=1
def Market(game,player):
	player.drawcard(game)
	player.buys+=1
	player.buyingpower+=1
	player.actions+=1
def Militia(game,player):
	player.buyingpower+=2
	for opponent in game.players:
		if opponent==player:
			pass
		else:
			done=False
			doneblock=pygame.Surface((80,20))
			textimage=game.my_font.render("Done",True,(0,0,0))
			
			game.currentplayer=opponent
			opponent.toselect=True
			game.textarrayappend(opponent.name + " discard down to 3 cards.")
			for i in range(len(opponent.hand)):
				
				opponent.selected.append(False)
			while not done:
				
				
				for event in pygame.event.get():
					if event.type==QUIT:
						exit()
					elif event.type==KEYDOWN:
						if event.key==K_ESCAPE:
							exit()
					elif event.type==MOUSEBUTTONDOWN:
						for i in range(len(opponent.hand)):
							testRect=Rect(5+i*74+i*5,680,74,118)
							if testRect.collidepoint(event.pos):
								if opponent.selected[i]==False:
									opponent.selected[i]=True
									break
								elif opponent.selected[i]==True:
									opponent.selected[i]=False
									break
						if Rect(1000,450,80,20).collidepoint(event.pos):
							nonselected=0
							for i in range(len(opponent.hand)):
								if opponent.selected[i]==False:
									nonselected+=1
							if nonselected != 3:
								pass
							else:
								done=True
				
				
				
				
				
				game.blitscreen(True)
				doneblock.fill((255,0,0))
				doneblock.blit(textimage,(6,3))
				game.screen.blit(doneblock,(1000,450))
				
				
				pygame.display.update()
			temphand=[]	
			for i in range(len(opponent.hand)):
				if opponent.selected[i]==False:
					temphand.append(opponent.hand[i])
				else:
					opponent.discard.append(opponent.hand[i])
			opponent.selected=[]
			opponent.toselect=False
			
			opponent.hand=temphand
			game.currentplayer=player	
def Smithy(game,player):
	for i in range(3):
		player.drawcard(game)
	
def ThroneRoom(game,player):
	actionsleft=False
	for card in player.hand:
		if card.type1=="Action":
			actionsleft=True
			break
	if actionsleft==True:
		pass
			
	
def Village(game,player):
	player.actions+=2
	player.drawcard(game)
	
def Woodcutter(game,player):
	player.buys+=1
	player.buyingpower+=2
	
	

	
allcardfunctions={
	"cellar":Cellar,
	"festival":Festival,
	"gardens":Gardens,
	"laboratory":Laboratory,
	"market":Market,
	"militia":Militia,
	"smithy":Smithy,
	"throneroom":ThroneRoom,
	"village":Village,
	"woodcutter":Woodcutter,
	"copper":None,
	"silver":None,
	"gold":None,
	"estate":None,
	"duchy":None,
	"province":None,
	"curse":None
	
}	



