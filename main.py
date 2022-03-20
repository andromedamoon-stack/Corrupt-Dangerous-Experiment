#Creator: Sarah W (Andromedamoon)
# Ver 1.0
import sys 
import time
import random


# time delay for text
a = 2
b = .7 
c = 0.08 

#colors 
green = "\033[0;32m"
italic = "\033[3m"
white = "\033[0;37m"



# variables for attack
EnemyHP = 30
YourHP = 25
damage = 0
damaged = 0
taunt = 0
FrankenstienHP = 36


def intro():
  print()
  print("Everything is dark")
  time.sleep(a)
  print()
  print("A flash of lightning briefly illuminates the room")
  time.sleep(a)
  print()
  print("You see a light switch on the wall just a few feet in front of you. You flip the switch")
  time.sleep(a)
  print()
  print("You hear a whirl of a generator starting as the light turn on")
  print()
  time.sleep(a)
  print("There is a  body  on an operating table in the middle of the room on a platform directly below the opening in the ceiling.")
  print()
  time.sleep(a)
  print('“I’m inside a laboratory?” ')
  print()
  time.sleep(a)
  print("The face has a few stitch marks on his face. Electrodes stick out from both sides of his neck.")
  print()
  time.sleep(a)
  print("You see a trapdoor behind the platform")
  time.sleep(a)
  print("......")
  time.sleep(a)
  print("Quickly, choose a path! The doctor will be here any moment!")
  time.sleep(a)
  print()
  print("Path One")
  print("""
▀█▀ █▀█ ▄▀█ █▀█ █▀▄ █▀█ █▀█ █▀█
░█░ █▀▄ █▀█ █▀▀ █▄▀ █▄█ █▄█ █▀▄""")
  print()
  time.sleep(a)
  print("Path two")
  print("""
█░█░█ ▄▀█ █ ▀█▀   ▄▀█ █▄░█ █▀▄   █░█ █ █▀▄ █▀▀
▀▄▀▄▀ █▀█ █ ░█░   █▀█ █░▀█ █▄▀   █▀█ █ █▄▀ ██▄""")

  print()
  time.sleep(a)
  firstPath = input("What path will you choose (1/2)  ")
  if firstPath == '1':
    print()
    path1()
  elif firstPath == '2':
    print()
    hide()


def path1():
  print("After going down the trap door you you seem to be inside a basement")
  print()
  time.sleep(a)
  print("The halls stretch on forever, layers of dust cover the walls and floor and you can see quite a few cobwebs.")
  print()
  pathCon()


def pathCon():
  print()
  time.sleep(a)
  print("You find a flashlight in a dusty supply closet")
  print()
  time.sleep(a)
  print()
  time.sleep(a)
  print("You finally reach stone steps that go down a level into a dark path")
  print()
  time.sleep(a)
  print("You can hear the sounds of running water coming from down below in the dark path")
  print()
  time.sleep(a)
  print("You can either go down into the dark path and hope to find a way out or go back to the labratory and fight your way through the castle")
  print()
  time.sleep(a)
  print("You decide to go down into the dark and try your luck")
  pathDark()
  
def pathDark():
  print()
  time.sleep(a)
  print("When you reach the bottom of the stairs you use your flashlight to illuminate the space.")
  print()
  time.sleep(a)
  print("The space is flooded with water.The water is flowing down a long dark pathway. You hope it leads to a way outside and decide to walk down the flooded corridor ")
  time.sleep(a)
  print()
  print(".....")
  print()
  time.sleep(a)
  print(" You start to hear faint moaning from somewhere in front of you")
  time.sleep(a)
  print()
  print(".....")
  time.sleep(a)
  print(".....")
  print()
  print("A tall dark figure is illuminated by your flashlight")
  print()
  time.sleep(a)
  print("The man looks similar to the body you saw in the lab." )
  print()
  time.sleep(a)
  print("You find yourself frozen in fear. You expect the monster to attack you. He dosn't. Instead he talks")
  print()
  time.sleep(a)
  print("What have I done to deserve such a sentence in hell?"+ green + italic)
  print()
  time.sleep(a)
  print("Born as a demon, a ghoul from a nightmare" + green + italic)
  print()
  time.sleep(a)
  print("Yet one who still suffers and scars like a human as well" + green + italic)
  print()
  time.sleep(a)
  print("Now here I stand, a half of a man" + green + italic)
  print()
  time.sleep(a)
  print("Wondering why I draw breath!" + green + italic)
  print()
  time.sleep(b)
  print("You realize that this must have been the original creature from Victor Frankenstien's experiments. The tortured soul must have taken refuge in the basement"+ red)
  print()
  time.sleep(b)
  print("You now have two options: " + white)
  print()
  time.sleep(b)
  print("1. Console the creature and ask him for help escaping the castle. 2. Attack the monster")
  choice = input("What do you choose to do? 1/2   " + white)
  if choice == '1':
    print()
    print(" The monster guides you through the rest of the sewers until you reach an exit that leads to the outside world. " + white)
    print()
    time.sleep(a)
    print("You turn to thank him but find he has already retreated back into the saftey of the dark" + white )
    winSewers()
    
  else:
    Frankenstien()

  
