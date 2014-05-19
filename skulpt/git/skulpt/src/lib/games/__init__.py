
#default
#code debug
import random

COLORS = ('trefle','pique','coeur','carreau')
RANKS = ('A','2','3','4','5','6','7','8','9','10', 'V','D','R')

class Card:
  
  def __init__(self, color, rank):    
    self.color = COLORS.index(color)
    self.rank = RANKS.index(rank)
    self.image = ( self.rank , self.color )

class Deck:
  def __init__(self, numbergames = 1):   
    self.games = numbergames
    self.card_size = (73, 98)
    self.card_center = (36.5, 49)
    self.card_back_size = (71, 96)
    self.card_back_center = (35.5, 48)
    self.cards = []

    self.shake()
  def shake(self):
    for i in range(self.games):
      for j in range(len(COLORS)):
        for k in range(len(RANKS)):
          self.cards.append([COLORS[j], RANKS[k]])
    random.shuffle(self.cards)

  def __str__(self):
    return "build card game"
  def give_card(self):
    if len(self.cards) == 0:
	  self.shake()
    choice = self.cards.pop(0)
    return Card(choice[0],choice[1]).image
