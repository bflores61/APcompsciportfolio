#Benjamin  Flores
#Race
#Tortoise And Hare Simulation Race

#Initialize
import random

# Hare has a 30% chance of falling a sleep for a turn

# If Hare is awake, it will move 1 - 10 meters at random

#Tortoise always moves a short distance between 1 - 3 meters at random

# Print the positions of the Hare and Tortoise after each round

#Functions

def race():
    global hare_wins
    global tortoise_wins
    global tortoise_pos
    global hare_pos
    global hare_asleep
    finish_line = 50 #finish line
    hare_asleep = False #hare
    tortoise_pos = 0
    hare_pos = 0
    while tortoise_pos < finish_line and hare_pos < finish_line:
        sleepy_hare()
        hare_movement()
        hare_asleep=False
        tortoise_movement()
    hare_pos=0
    tortoise_pos=0


def simulation(trials):
    global hare_wins
    global tortoise_wins
    hare_wins=0
    tortoise_wins=0
    for i in range(int(trials)):
        race()
    tortoise_wins=10000-hare_wins
    print(f"Tortoise Wins | {tortoise_wins}")
    print(f"Hare Wins | {hare_wins}")




def hare_movement():
    global hare_pos
    global finish_line
    global hare_wins
    finish_line=50
    movement=random.randint(1,10)
    if hare_asleep==True:
        hare_pos=hare_pos
    else:
        hare_pos=hare_pos+movement
        if hare_pos >= finish_line:
                hare_wins=hare_wins+1

def tortoise_movement():
    global tortoise_pos
    global finish_line
    global tortoise_wins
    finish_line=50
    walk=random.randint(1,3)
    tortoise_pos=tortoise_pos+int(walk)
    if tortoise_pos >= finish_line:
            tortoise_wins=tortoise_wins+1


def sleepy_hare():
    global hare_asleep
    sleepchance=random.randint(1,100)
    if sleepchance <= float(43):
        hare_asleep=True
    else:
        hare_asleep=False


#main
simulation(10000)