def Frankenstien():
  print()
  global damage
  global YourHP
  global FrankenstienHP
  global damaged 
 

  time.sleep(a)
  print("Boss Fight!")
  print()
  time.sleep(b)
  print("Your Turn!")
  print()
  time.sleep(b)
  print(f"You: " +(str(YourHP))+"HP")
  Sleep()
  print(f"Frankenstien"+(str(FrankenstienHP))+ "HP" )
  print("(1) Attack!")
  print()
  time.sleep(b)
  print("(2) Defend!")
  print()
  time.sleep(b)
  Attack = input("What will you do?")
  if Attack == '1':
    print()
    Attacking = random.randomint(3, 5)
    Attacking = Attacking + damage
    print(reset+" You did"+(str(Attacking)) +"damage")
    FrankenstienHP = FrankenstienHP - Attacking
    time.sleep(a)
  if Attack == '2':
    print()
    print(f" You defended yourself.")
    print()
    time.sleep(b)
    print("Frankenstien's attacks do less damage now")
    damaged = damaged + random.randint(2,4)

  if FrankenstienHp <= 0:
    print()
    time.sleep(b)
    print("You beat Frankenstien!")
    winSewers()
  else:
    frankTurn()

def frankTurn():
  print()
  global damage
  global YourHP
  global FrankenstienHP
  global damaged 
  global Attacked
  print("Frankenstien's Turn!")
  Attacked = random.randint(6,10)
  Attacked = Attacked - damaged
  if Attacked  < 1:  
      Attacked = random.randint(1,4)
  print("Frankenstien did" + (str(Attacked)) +" damage")
  YourHP = YourHP - Attacked
  time.sleep(b)
  if YourHP <= 0:
    print("You lost. You are knocked uncouncious")
    gameOver()
  else:
    Frankenstien()






  
def hide():
  print()
  time.sleep(a)
  print("You quickly dash under a desk that is in a cluttered corner of the room. The clutter and desk obscure you from view as long as you don't peek your head out")
  print()
  time.sleep(a)
  print("Just a minute later you hear the doctor and another person enter the room while they talk about about drawing plans up.")
  print()
  leaveLab()


  
def leaveLab():
  print()
  time.sleep(a)
  print("You hide under the desk for what feels like hours")
  print()
  time.sleep(a)
  print("......")
  print()
  time.sleep(a)
  print(".......")
  print()
  time.sleep(a)
  print("Finally you hear the doctor exclaim 'You've caught something there. Yes! As a matter of fact I think that this might be our man!'")
  print()
  time.sleep(a)
  print(".......")
  print()
  time.sleep(a)
  print("You eventually hear them leave the lab. Now is your time to escape!")
  secretDoor()

def secretDoor():
  print()
  time.sleep(a)
  print("Quickly, try to find a way out! You notice that something about the bookcase looks odd")
  print()
  time.sleep(a)
  print("Could it possibly be a secret door?")
  print()
  time.sleep(a)
  print("You notice that there is soft music coming from somewhere")
  print()
  time.sleep(a)
  print("The music It seem to be coming from behind this bookcase. ")
  print()
  time.sleep(a)
  print("You puts your ear against the books and then feel for some hidden button or handle.")
  print()
  time.sleep(a)
  print("You see one book that seems to stand out more than the others. You take a candle from the sconce and look at it closely. ")
  print()
  time.sleep(a)
  print("It reads: SEX AND HAIR GROWTH: IT'S UP TO YOU")
  print()
  time.sleep(a)
  print("You pull the book out from the bookshelf. Beside you a small door pops open.")
  passageway()
  
