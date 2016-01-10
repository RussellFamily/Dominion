





################################
class Card():
	def __init__(self,name,info):
		self.name=name
		self.type1=info[0]
		self.type2=info[1]
		self.cost=info[2]
		self.money=info[3]
		self.points=info[4]
		self.function=info[5]
		self.imageloc="Dominion_Images/"+name+".jpg"
		self.image = pygame.image.load(self.imageloc).convert()
		self.reducedimage=pygame.transform.scale(self.image,(74,118))
################################
class Game():
	#############
	def __init__(self,cardlist):
		self.getplayers()
		self.initbasecards()
		self.initvariablecards(cardlist)
		
	#################	
	def initbasecards(self):
		copper=Card("copper",basecards["copper"])
		silver=Card("silver",basecards["silver"])
		gold=Card("gold",basecards["gold"])
		estate=Card("estate",basecards["estate"])
		duchy=Card("duchy",basecards["duchy"])
		province=Card("province",basecards["province"])
		curse=Card("curse",basecards["curse"])
		self.toprow=["copper","silver","gold","estate","duchy","province","curse"]
		self.piles={
			"copper":[copper,50],
			"silver":[silver,30],
			"gold":[gold,20],
			"estate":[estate,8],
			"duchy":[duchy,8],
			"province":[province,8],
			"curse":[curse,10]
		}
	####################
	def initvariablecards(self,cardlist):
		for card in cardlist:
			self.piles[card]=[Card(card,basecards[card]),0]
			if piles[card].type1=="Victory" or piles[card].type2=="Victory":
				self.piles[card][1]=self.victory
			else:
				self.piles[card][1]=10
				
		self.midrow=cardlist[:5]
		self.botrow=cardlist[5:]
			
		
		
		