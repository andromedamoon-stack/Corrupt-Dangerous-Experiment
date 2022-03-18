#Creator: Sarah W (Andromedamoon)
# Ver 1.0
import sys 
import time

# time delay for text
a = 2
b = .2 # quicker delay  rate
c = 0.08 # slower delay rate

#inventory for items
inventory = ["flashlight","knife","pipe", "violin"]

class mutatedRat(object):
  enemyhealth = 45
  enemyDefense = 8
  enemyAttack = 2
  
class Player(object):
  playerHealth = 65
  playerDefense = 18
  playerAttack = 4


# classes for boss fights
class Experiment(object):
  enemyHealth = 80
  enemyDefense = 20
  enemyAttack = 8
 

class Dr_Frankenstien(object):
  enemyHealth = 64
  enemyDefense = 12
  enemyAttack = 3
  

class Igor(object):
  enemyHealth = 55
  enemyDefense = 12
  enemyAttack = 3
 

def attack():
  global enemyHealth
  global enemyAttack
  global enemyDefense
  global playerAttack
  global playerDefense
  global playerHealth
  
  playerHealth = playerHealth - enemyAttack 
  enemyHealth = enemyHealth - playerAttack
  
  if playerHealth <= 0:
    gameOver()



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
  print()
  print("Path One")
  print("""
▀█▀ █▀█ ▄▀█ █▀█ █▀▄ █▀█ █▀█ █▀█
░█░ █▀▄ █▀█ █▀▀ █▄▀ █▄█ █▄█ █▀▄""")
  print()
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
    path2()


def path1():
  print("After going down the trap door you you seem to be inside a basement")
  print()
  time.sleep(a)
  print("The halls stretch on forever, layers of dust cover the walls and floor and you can see quite a few cobwebs.")
  print()
  print()
  time.sleep(a)
  print("To your right is a supply closet.")
  print("""
█▀▀ █░█ █▀▀ █▀▀ █▄▀   ▀█▀ █░█ █▀▀   █▀█ █▀▀ █▀▀ █ █▀▀ █▀▀   █▀▀ █▀█ █▀█   ▄▀█ █▄░█ █▄█
█▄▄ █▀█ ██▄ █▄▄ █░█   ░█░ █▀█ ██▄   █▄█ █▀░ █▀░ █ █▄▄ ██▄   █▀░ █▄█ █▀▄   █▀█ █░▀█ ░█░

█▀ █░█ █▀█ █▀█ █░░ █ █▀▀ █▀ ▀█
▄█ █▄█ █▀▀ █▀▀ █▄▄ █ ██▄ ▄█ ░▄""")
  supplyCloset = input("Y/N:  ")
  if supplyCloset == 'Y' or supplyCloset == 'y':
    print()
    pathSupply()
  else:
    print()
    pathCon()

def pathSupply():
   print()
   time.sleep(a)
   print("You see a flashlight on one of the shelves.")
   print()
   time.sleep(b)
   pickup = input("Do you want to add this to your Inventory? (Y/N)  ")
   if pickup == 'y' or pickup == 'Y':
    addToInventory("flashlight")
    pathCon()
     
   else:
    print()
    time.sleep(a)
    print("You leave the flashlight on the shelf")
    pathCon()