def passageway():
  print()
  time.sleep(a)
  print("holding the candle above you, you  follow the music down a narrow, winding stairway.")
  print()
  time.sleep(a)
  print("The source of the gets closer and closer as you follow the light down... brushing against the cobwebbed walls.")
  print()
  time.sleep(a)
  print(" As you pass one section of wall, an ancient sign can just barely be made out in the after glow of their light.")
  print()
  print()
  print("""
           #  CAPACITY: NOT MORE THAN 3 PERSONS #
           #      BY ORDER OF: FIRE DEPT.       #
          
           """)
  print()
  time.sleep(a)
  print("Finally, you reach a landing. A door separates you from whatever lies beyond")
  print()
  library()

def library():
  print()
  time.sleep(a)
  print("When you open the door the music stops. ")
  print()
  time.sleep(a)
  print("By the light of your candle, you see a small, creepy room, filled with musty books. ")
  print()
  time.sleep(a)
  print("There is a table in the center of the floor that has  a large book, an ashtray, and a violin and bow.")
  diary()

def diary():
  print()
  diary = input("Would you like to read the book? ( Y/N)")
  if diary == 'Y' or diary == 'y':
    print('''        
                HOW I DID IT" BY VICTOR FRANKENSTEIN.
                ‘Whence, I often asked myself, did
                the principles of life proceed? To
                examine the causes of life... we
                must first have recourse to death.
'''+ bright_red)
    time.sleep(a)
    print('''
               ...and as soon as the dazzling light
                      vanished, the oak tree had
                    disappeared. I knew then that
                electricity and galvanism had changed
                          my life.''' )
    print()
    time.sleep(a)
    print('''       When I look back now, it seems to
              me as if this almost miraculous event
                obliterated any last effort by the
                spirit of preservation to avert the
                storm that was even then hanging in
                          the stars.''' )
    print()
    time.sleep(a)
    print('''        Until, from the midst of this
                darkness, a sudden light broke in
                upon me -- a light so brilliant and
                wondrous, and yet so simple! ''')
    print()
    time.sleep(a)
    print('''
              Change the poles from plus to minus
                and from minus to plus! ''')
    print()
    time.sleep(a)
    print("""
              I alone succeeded in discovering
              the cause of generation of life.""")
    print()
    time.sleep(a)
    print()
    print("""
              Nay, even more -- I, myself became
              capable of bestowing animation upon
              lifeless matter."""+ bright_red)
    print()
    time.sleep(a)
    print("""
            IRREVERSIBLY COMMITTED TO THE DARK
            DESTINY OF ALL THOSE WHO BEAR THE NAME OF 'FRANKENST' NAME
            OR 'FRANKENSTEIN' 'FRONKONSTEEN.'""" + bright_red)

            
    hallwayStairs()
  else:
    hallwayStairs()
            


  
def wait():
  print()
  print("You wait....")
  print()
  print("............")
  print()
  print("............")
  print()
  print(" You eventually wait so long that you eventually fall asleep")
  gameOver()
 
  
def hallwayStairs():
  print()
  time.sleep(a)
  print(" You step out of the secret door into a large wide hallway. You can see the forest when you look out the window and what looks to be smoke in the distance." + white)
  print()
  time.sleep(a)
  print("To your right the hallway eventually leads up to stairs that go upward. Possibly back to the lab")
  print()
  time.sleep(a)
  print("To your left the hallway has several doors and appears to strecth on before finally reaching what looks like stairs going down ")
  print()
  time.sleep(a)
  print(" You decide to go left. You walk softly to attract less attention.")
  print()
  time.sleep(a)
  print("Just as you pass the second door a middle age woman steps out of the room carrying a violin that looks suspiciously like the one from the office")
  print()
  time.sleep(a)
  print("She hasn't noticed you yet! Quick what will you do?")
  print()
  print("1. Attempt to knock her out. 2. Quickly introduce yourself and convince her you area a new assistant who got lost looking for the doctor")
  print()
  answer = input("What option will you choose? 1 or 2  ")
  if answer == '1':
    print()
    time.sleep(a)
    print("You manage to knock out the woman before she notices you. She looks to be out cold")
    print()
    time.sleep(a)
    print("You aren't sure how long she will be unconcious. You grab the candlestick and quickly head down the hallway to the stairs")
    foyer()
  else:
    print()
    time.sleep(a)
    print('"Herr Doctor? He just stepped out to town. He should be back within the hour. Did Igor send you?"')
    print()
    time.sleep(a)
    print("I believe that may have been his name, yes. You know I think I'll just wait for Herr Doctor near the front door!")
    print()
    time.sleep(a)
    print("You quickly start heading down the steps at a brisk pace. Frau Blutcher shrugs and leaves to another part of the castle unconcerned about your story or presence in the castle" )
    foyer()


