from player_settings import *

aux = False
collision_count = 0

def crash(value):
    global aux,collision_count

    if value == True and aux == False:
        aux = True
        collision_count += 1
    
    if value == False and aux == True:
        aux = False

    if collision_count >= Settings.num_vidas:
        print("GAME OVER")
        sys.exit()
