import pygame
from pygame.locals import *
from sys import exit
#from cardfuncs import *
#from random import shuffle

def Adventurer(game,player):
	pass
def Bureaucrat(game,player):
	pass
def Cellar(game,player):
	player.actions+=1
def Chancellor(game,player):
	pass
def Chapel(game,player):
	pass
def CouncilRoom(game,player):
	pass
def Feast(game,player):
	pass
def Festival(game,player):
	player.actions+=2
	player.buys+=1
	player.buyingpower+=2
def Laboratory(game,player):
	player.drawcard(game)
	player.drawcard(game)
	player.actions+=1
def Library(game,player):
	pass
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
def Mine(game,player):
	pass
def Moat(game,player):
	pass
def Moneylender(game,player):
	pass
def Remodel(game,player):
	pass
def Smithy(game,player):
	for i in range(3):
		player.drawcard(game)
def Spy(game,player):
	pass
def Thief(game,player):
	pass
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
def Witch(game,player):
	pass			
			
def Woodcutter(game,player):
	player.buys+=1
	player.buyingpower+=2
	
def Workshop(game,player):
	pass	

	
cardinfo={
	"adventurer":["Action","None",6,0,0,Adventurer],
	"bureaucrat":["Action","Attack",4,0,0,Bureaucrat],
	"cellar":["Action","None",2,0,0,Cellar],
	"chancellor":["Action","None",3,0,0,Chancellor],
	"chapel":["Action","None",2,0,0,Chapel],
	"councilroom":["Action","None",5,0,0,CouncilRoom],
	"feast":["Action","None",4,0,0,Feast],
	"festival":["Action","None",5,0,0,Cellar],
	"gardens":["Victory","Garden",4,0,0,None],
	"laboratory":["Action","None",5,0,0,Laboratory],
	"library":["Action","None",5,0,0,Library],
	"market":["Action","None",5,0,0,Market],
	"militia":["Action","Attack",4,0,0,Militia],
	"mine":["Action","None",5,0,0,Mine],
	"moat":["Action","Reaction",2,0,0,Moat],
	"moneylender":["Action","None",4,0,0,Moneylender],
	"remodel":["Action","None",4,0,0,Remodel],
	"smithy":["Action","None",4,0,0,Smithy],
	"spy":["Action","Attack",4,0,0,Spy],
	"thief":["Action","Attack",4,0,0,Thief],
	"throneroom":["Action","None",4,0,0,ThroneRoom],
	"village":["Action","None",3,0,0,Village],
	"witch":["Action","Attack",5,0,0,Witch],
	"woodcutter":["Action","None",3,0,0,Woodcutter],
	"workshop":["Action","None",3,0,0,Workshop]
}	
basecards={	
	"copper":["Treasure","None",0,1,0,None],
	"silver":["Treasure","None",3,2,0,None],
	"gold":["Treasure","None",6,3,0,None],
	"estate":["Victory","None",2,0,1,None],
	"duchy":["Victory","None",5,0,3,None],
	"province":["Victory","None",8,0,3,None],
	"curse":["Curse","None",0,0,-1,None]	
}	




