def foyer():
  print() 
  time.sleep(a)
  print('Once Frau Blutcher is out of sight you break into a run down the rest of the hallway and down the stairs')
  print()
  print("When you get to the bottom of the stairs and into the foyer there is a gigantic door with a small door inside the gigantic door. Next to the door is Dr.Frankenstien inspecting several boxes" )
  time.sleep(b)
  print('"Who are you?"' )
  print()
  time.sleep(b)
  print("Who Am I? Im Fredereck Fronkonsteen" )
  print()
  time.sleep(b)
  print('"Frederick Frankenstein? Like Victor Frankenstien"' )
  print()
  time.sleep(b)
  print("Fron kon steen!")
  print()
  time.sleep(b)
  print('"Are you putting me on?"')
  print()
  time.sleep(b)
  print("No, it's pronounced Fron kon steen. It's Fredereck Fronkonsteen. Who are you? You were sent by Herr Falkstein, weren't you?" )
  answer = input("""1: Herr who? No-one sent me you crazy madman. I've seen what you do in your lab! (attack)  2:Herr Falkstein, of course! Yes he thought you might need an extra assistant   """)
  if answer == '1':
    print()
    print("Stop that! Now just stop that this instant and listen to me!" )
    drBoss()
  else:
    print()
    time.sleep(b)
    print("Wonderful. We should get you settled in. Aye-gor!…he must be farther in the castle. Let me go find him and have him bring in your luggage" )
    print()
    time.sleep(b)
    print('You leave out the front door while the doctor wanders off in search of Igor')
    outsideCastle()

def drBoss():
  print()
  global damage
  global YourHP
  global enemyHP
  global damaged 
 

  time.sleep(a)
  print("Boss Fight!")
  print()
  time.sleep(b)
  print("Your Turn!")
  print()
  time.sleep(b)
  print(f"You: " +(str(YourHP))+"HP")
  Sleep()
  print(f"Doctor's"+(str(enemyHP))+ "HP" )
  print("(1) Attack!")
  print()
  time.sleep(b)
  print("(2) Defend!")
  print()
  time.sleep(b)
  Attack = input("What will you do?")
  if Attack == '1':
    print()
    Attacking = random.randomint(3, 5)
    Attacking = Attacking + damage
    print(reset+" You did"+(str(Attacking)) +"damage")
    FrankenstienHP = FrankenstienHP - Attacking
    time.sleep(a)
  if Attack == '2':
    print()
    print(f" You defended yourself.")
    print()
    time.sleep(b)
    print("The Doctor's attacks do less damage now")
    damaged = damaged + random.randint(2,4)

  if enemynHp <= 0:
    print()
    time.sleep(b)
    print("You beat Dr.Fronkensteen!")
    winSewers()
  else:
      drTurn()

def drTurn():
  print()
  global damage
  global YourHP
  global enemyHP
  global damaged 
  global Attacked
  print("The Doctor's Turn!")
  Attacked = random.randint(6,10)
  Attacked = Attacked - damaged
  if Attacked  < 1:  
      Attacked = random.randint(1,4)
  print("The doctor did" + (str(Attacked)) +" damage")
  YourHP = YourHP - Attacked
  time.sleep(b)
  if YourHP <= 0:
    print("You lost. You are knocked uncouncious")
    gameOver()
  else:
    drBoss()
    
def outsideCastle():
  print()
  time.sleep(a)
  print('In the front courtyard you spot your small suitcase sitting near the horses.')
  print()
  time.sleep(a)
  print("How did this get here? You remember having it with you before you woke up at the lab")
  print()
  time.sleep(a)
  print("You now have two options. Choose Carefully")
  print()
  time.sleep(a)
  print("1.Take your suitcase, steal one of the nearby horses and escape.")
  print()
  time.sleep(b)
  print("2.Take your suitcase and go back inside the castle")
  end = input("What path will you take? 1/2 :  ")
  if end == '1':
    winCastle()
  else:
    winRun()
        
def winSewers():
  print()
  time.sleep(a)
  print("After harrowing journey through the lab and  dark sewers you finally find what looks to be a sewage tunnel that leads outside." + white)
  print()
  time.sleep(a)
  print("You look behind you to see the imposing castle loom over you. You think you can see a town in the distance, possibly about a mile away")
  print()
  time.sleep(a)
  print("You escape to the town to find help")
  print()
  time.sleep(a)
  print("You've escaped from the clastle and avoided becoming a new experiment!")
  print()
  print(".......")
  time.sleep(a)
  print("Or did you really escape in time?" + red)
  print()
  print("......."+ red)
  restart()
  
