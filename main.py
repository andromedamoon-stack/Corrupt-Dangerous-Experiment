#Creator: Sarah W (Andromedamoon)
# Ver 1.0
import sys 
import time

# time delay for text
a = 2
b = .2 # quicker delay  rate
c = 0.08 # slower delay rate

#inventory for items
inventory = ["flashlight","knife","bandage","pipe","sword"]


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
  enemyHealth = 50
  enemyDefense = 12
  enemyAttack = 2
  

class Igor(object):
  enemyHealth = 50
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
    path1_pathCon()

def pathSupply():
   print()
   time.sleep(a)
   print("You see a flashlight on one of the shelves.")
   print()
   time.sleep(b)
   pickup = input("Do you want to add this to your Inventory? (Y/N)  ")
   if pickup == 'y' or pickup == 'Y':
    addToInventory("flashlight")
    path1_pathCon()
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
  print("You see a piece of pip on the ground near some rubble.")
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

  
def library():
 print()

  
def foyer():
 print() 

  
def drBoss():
  print()

  
def winSewers():
  print()

def winCastle():
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