def pathCon():
  print()
  time.sleep(a)
  print("After traversing down the basement hall for a few minutes you can see that the hallway splits off into two paths")
  print()
  time.sleep(a)
  print("You see a piece of pipe on the ground near some rubble.")
  time.sleep(a)
  pickup = input("Do you want to add this to your Inventory? (Y/N)  ")
  
  if pickup == 'y' or pickup == 'Y':
      addToInventory("pipe")
  else:
      print("You leave the pipe where it is.")

  print()
  time.sleep(a)
  print("on the left leads is another short hallway that leads to a red door.")
  time.sleep(a)
  print("On the right there is stone steps that go down a level into a dark path")
  time.sleep(a)
  print(" You can hear the sounds of running water coming from down below in the dark path")
  time.sleep(c)
  print("""
█░█░█ █░█ ▄▀█ ▀█▀   █▀█ ▄▀█ ▀█▀ █░█   █░█░█ █ █░░ █░░   █▄█ █▀█ █░█   ▀█▀ ▄▀█ █▄▀ █▀▀ ▀█
▀▄▀▄▀ █▀█ █▀█ ░█░   █▀▀ █▀█ ░█░ █▀█   ▀▄▀▄▀ █ █▄▄ █▄▄   ░█░ █▄█ █▄█   ░█░ █▀█ █░█ ██▄ ░▄""")
  path_edDark = input("Red/Dark:   ")
  if pathredDark == 'Red' or pathredDark == 'red':
    print()
    pathRed()
  else:
    print()
    pathDark()

def pathRed():
  print()
  print(" Test ")   

def pathDark():
  print()
  
  # if player does not have flashlight they cannot go down the stairs
  if "flashlight" not in inventory:
    print("The path ahead looks  dark, you can’t continue on without a light source")
    gameOver()
  else:
    print()
    time.sleep(a)
    print("When you reach the bottom of the stairs you use your flashlight to illuminate the space.")
    time.sleep(a)
    print("The space is flooded with water but you should still be able to walk through it.")
    time.sleep(a)
    print("When you shine your flashlight to the left you see  several steps above the water level to a door.")
    time.sleep(a)
    print("To you your right the water is flowing down a long dark pathway.")
    print()
    print("""
█░█░█ █░█ ▄▀█ ▀█▀   █▀█ ▄▀█ ▀█▀ █░█   █░█░█ █ █░░ █░░   █▄█ █▀█ █░█   ▀█▀ ▄▀█ █▄▀ █▀▀ ▀█
▀▄▀▄▀ █▀█ █▀█ ░█░   █▀▀ █▀█ ░█░ █▀█   ▀▄▀▄▀ █ █▄▄ █▄▄   ░█░ █▄█ █▄█   ░█░ █▀█ █░█ ██▄ ░▄""")
    answer = input("Left/ Right:   ")
    if answer == 'Left' or answer == 'left':
      print()
      left()
    else:
      print()
      right()

    
def left():
  print()
  time.sleep(a)
  print("As you step inside the room the door slams behind you. You are unable to open the door.")
  time.sleep(a)
  print("In your panic you drop your flashlight.")
  print()
  time.sleep(a)
  print("As you struggle to open the door you start to hear noises coming from behind you.")

  
def right():
  print()

def ratSewer():
  print()

def path2():
 print()

  
def hide():
 print()

def desk():
  print()

def igorBoss():
  print()

def secretDoor():
  print()
  time.sleep(a)
  print("")
  
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
  print("""######################################
           #  CAPACITY: NOT MORE THAN 3 PERSONS #
           #      BY ORDER OF: FIRE DEPT.       #
           #######################################
           """)
  print()
  time.sleep(a)
  print("Finally, you reach a landing. A door separates you from whatever lies beyond")
  print()
  library()

def library():
  print()
  time.sleep(a):
  print("When you open the door the music stops. ")
  print()
  time.sleep(a)
  print("By the light of your candle, you see a small, creepy room, filled with musty books. ")
  print()
  time.sleep(a)
  print("There is a table in the center of the floor that has  a large book, an ashtray, and a violin and bow.")
  pickup = input("Do you want to add this to your Inventory? (Y/N)  ")
    if pickup == 'Y' or pickup == 'y':
      addToInventory("violin")
      print inventory
      diary()
    else:
      print()
      print("You leave the violin on the table")
      diary()

