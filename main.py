import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Six', 'Eight', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
  
  def __init__(self,type,rank):
    self.type=type
    self.rank=rank
    self.value=values[rank]
    
  def __str__(self):
    return self.rank + " of " + self.type

class Deck:
  
  def __init__(self):
    self.all_cards=[]
    for suit in suits:
      for rank in ranks:
        
        createdCard=Card(suit,rank)
        self.all_cards.append(createdCard)

  def shuffleDeck(self):
    random.shuffle(self.all_cards)
    
  def deal_one(self):
    return self.all_cards.pop()

class Player:
  
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
    self.all_cards=[]

  def removeOne(self):
    return self.all_cards.pop(0)

  def addCard(self,new_cards):
    
    if type(new_cards) == type([]):
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)

  def placeBet(self):
    
    while True:
      bet = int(input("Please place your bet: "))
      if bet>self.balance:
        print(f"Unable to place bet, current Balance is: {self.balance} and bet amount is {bet}")
      elif bet<=0:
        print("Bet must be higher than 0")
      else:
        self.balance=self.balance-bet
        return bet
        
  def updateBalance(self,bet):
      self.balance=self.balance+(bet*2)
      
  def checkSum(self,aceSum):
    sum=0
    for x in range(len(self.all_cards)):
     sum=sum+self.all_cards[x].value
    print(f"Player {self.name} currently has a total sum of {sum-aceSum} from their {len(self.all_cards)} cards\n")
    return sum-aceSum

  def containsAce(self):
    aceCounter=0
    for x in range(len(self.all_cards)):
     if(self.all_cards[x].rank=="Ace"):
       aceCounter+=1
       
    return aceCounter

  def isAce(self,i):
    if self.all_cards[i].rank=="Ace":
      return True
    else:
      return False
    

class ComputerDealer:
  
  def __init__(self,name,casinoBalance):
    self.name=name
    self.casinoBalance=casinoBalance
    self.all_cards=[]

  def addCard(self,new_card):
    self.all_cards.append(new_card)

  def updateBalance(self,status,bet):
    if status=="lost":
      self.casinoBalance=self.casinoBalance-(bet*2)
    else:
      self.casinoBalance=self.casinoBalance+bet
  
  def getInfo(self):
    print(f"**Computer currently has a {self.all_cards[0]} which sums {self.all_cards[0].value}\n**")

  def checkSum(self):
    sum=0
    for x in range(len(self.all_cards)):
     sum=sum+self.all_cards[x].value
      
    return sum
   

#MAIN
#Game Set-Up

gameDeck = Deck()
gameDeck.shuffleDeck()

player = Player("Pablo", 100000)
computer = ComputerDealer("Alexa", 500000)

#Delivering the first two cards to the Player and the Computer. Can be done with a for loop as player size increases
player.addCard(gameDeck.deal_one())
player.addCard(gameDeck.deal_one())
computer.addCard(gameDeck.deal_one())
computer.addCard(gameDeck.deal_one())

game = True
game_on= True
playerSum=0
computerSum=0
playerAce=False
aceSum=0
i=1;
aceSumChange = False
isAce = False

while game:
  
  
  print("Welcome to BlackJack. May the Odds be with You\n")
  print("Remember that Aces can either count as a 1 or 11. Whichever favours you")
  
  print(f"--Hello my name is {computer.name} and I will be your dealer--")
  bet = player.placeBet()
  print(f"Current bet is {bet}. The game will now start\n")
  print("** Initial Dealing in Progress**")
  print(f"{player.name} has started with: ")
  print(player.all_cards[0]) 
  print(player.all_cards[1])
  
  playerSum = player.checkSum(aceSum)
  playerAce = player.containsAce()
  a=playerAce

  if(a==2):
    a-=1
    aceSum=10
    print("DoubleAce")
    print(f"Due to having an Ace. Its value will be automatically reduced to the value of 1 to avoid a Bust ** New sum: {playerSum}**\n")

  if(playerSum==21):
    print(f"{player.name} has Won the game. {bet*2} has been added to your balance")
    player.updateBalance(bet)
    computer.updateBalance("lost",bet*2)
    
  if(playerSum>21):
     print(f"{player.name} has Lost the game. {bet} have been reduced from your balance")
     computer.updateBalance("won",bet)
    
  
  computerStum = computer.checkSum()
  computer.getInfo()
  #Possible to win with only two cards LOGIC
  ##
  while game_on:
    choice = input("If you wish to hit, type h - If you wish to Stand, type s \n")

    if choice=="h":
      i+=1
      player.addCard(gameDeck.deal_one())
      print(f"{player.name} has received a {player.all_cards[i]}")
      isAce = player.isAce(i)
      if isAce:
        a+=1
        
      playerSum=player.checkSum(aceSum) 
      playerAce = player.containsAce()
      

      if playerSum>21 and playerAce>0 and aceSumChange==False: 
        playerSum = playerSum-10  
        aceSum = aceSum+10
        a-=a
        if a==0:
          aceSumChange=True
        
        print(f"Due to having an Ace. Its value will be automatically reduced to the value of 1 to avoid a Bust ** New sum: {playerSum}**\n")
    
      if playerSum==21: 
        print(f"{player.name} has Won the game. {bet*2} has been added to your balance")
        player.updateBalance(bet)
        computer.updateBalance("lost",bet*2)
        break;
      
      if playerSum>21 :
        print(f"{player.name} has Lost the game. {bet} have been reduced from your balance")
        computer.updateBalance("won",bet)
        break;

    if choice=="s":
      

      
        

    

  

  

  
  
  

  



  
  
  








    
    

  
    
  

    
  
    

  