def winCastle():
  print()
  time.sleep(b)
  print("You take your suitcase and walk back into the castle"+ white)
  print()
  time.sleep(b)
  print("You are overwheledmed with curiosity about what really goes on in that labratory. You decide to join the doctor as a second assistant.")
  print(b)
  time.sleep(b)
  print("........")
  print()
  time.sleep(b)
  print("Several Weeks later....")
  print()
  time.sleep(b)
  print("""Fredrick, wearing a long, white surgeon's gown and surgical
mask, stands over the Body which is strapped across the chest and thighs.""" + red)
        
  print("""Fredrick has a thimble on the finger of one
hand a needle and thread in the other.""" + red)
  print()
  time.sleep(b)
  print("""The Body is on an operating table, which is in the center
of a platform directly below the opening in the ceiling.
Inga stands nearby.""" + white)
  print()
  time.sleep(b)
  print("""The doctor's face is illuminated by a crack of lightning. The dark circles under his eyes suggest that he is irreverably insane.""")
  print("You are near the switches waiting for the command to start the process. You have a similar crazed expression as Igor and the doctor. " + red)
  print()
  time.sleep(b)
  print("Go!!")
  print("........"+ white )
  print(".........")
  print()
  print()
  time.sleep(b)
  restart()

        
def winRun():
  print()
  time.sleep(b)
  print("You successfully escape from the castle with one of the horses. After several minutes of riding down the pathway ou think you can see a town in the distance, possibly about a mile away"+ white)
  print()
  time.sleep(b)
  print("You've escaped from the clastle and avoided becoming a new experiment and now see your chance to get even further away by taking a train from the town to somewhere far away from that damned castle.")
  print()
  print()
  time.sleep(b)
  print("Or did you really escape in time?" + red)
  print()
  print(".......")
  restart()

def gameOver():
  print()
  print("..........")
  print("..........")
  print('"What happened?... Where am i?"')
  print()
  print()
  print("you are now the one strapped to the operating table in the laboratory.")
  time.sleep(a)
  print("you hear the sounds of people shuffling around you and the sounds of mad laughter.")
  print()
  time.sleep(b)
  print('"Soon all the electrical secrets of heaven shall be mine!"')
  time.sleep(b)
  print('"Raise the Platform Igor!"')
  time.sleep(b)
  print("You've got it Master!")
  time.sleep(a)
  print("The platform rises higher and higher. Rain starts to pour in.")
  print()
  time.sleep(b)
  print('''𝑇ℎ𝑒 𝑎𝑛𝑐𝑖𝑒𝑛𝑡 𝑚𝑎𝑠𝑡𝑒𝑟𝑠 𝑝𝑟𝑜𝑚𝑖𝑠𝑒𝑑''')
  time.sleep(b)
  print("𝑖𝑚𝑝𝑜𝑠𝑠𝑖𝑏𝑖𝑙𝑖𝑡𝑖𝑒𝑠 𝑎𝑛𝑑 𝑝𝑒𝑟𝑓𝑜𝑟𝑚𝑒𝑑 𝑛𝑜𝑡ℎ𝑖𝑛𝑔.")
  time.sleep(b)
  print("𝑊𝑒 𝑠ℎ𝑎𝑙𝑙 𝑝𝑒𝑛𝑒𝑡𝑟𝑎𝑡𝑒 𝑖𝑛𝑡𝑜 𝑡ℎ𝑒 𝑟𝑒𝑐𝑒𝑠𝑠𝑒𝑠 𝑜𝑓 𝑛𝑎𝑡𝑢𝑟𝑒")
  time.sleep(b)
  print("𝑊𝑒 𝑠ℎ𝑎𝑙𝑙 𝑎𝑠𝑐𝑒𝑛𝑑 𝑖𝑛𝑡𝑜 𝑡ℎ𝑒 𝐻𝑒𝑎𝑣𝑒𝑛𝑠.")
  time.sleep(b)
  print("𝑊𝑒 𝑠ℎ𝑎𝑙𝑙 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑡ℎ𝑒 𝑡ℎ𝑢𝑛𝑑𝑒𝑟𝑠 𝑜𝑓 𝐻𝑒𝑎𝑣𝑒𝑛")
  time.sleep(b)
  print("𝘮𝘪𝘮𝘪𝘤 𝘵𝘩𝘦 𝘦𝘢𝘳𝘵𝘩𝘲𝘶𝘢𝘬𝘦 𝘢𝘯𝘥 𝘦𝘷𝘦𝘯 𝘮𝘰𝘤𝘬 𝘵𝘩𝘦 𝘪𝘯𝘷𝘪𝘴𝘪𝘣𝘭𝘦 𝘸𝘰𝘳𝘭𝘥 𝘸𝘪𝘵𝘩 𝘪𝘵𝘴 𝘰𝘸𝘯 𝘴𝘩𝘢𝘥𝘰𝘸𝘴!")
  print()
  print()
  print('"Get ready the platform nears the opening"')
  print()
  print()
  print("The platform rises through the opening and then stops. " + white)
  print()
  print("You see a flash of lightning")
  print(".........")
  print()
  print("Your vision goes dark")
  playAgain()