def diary():
  print()
  diary = input("Would you like to read the book? ( Y/N)")
    if diary == 'Y' or diary == 'y':
      print('''"HOW I DID IT" BY VICTOR FRANKENSTEIN.
                ‘Whence, I often asked myself, did
                the principles of life proceed? To
                examine the causes of life... we
                must first have recourse to death."
''')
      time.sleep(a)
      print('''
            "...and as soon as the dazzling light
                      vanished, the oak tree had
                    disappeared. I knew then that
                electricity and galvanism had changed
                          my life."''')
      print()
      time.sleep(a)
      print('''When I look back now, it seems to
              me as if this almost miraculous event
                obliterated any last effort by the
                spirit of preservation to avert the
                storm that was even then hanging in
                          the stars."''')
      print()
      time.sleep(a)
      print('''"Until, from the midst of this
                darkness, a sudden light broke in
                upon me -- a light so brilliant and
                wondrous, and yet so simple!"''')
      print()
      time.sleep(a)
      print('''"
              "Change the poles from plus to minus
                and from minus to plus!"''')
      print()
      time.sleep(a)
      print("
              'I alone succeeded in discovering
              the cause of generation of life.'")
      print()
      time.sleep(a)
      print()
      print("
              'Nay, even more -- I, myself became
              capable of bestowing animation upon
              lifeless matter.'")
      print()
      time.sleep(a)
      print("
            IRREVERSIBLY COMMITTED TO THE DARK
            DESTINY OF ALL THOSE WHO BEAR THE NAME OF 'FRANKENST' NAME
            OR 'FRANKENSTEIN' 'FRONKONSTEEN.'"")

            
      castle()
            
    else:
      print()
      castle()


def castle():
  print()

  
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

  
def path3():
  print()

  
def hallwayStairs():
 print()
  
def mutatedRat():
  print()
  
def foyer():
 print() 

  
def drBoss():
  print()

  
def winSewers():
  print()
  time.sleep(a)
  print(""" After harrowing journey through the dark passage and winning against the mutated rat you finally find what looks to be a sewage tunnel that leads outside.""")
  time.sleep(b)
  print("You look behind you to see the imposing castle loom over you. You think you can see a town in the distance, possibly about a mile away")
  print()
  time.sleep(b)
  print("You escape to the town to find help")
  print()
  time.sleep(b)
  print("You've escapes from the clastle and avoided becoming a new experiment")
  print()
  time.sleep(b)
  print("Or did you really escape in time?")
  print()
  print(".......")
  playAgain()
  
def winCastle():
  print()

def winRun():
  print()
  

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
  print('''🆂🅾🅾🅽, 🅰🅻🅻 🆃🅷🅴 🅴🅻🅴🅲🆃🆁🅸🅲🅰🅻 🆂🅴🅲🆁🅴🆃🆂 🅾🅵 🅷🅴🅰🆅🅴🅽 🆂🅷🅰🅻🅻 🅱🅴 🅼🅸🅽🅴❗''')
  time.sleep(b)
  print("""
▒█▀▀█ █▀▀█ ░▀░ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █▀▀█ █░░ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀█ █▀▄▀█ ░░ 　 ▀█▀ █▀▀▀ █▀▀█ █▀▀█ █ 
▒█▄▄▀ █▄▄█ ▀█▀ ▀▀█ █▀▀ 　 ░░█░░ █▀▀█ █▀▀ 　 █░░█ █░░ █▄▄█ ░░█░░ █▀▀ █░░█ █▄▄▀ █░▀░█ ▄▄ 　 ▒█░ █░▀█ █░░█ █▄▄▀ ▀ 
▒█░▒█ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 █▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀░░ ▀▀▀▀ ▀░▀▀ ▀░░░▀ ░█ 　 ▄█▄ ▀▀▀▀ ▀▀▀▀ ▀░▀▀ ▄""")
  time.sleep(b)
  print("""
█▄█ █▀█ █░█ ▀ █░█ █▀▀   █▀▀ █▀█ ▀█▀   █ ▀█▀ ░   █▀▄▀█ ▄▀█ █▀ ▀█▀ █▀▀ █▀█ ░
░█░ █▄█ █▄█ ░ ▀▄▀ ██▄   █▄█ █▄█ ░█░   █ ░█░ █   █░▀░█ █▀█ ▄█ ░█░ ██▄ █▀▄ ▄""")
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
  print("""🅶🅴🆃 🆁🅴🅰🅳🆈❗🆃🅷🅴 🅿🅻🅰🆃🅵🅾🆁🅼 🅽🅴🅰🆁🆂 🆃🅷🅴 🅾🅿🅴🅽🅸🅽🅶.""")
  print()
  print()
  print("The platform rises through the opening and then stops. ")
  print()
  print("You see a flash of lightning")
  print(".........")
  print()
  print("Your vision goes dark")
  playAgain()


def playAgain():
  print("""
█▀▄ █▀█   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █▀█ █░░ ▄▀█ █▄█   ▄▀█ █▀▀ ▄▀█ █ █▄░█ ▀█
█▄▀ █▄█   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █▀▀ █▄▄ █▀█ ░█░   █▀█ █▄█ █▀█ █ █░▀█ ░▄""")
  answer = input("(Y/N):   ")
  if answer == 'Y' or answer == 'y':
   intro()
  else:
   print("""
█▀ █▀▀ █▀▀   █▄█ █▀█ █░█   █▄░█ █▀▀ ▀▄▀ ▀█▀   ▀█▀ █ █▀▄▀█ █▀▀
▄█ ██▄ ██▄   ░█░ █▄█ █▄█   █░▀█ ██▄ █░█ ░█░   ░█░ █ █░▀░█ ██▄""")
   sys.exit()
      



        
# adds items to inventory

def addToInventory(item):
  inventory.append(item)


def printInventory(item):




## main function ##

  print()
print()
print()
print("""
░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝
██║░░╚═╝██║░░██║██████╔╝██████╔╝██║░░░██║██████╔╝░░░██║░░░
██║░░██╗██║░░██║██╔══██╗██╔══██╗██║░░░██║██╔═══╝░░░░██║░░░
╚█████╔╝╚█████╔╝██║░░██║██║░░██║╚██████╔╝██║░░░░░░░░██║░░░
░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░░░░╚═╝░░░

██████╗░░█████╗░███╗░░██╗░██████╗░███████╗██████╗░░█████╗░██╗░░░██╗░██████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗██╔══██╗██║░░░██║██╔════╝
██║░░██║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝██║░░██║██║░░░██║╚█████╗░
██║░░██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗██║░░██║██║░░░██║░╚═══██╗
██████╔╝██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║╚█████╔╝╚██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░

███████╗██╗░░██╗██████╗░███████╗██████╗░██╗███╗░░░███╗███████╗███╗░░██╗████████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗██║████╗░████║██╔════╝████╗░██║╚══██╔══╝
█████╗░░░╚███╔╝░██████╔╝█████╗░░██████╔╝██║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══╝░░██╔══██╗██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
███████╗██╔╝╚██╗██║░░░░░███████╗██║░░██║██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░""")
print()
print()
time.sleep(a)
startGame = input("""D̒͒͐ò͝͝ y̾͘̚ö́́͋u͌́̓ d̀͊̐a̓̓͝r̒̒e͌͒̒ t͋̿͐o͛̈́͘ e͛͐̓n͒̈́̈́t̓̀͘ë́͛̕r͒͒̿?͒͋͝ (̔̔͘Y͌͝/͑̈́͌ N͐̐͝)͐̓͝""")
if startGame == 'n' or startGame == 'N':
  print("""
█▀▄▀█ ▄▀█ █▄█ █▄▄ █▀▀   █▄░█ █▀▀ ▀▄▀ ▀█▀   ▀█▀ █ █▀▄▀█ █▀▀
█░▀░█ █▀█ ░█░ █▄█ ██▄   █░▀█ ██▄ █░█ ░█░   ░█░ █ █░▀░█ ██▄""")

elif startGame == 'y' or startGame == "Y":
  intro()

