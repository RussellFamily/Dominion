import pygame as pg
import pygame.locals as pgl
from sys import exit
import dominion_cards as dc


class Game():

    def __init__(self):
        self.empytpiles = 0  # end game condition!
        # TODO: Vary Screensize and Add FullScreen
        self.screensize = (1200, 800)
        self.screen = pygame.display.set_mode(self.screensize, 0, 32)

        # TODO Determine the number of players
        self.players = self.get_players()
        self.numplayers = len(self.players)
        self.currentplayer = self.players[0]

        # Set up the card piles, and their image locations
        self.cardpiledict = self.get_card_piledict()

        # Set up draw pile
        self.drawpile = pygame.image.load(
            "Dominion_Images/card-back.jpg").convert()
        self.reduceddrawpile = pygame.transform.scale(self.drawpile, (74, 118))

        # Set up font and text
        self.my_font = pygame.font.SysFont("arial", 16)
        self.drawtext = self.my_font.render("Draw", True, (255, 255, 255))
        self.discardtext = self.my_font.render(
            "Discard", True, (255, 255, 255))

        self.playertext = None
        self.actiontext = None
        self.buytext = None
        self.phasetext = self.my_font.render(
            "Action Phase", True, (255, 255, 255))
        self.buyingpowertext = None
        self.textbox = pygame.Surface((512, 256))
        self.endgame = False
        self.nextbutton = Button(self, "End Phase")
        self.textarray = []

        # Have Players draw initial hands so they can start the game!
        for player in self.players:
            for i in range(5):
                player.drawcard()

    # here are some placeholders for variables to be used:
    self.currentplayer
    self.gamephase
    self.cardpiledict = self.get_card_piledict()

    # TODO: Dynamically get players
    def get_players(self):
        playerlist = [Player(name='Player1'), Player(name='Player2')]
        shuffle(playerlist)
        return playerlist

    # TODO: Allow Players to choose which cards will be used
    # TODO: Add in option to generate random selection of cards
    def get_card_piledict(self):
        # determine action cards
        card1 = dc.Cellar()
        card2 = dc.Festival()
        card3 = dc.Gardens()
        card4 = dc.Laboratory()
        card5 = dc.Market()
        card6 = dc.Militia()
        card7 = dc.Smithy()
        card8 = dc.ThroneRoom()
        card9 = dc.Village()
        card10 = dc.Woodcutter()
        cardlist = [card1, card2, card3, card4, card5,
                    card6, card7, card8, card9, card10]
        sortedcardlist = sorted(cardlist, lambda x: (x.cost, x.name))
        carddict = {'card' + str(i + 1): card for i,
                    card in enumerate(sortedcardlist)}

        # get predtermined cards
        setcarddict = {'copper': gc.Copper(),
                       'silver': gc.Silver(),
                       'gold': gc.Gold(),
                       'estate': gc.Estate(),
                       'duchy': gc.Duchy(),
                       'province': gc.Province(),
                       'curse': gc.Curse()}

        # append dicts
        carddict.update(setcarddict)

        # create dict of card piles
        cardpiledict = {name: CardPile(card, self.numplayers) for (
            name, card) in carddict.iteritems()}

        # determine card order of set cards
        card_order = ['copper',
                      'silver',
                      'gold',
                      'estate',
                      'duchy',
                      'province',
                      'curse']

        # for each row, set a blit location for the card piles
        # top row (set cards)
        for i, card in enumerate(card_order):
            currentcardpile = cardpiledict[card]
            currentcardpile.location = (5 + i * 74 + i * 5, 5)
        # middle row (first 5 action cards)
        for i in range(0, 5):
            currentcardpile = cardpiledict['card' + str(i + 1)]
            currentcardpile.location = (5 + i * 74 + i * 5, 5 + 118)
        # bottom row (second 5 action cards)
        for i in range(5, 10):
            currentcardpile = cardpiledict['card' + str(i + 1)]
            currentcardpile.location = (5 + i * 74 + i * 5, 5 + 118 * 2)

        return cardpiledict

    def textarrayappend(self, text):
        if len(self.textarray) > 14:
            while len(self.textarray) > 14:
                self.textarray.pop(0)
        self.textarray.append(text)

    def play_game(self):

        while self.endgame == False:
            self.playertext = self.my_font.render(
                self.currentplayer.name + "'s Turn", True, (255, 255, 255))
            self.textarrayappend(self.currentplayer.name + "'s Turn!")

            self.currentplayer.buys = 1
            self.currentplayer.actions = 1
            self.currentplayer.buyingpower = 0

            self.action_phase()

    ##################################
    # Check Events
    ##################################
    def check_for_events():
        phase = self.gamephase
        actionable_event = False
        event_queue = []
        while not actionable_event:
            self.blitscreen()
            for event in pg.event.get():
                event_result, event_location = self.event_handler(event)
                if event_location == 'endphase':
                    actionable_event = True
                    event_queue.append([event_result, event_location])
    ##################################
    # Determine the effect of an event
    ##################################

    def event_handler(event):

        # need to determine select type! action/buy,
        # hand/cardpile/deck/discard/other?

        # first, lets test if the program is quit, or if the escape key is
        # pressed
        if event.type == pgl.QUIT:
            exit()
        elif event.type == pgl.KEYDOWN:
            if event.key == pgl.K_ESCAPE:
                exit()
        # next we need to se if the ev ent button was pushed down.
        elif event.type == pgl.MOUSEBUTTONDOWN:

            # if the event is button one, multiple things may happen
            # we need to check each
            if event.button == 1:

                # now depending on what kind of card/area is clicked affects
                # what happens
                returnobject, returntype = self.check_collision(event)
                return returnobject, returntype
            # if the event is button 3, we
            elif event.button == 3:
                return None, 'None'

            elif event.button == 2:
                None, 'None'
            else:
                # wtf just happened?
                print 'MOUSE ERROR'
                return None, 'None'

    def check_collision(self, event):

        # check card piles
        for key, value in self.cardpiledict:
            testRect = Rect(value.location[0], value.location[1], 74, 118)
            if testRect.collidepoint(event.pos):
                return key, 'cardpile'

        # check cards in hand
        for card in self.currentplayer.hand:
            testRect = Rect(card.location[0], card.location[
                            1], card.width, 118)
            if testRect.collidepoint(event.pos):
                return card, 'hand'

        # check for end phase button

        # check for exit out button

        #


###############

    def action_phase(self):
        action_phase_end = False
        while not self.action_phase_end:
            for event in pygame.event.get():
                eventobject, eventtype = event_handler(event)

                # test if the endphase button was clicked
                if eventtype == 'endphase':
                    action_phase_end = True
                    break
                elif eventtype == 'hand':
                    self.currentplayer.playcard(card)

            for eventobject, event in event_queue:
                if event == 'endphase':
                    self.action_phase_end = True
                    break
                # play card
                elif event == 'hand':
                    self.currentplayer.play(card)
                    if currentplayer.actions == 0:
                        self.action_phase_end = True
                        break

    def buy_phase():
        self.buy_phase_end = False
        while not self.buy_phase_end:
            event_queue = check_for_events()

            for eventobject, event in event_queue:
                if event == 'endphase':
                    self.buy_phase_end = True
                    break
                # play card
                elif event == 'cardpile':
                    self.currentplayer.acquire(card)
                    if currentplayer.buys == 0:
                        self.buy_phase_end = True
                        break