def restart():
  print("""
█▀█ █░░ ▄▀█ █▄█   ▄▀█ █▀▀ ▄▀█ █ █▄░█ ▀█
█▀▀ █▄▄ █▀█ ░█░   █▀█ █▄█ █▀█ █ █░▀█ ░▄""")
  answer = input("(Y/N):   ")
  if answer == 'Y' or answer == 'y':
   intro()
  else:
   print("""
█▀ █▀▀ █▀▀   █▄█ █▀█ █░█   █▄░█ █▀▀ ▀▄▀ ▀█▀   ▀█▀ █ █▀▄▀█ █▀▀
▄█ ██▄ ██▄   ░█░ █▄█ █▄█   █░▀█ ██▄ █░█ ░█░   ░█░ █ █░▀░█ ██▄""")
   sys.exit()
      



        


## main function ##

  print()
  print()
print()
print("""
▒█▀▀█ █▀▀█ █▀▀█ █▀▀█ █░░█ █▀▀█ ▀▀█▀▀ 　 █▀▀▄ █▀▀█ █▀▀▄ █▀▀▀ █▀▀ █▀▀█ █▀▀█ █░░█ █▀▀ 
▒█░░░ █░░█ █▄▄▀ █▄▄▀ █░░█ █░░█ ░░█░░ 　 █░░█ █▄▄█ █░░█ █░▀█ █▀▀ █▄▄▀ █░░█ █░░█ ▀▀█ 
▒█▄▄█ ▀▀▀▀ ▀░▀▀ ▀░▀▀ ░▀▀▀ █▀▀▀ ░░▀░░ 　 ▀▀▀░ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀▀ ░▀▀▀ ▀▀▀ 

█▀▀ █░█ █▀▀█ █▀▀ █▀▀█ ░▀░ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ 
█▀▀ ▄▀▄ █░░█ █▀▀ █▄▄▀ ▀█▀ █░▀░█ █▀▀ █░░█ ░░█░░ 
▀▀▀ ▀░▀ █▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░""")
print()
print()
print("""A͇͇̝ Y̟̞͜o͕͔͕u̺̙n͉̠̙g͉͚̪ F͔̫r͓̞̙a͓̪̦n͇̝͜k̻̪̺e͔̟͇n͚͔̞s͕̫͖t̠̼e̪̺̞i͓͍̟n͓̞͚ t͇͚͜e͎̪͙x̫̙̫t͕͔̦ a͉͙̠d̫̟͖v̝̼͜e̟̟̼n̪̞͜t͓͖u̪͕͜r̟̼̦e̢̠͔""")
print()
print("Be careful of the choices you make- or you might end up as the next experiment")
print()
time.sleep(b)
startGame = input("""D̒͒͐ò͝͝ y̾͘̚ö́́͋u͌́̓ d̀͊̐a̓̓͝r̒̒e͌͒̒ t͋̿͐o͛̈́͘ e͛͐̓n͒̈́̈́t̓̀͘ë́͛̕r͒͒̿?͒͋͝ (̔̔͘Y͌͝/͑̈́͌ N͐̐͝)͐̓͝"  """)
if startGame == 'n' or startGame == 'N':
  print("""
█▀▄▀█ ▄▀█ █▄█ █▄▄ █▀▀   █▄░█ █▀▀ ▀▄▀ ▀█▀   ▀█▀ █ █▀▄▀█ █▀▀
█░▀░█ █▀█ ░█░ █▄█ ██▄   █░▀█ ██▄ █░█ ░█░   ░█░ █ █░▀░█ ██▄""")

elif startGame == 'y' or startGame == "Y":
  intro()

