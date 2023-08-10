from operator import truediv
from headers import *
from board import *
from utilities import *
from barbarian import *
from walls import *
from townhall import *
from hut import *
from cannon import *
from king import *
from heal import *

import colorama
from colorama import Fore
from colorama import init

starttime = time.time()

barbsalive = []
barbsdead = []
bkalive = []
bkdead = []
nonattack_buildings = []
attack_buildings = []
wallspresent = []


g_load = 0
firstload = 0
barblimit = 0
bkflag = 0
cflag = 0
loadonce = 0
ragemoment = 0.10

os.system('clear')
init()
cursor = Cursor()
cursor.hide()

while True:
    if g_load == 0 and loadonce == 0:
        game_load()
        loadonce = 1

    if g_load == 1:
        os.system('clear')
        if time.time() - starttime >= 1.0:
            # print(bk.gethealth())
            if len(attack_buildings) != 0:
                for obj in attack_buildings:
                    if cflag == 0:
                        obj.shoot(2, gboard, barbsalive, bkalive)
                    else:
                        obj.shoot(3, gboard, barbsalive, bkalive)
            cflag = 1-cflag
            starttime = time.time()
        if bkflag == 1 and len(bkalive)==0:
            print(Fore.RED + 'BK Died x_x')

        if bkflag == 1 and len(bkalive) != 0:
            bk = bkalive[0]
            os.system('clear')
            print(Fore.GREEN + str(bk.gethealth()))
            maxhp = bk.getmaxhp()
            health = bk.gethealth()
            print(Fore.GREEN + 'bk health')
            if health/maxhp >= 0.5:
                val = round(health/maxhp * 10)
                print(Fore.GREEN + '|', end='')
                for i in range(val):
                    print(Fore.GREEN + '-', end='')
                print(Fore.GREEN + '>|')
            elif health/maxhp >= 0.2:
                val = round(health/maxhp * 10)
                print(Fore.YELLOW + '|', end='')
                for i in range(val):
                    print(Fore.YELLOW + '-', end='')
                print(Fore.YELLOW + '>|')
            elif health/maxhp > 0:
                val = round(health/maxhp * 10)
                print(Fore.RED + '|', end='')
                for i in range(val):
                    print(Fore.RED + '-', end='')
                print(Fore.RED + '>|')
            else:
                print(Fore.RED + 'bk dead x_x')
            # gboard.displayboard(0)
        for obj in barbsalive:
            x = obj.getx()
            y = obj.gety()

            targetbuilds = []
            for ob in attack_buildings:
                targetbuilds.append(ob)
            for ob in nonattack_buildings:
                if ob.getxrange() != 1 or ob.getyrange() != 1:
                    targetbuilds.append(ob)
            manhatdist = 10000000
            x_ = -1
            y_ = -1

            ff = False

            gg = False

            for ob in targetbuilds:
                xx = ob.getx()
                yy = ob.gety()
                dist = abs(x-xx)+abs(y-yy)
                if dist < manhatdist:
                    manhatdist = dist
                    x_ = xx
                    y_ = yy
                    ff = True

            state = -1
            if ff == True:
                if abs(y-y_) != 0:
                    # print('ye')
                    if y < y_:
                        # move right
                        state = 0
                        if obj.checkcollisionright(gboard):
                            gg = True
                            obj.move(x, y+1, x, y, gboard)
                    else:
                        state = 1
                        # move left
                        if obj.checkcollisionleft(gboard):
                            gg = True
                            obj.move(x, y-1, x, y, gboard)
                else:
                    if x < x_:
                        state = 2
                        # movedown
                        if obj.checkcollisiondown(gboard):
                            gg = True
                            obj.move(x+1, y, x, y, gboard)
                    else:
                        state = 3
                        # moveup
                        if obj.checkcollisionup(gboard):
                            gg = True
                            obj.move(x-1, y, x, y, gboard)

            if gg:
                continue

            hh = False
            # right
            if state == 0:
                if gboard.getcell(obj.getx(), obj.gety()+1) != 'B':
                    x = obj.getx()
                    y = obj.gety()+1
                    hh = True

            elif state == 1:
                if gboard.getcell(obj.getx(), obj.gety()-1) != 'B':
                    x = obj.getx()
                    y = obj.gety()-1
                    hh = True

            elif state == 2:
                if gboard.getcell(obj.getx()+1, obj.gety()) != 'B':
                    x = obj.getx()+1
                    y = obj.gety()
                    hh = True

            elif state == 3:
                if gboard.getcell(obj.getx()-1, obj.gety()) != 'B':
                    x = obj.getx()-1
                    y = obj.gety()
                    hh = True

            if hh == False:
                continue

            f = False
            for ob in attack_buildings:
                x_ = ob.getx()
                y_ = ob.gety()
                for i in range(x_, x_+ob.getxrange()):
                    for j in range(y_, y_+ob.getyrange()):
                        if i == x and j == y:
                            f = True

                if f == True:
                    atk = obj.getatk()
                    ob.sethp(max(0, ob.gethp()-atk))
                    new_health = ob.gethp()
                    if new_health/ob.getmaxhp() >= 0.50:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 1)
                        # gboard.displayboard(0)
                    elif new_health/ob.getmaxhp() >= 0.20:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 2)
                    elif new_health/ob.getmaxhp() > 0:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 3)
                    elif new_health == 0:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updateboard(i, j, ' ')
                                gboard.updatecolorboard(i, j, 0)
                        attack_buildings.remove(ob)
                    break

            if f == True:
                continue

            activebuildings = []
            nonactivebuildings = []
            for ob in nonattack_buildings:
                if ob.getxrange() == 1 and ob.getyrange() == 1:
                    nonactivebuildings.append(ob)
                else:
                    activebuildings.append(ob)

            g = False
            for ob in activebuildings:
                x_ = ob.getx()
                y_ = ob.gety()
                for i in range(x_, x_+ob.getxrange()):
                    for j in range(y_, y_+ob.getyrange()):
                        if i == x and j == y:
                            g = True
                if g == True:
                    atk = obj.getatk()
                    ob.sethp(max(0, ob.gethp()-atk))
                    new_health = ob.gethp()
                    if new_health/ob.getmaxhp() >= 0.50:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 1)
                        # gboard.displayboard(0)
                    elif new_health/ob.getmaxhp() >= 0.20:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 2)
                    elif new_health/ob.getmaxhp() > 0:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 3)
                    elif new_health == 0:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updateboard(i, j, ' ')
                                gboard.updatecolorboard(i, j, 0)
                        nonattack_buildings.remove(ob)
                    break

            if g == True:
                continue

            h = False
            for ob in nonactivebuildings:
                x_ = ob.getx()
                y_ = ob.gety()
                for i in range(x_, x_+ob.getxrange()):
                    for j in range(y_, y_+ob.getyrange()):
                        if i == x and j == y:
                            h = True
                if h == True:
                    atk = obj.getatk()
                    ob.sethp(max(0, ob.gethp()-atk))
                    new_health = ob.gethp()
                    if new_health/ob.getmaxhp() >= 0.50:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 1)
                        # gboard.displayboard(0)
                    elif new_health/ob.getmaxhp() >= 0.20:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 2)
                    elif new_health/ob.getmaxhp() > 0:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updatecolorboard(i, j, 3)
                    elif new_health == 0:
                        for i in range(ob.getx(), ob.getx()+ob.getxrange()):
                            for j in range(ob.gety(), ob.gety()+ob.getyrange()):
                                gboard.updateboard(i, j, ' ')
                                gboard.updatecolorboard(i, j, 0)
                        nonattack_buildings.remove(ob)
                    break
        f_done = True
        for obj in nonattack_buildings:
            if obj.getxrange() > 1 or obj.getyrange() > 1:
                f_done = False
        for obj in attack_buildings:
            f_done = False

        if f_done == True:
            os.system('aplay -q ./sounds/barb_spawn.wav&')
            game_overwin()
            cursor.show()
            quit()
        if barblimit == 10 and bkflag == 1 and len(barbsalive) == 0 and len(bkalive) == 0:
            f_done = True
        if f_done == True:
            os.system('aplay -q ./sounds/barb_spawn.wav&')
            game_overlose()
            cursor.show()
            quit()
        gboard.displayboard(0)
    inp = Input()
    _inp = inp.get_parsed_input(ragemoment)
    if(_inp != None):
        g_load = 1
        # print(_inp, end = ' ')
        if firstload == 0:
            if _inp == 'quit':
                cursor.show()
                quit()
            os.system('clear')
            for i in range(21, 29):
                wall_left = Walls(i, 91, gboard, 0, 2)
                wall_right = Walls(i, 107, gboard, 0, 2)
                wallspresent.append(wall_left)
                wallspresent.append(wall_right)
                nonattack_buildings.append(wall_left)
                nonattack_buildings.append(wall_right)
            for i in range(92, 107):
                wall_up = Walls(20, i, gboard, 1, 2)
                wall_down = Walls(28, i, gboard, 1, 2)
                wallspresent.append(wall_up)
                wallspresent.append(wall_down)
                nonattack_buildings.append(wall_up)
                nonattack_buildings.append(wall_down)
            th = TownHall(23, 98, gboard, 1)
            nonattack_buildings.append(th)

            # change to randomised later
            hut1 = Hut(19, 120, gboard, 1)
            nonattack_buildings.append(hut1)
            hut2 = Hut(11, 99, gboard, 1)
            nonattack_buildings.append(hut2)
            hut3 = Hut(6, 69, gboard, 1)
            nonattack_buildings.append(hut3)
            hut4 = Hut(30, 53, gboard, 1)
            nonattack_buildings.append(hut4)
            hut5 = Hut(40, 70, gboard, 1)
            nonattack_buildings.append(hut5)

            cannon1 = Cannon(35, 110, gboard, 1)
            attack_buildings.append(cannon1)
            cannon2 = Cannon(24, 60, gboard, 1)
            attack_buildings.append(cannon2)
            cannon3 = Cannon(10, 120, gboard, 1)
            attack_buildings.append(cannon3)
            cannon4 = Cannon(15, 80, gboard, 1)
            attack_buildings.append(cannon4)
            gboard.displayboard(0)
            firstload = 1
            continue
        os.system('clear')
        if _inp == 'AOE':
            for bk in bkalive:
                x = bk.getx()
                y = bk.gety()
                for obj in nonattack_buildings:
                    x_=obj.getx()
                    y_=obj.gety()
                    if abs(x-x_)<=5 and abs(y-y_)<=5:
                        f_na = False
                        hpdec = bk.getatk()
                        obj.sethp(max(0, obj.gethp()-hpdec))
                        new_health = obj.gethp()
                        if new_health/obj.getmaxhp() >= 0.50:
                            # print('Green ig?')
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 1)
                        elif new_health/obj.getmaxhp() >= 0.20:
                            # print('Yellow ig?')
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 2)
                        else:
                            # print('Red ig?')
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 3)
                        if new_health == 0:
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updateboard(i, j, ' ')
                                    gboard.updatecolorboard(i, j, 0)
                            nonattack_buildings.remove(obj)
                        f_na = True

                for obj in attack_buildings:
                    x_=obj.getx()
                    y_=obj.gety()
                    f_a = False
                    if abs(x-x_)<=5 and abs(y-y_)<=5:
                        hpdec = bk.getatk()
                        obj.sethp(max(0, obj.gethp()-hpdec))
                        new_health = obj.gethp()
                        if new_health/obj.getmaxhp() >= 0.50:
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 1)
                            # gboard.displayboard(0)
                        elif new_health/obj.getmaxhp() >= 0.20:
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 2)
                        elif new_health/obj.getmaxhp() > 0:
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 3)
                        elif new_health == 0:
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updateboard(i, j, ' ')
                                    gboard.updatecolorboard(i, j, 0)
                            attack_buildings.remove(obj)
                        f_a = True

        if _inp == 'rage':
            os.system('aplay -q ./sounds/rage.wav&')
            ragemoment = 0.05
            for ob in bkalive:
                atk = ob.getatk()
                ob.setatk(atk*2)
        if _inp == 'spawn1':
            if barblimit == 10:
                print(Fore.RED + 'all troops deployed!!!')
                continue
            os.system('aplay -q ./sounds/barb_spawn.wav&')
            # os.system('clear')
            print("spawning barbs at", end=' ')
            print(gboard.spawningpoint1)
            barb = Barbarian(
                gboard.spawningpoint1[0], gboard.spawningpoint1[1], gboard, 2)
            barbsalive.append(barb)
            gboard.displayboard(0)
            barblimit = barblimit+1
        if _inp == 'spawn2':
            if barblimit == 10:
                print(Fore.RED + 'all troops deployed!!!')
                continue
            os.system('aplay -q ./sounds/barb_spawn.wav&')
            # os.system('clear')
            print("spawning barbs at", end=' ')
            print(gboard.spawningpoint2)
            barb = Barbarian(
                gboard.spawningpoint2[0], gboard.spawningpoint2[1], gboard, 2)
            barbsalive.append(barb)
            gboard.displayboard(0)
            barblimit = barblimit+1
        if _inp == 'spawn3':
            if barblimit == 10:
                print(Fore.RED + 'all troops deployed!!!')
                continue
            os.system('aplay -q ./sounds/barb_spawn.wav&')
            # os.system('clear')
            print("spawning barbs at", end=' ')
            print(gboard.spawningpoint3)
            barb = Barbarian(
                gboard.spawningpoint3[0], gboard.spawningpoint3[1], gboard, 2)
            barbsalive.append(barb)
            gboard.displayboard(0)
            barblimit = barblimit+1
        if _inp == 'spawnbk1':
            if bkflag == 1:
                print(Fore.RED + 'Barbarian King already deployed!!!')
                gboard.displayboard(0)
                continue
            os.system('aplay -q ./sounds/bk_spawn.wav&')
            # os.system('clear')
            print("spawning barb King at", end=' ')
            print(gboard.spawningpoint1)
            bk = King(
                gboard.spawningpoint1[0], gboard.spawningpoint1[1], gboard, 2)
            bkalive.append(bk)
            gboard.displayboard(0)
            bkflag = bkflag | 1
        if _inp == 'spawnbk2':
            if bkflag == 1:
                print(Fore.RED + 'Barbarian King already deployed!!!')
                gboard.displayboard(0)
                continue
            os.system('aplay -q ./sounds/bk_spawn.wav&')
            # os.system('clear')
            print("spawning barb King at", end=' ')
            print(gboard.spawningpoint2)
            bk = King(
                gboard.spawningpoint2[0], gboard.spawningpoint2[1], gboard, 2)
            bkalive.append(bk)
            gboard.displayboard(0)
            bkflag = bkflag | 1
        if _inp == 'spawnbk3':
            if bkflag == 1:
                print(Fore.RED + 'Barbarian King already deployed!!!')
                gboard.displayboard(0)
                continue
            os.system('aplay -q ./sounds/bk_spawn.wav&')
            # os.system('clear')
            print("spawning barb King at", end=' ')
            print(gboard.spawningpoint3)
            bk = King(
                gboard.spawningpoint3[0], gboard.spawningpoint3[1], gboard, 2)
            bkalive.append(bk)
            gboard.displayboard(0)
            bkflag = bkflag | 1
        if _inp == 'bkright':
            # os.system('clear')
            if len(bkalive) == 0:
                print('Bk dieded')
                gboard.displayboard(0)
                continue
            bk = bkalive[0]
            if bk.checkcollisionright(gboard) == False:
                gboard.displayboard(0)
                continue
            bk.move_forward(gboard)
            bkalive[0] = bk
            gboard.displayboard(0)
        if _inp == 'bkleft':
            # os.system('clear')
            if len(bkalive) == 0:
                print('Bk dieded')
                gboard.displayboard(0)
                continue
            bk = bkalive[0]
            if bk.checkcollisionleft(gboard) == False:
                gboard.displayboard(0)
                continue
            bk.move_backward(gboard)
            bkalive[0] = bk
            gboard.displayboard(0)
        if _inp == 'bkup':
            # os.system('clear')
            if len(bkalive) == 0:
                print('Bk dieded')
                gboard.displayboard(0)
                continue
            bk = bkalive[0]
            if bk.checkcollisionup(gboard) == False:
                gboard.displayboard(0)
                continue
            bk.move_up(gboard)
            bkalive[0] = bk
            gboard.displayboard(0)
        if _inp == 'bkdown':
            # os.system('clear')
            if len(bkalive) == 0:
                print('Bk dieded')
                gboard.displayboard(0)
                continue
            bk = bkalive[0]
            if bk.checkcollisiondown(gboard) == False:
                gboard.displayboard(0)
                continue
            bk.move_down(gboard)
            bkalive[0] = bk
            gboard.displayboard(0)
        if _inp == 'space':
            # os.system('clear')
            if len(bkalive) == 0:
                print('Bk dieded')
                gboard.displayboard(0)
                continue
            bk = bkalive[0]
            if gboard.vacant(bk.getx(), bk.gety()+1):
                gboard.displayboard(0)
                continue
            else:
                f_na = False
                for obj in nonattack_buildings:
                    # print('hi')
                    y = bk.gety()+1
                    x = bk.getx()
                    # print(y)
                    # print(obj.gety())
                    if obj.gety() == y and obj.getx() <= bk.getx() and obj.getx() + obj.getxrange() - 1 >= bk.getx():
                        hpdec = bk.getatk()
                        obj.sethp(max(0, obj.gethp()-hpdec))
                        new_health = obj.gethp()
                        print(new_health)
                        if new_health/obj.getmaxhp() >= 0.50:
                            # print('Green ig?')
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 1)
                        elif new_health/obj.getmaxhp() > 0.20:
                            # print('Yellow ig?')
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 2)
                        else:
                            # print('Red ig?')
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updatecolorboard(i, j, 3)
                        if new_health == 0:
                            for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                    gboard.updateboard(i, j, ' ')
                                    gboard.updatecolorboard(i, j, 0)
                            nonattack_buildings.remove(obj)
                        f_na = True

                if f_na == False:
                    f_a = False
                    y = bk.gety()+1
                    x = bk.getx()
                    for obj in attack_buildings:
                        if obj.gety() == y and gboard.vacant(x, y) == False:
                            checkobj = False
                            x_ = obj.getx()
                            if x_ <= x and x_+obj.getxrange()-1 >= x:
                                checkobj = True
                            if checkobj == False:
                                gboard.displayboard(0)
                                continue
                            hpdec = bk.getatk()
                            obj.sethp(max(0, obj.gethp()-hpdec))
                            new_health = obj.gethp()
                            if new_health/obj.getmaxhp() >= 0.50:
                                for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                    for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                        gboard.updatecolorboard(i, j, 1)
                                # gboard.displayboard(0)
                            elif new_health/obj.getmaxhp() >= 0.20:
                                for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                    for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                        gboard.updatecolorboard(i, j, 2)
                            elif new_health/obj.getmaxhp() > 0:
                                for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                    for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                        gboard.updatecolorboard(i, j, 3)
                            elif new_health == 0:
                                for i in range(obj.getx(), obj.getx()+obj.getxrange()):
                                    for j in range(obj.gety(), obj.gety()+obj.getyrange()):
                                        gboard.updateboard(i, j, ' ')
                                        gboard.updatecolorboard(i, j, 0)
                                attack_buildings.remove(obj)
                            f_a = True
                gboard.displayboard(0)
        if _inp == 'heal':
            os.system('aplay -q ./sounds/heal.wav&')
            heal = Heal(50)
            heal.affecttroops(barbsalive, bkalive, gboard)
        if _inp == 'quit':
            cursor.show()
            quit()
        else:
            # print(_inp)
            continue
    # quit()

# Town Hall
#  _
# / \
# | |
# |_|

# Huts
#  _
# / \
# |_|

# Walls
# |

# Cannon Ball
# ●

# Cannon
#  __
# |__|
#  /\

# King
# o
# |/
# /\
