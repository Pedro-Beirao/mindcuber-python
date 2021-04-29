#!/usr/bin/env python

import ev3_dc as ev3
import time
import kociemba
#projeto kociemba https://pypi.org/project/kociemba/
import sys
import os
import subprocess
import rubikscubetracker



#cubestring that the robot will solve
kociembaStr = sys.argv[1]
print("input  "+kociembaStr)
timeItTakes = time.time()
print("solve  "+kociemba.solve(kociembaStr))
#wait time to put the cube up on the platform
time.sleep(5)

ev3device = ev3.EV3(protocol=ev3.USB, host='00:16:53:3D:F8:DF')  

rotate = ev3.Motor(ev3.PORT_A, ev3_obj=ev3device)            #big motor (arm)
turnn = ev3.Motor(ev3.PORT_A, ev3_obj=ev3device)              #big motor (platform)


def wait():
    while rotate.busy:
        pass
    time.sleep(0.1)

def waitT():
    while turnn.busy:
        pass
    time.sleep(0.1)


#holds the upper layers
def hold():     
        rotate.start_move_to(110, speed=20,brake=True)
        wait()
        rotate.start_move_to(130, speed=5,brake=True)
        wait()
        
#releases the upper layers
def release():  
        rotate.start_move_to(240, speed=20)
        wait()
        rotate.start_move_by(-230, speed=50,brake=True)
        wait()
        rotate.start_move_for(1, speed=5, direction=-1, brake=True)
        wait()

#rotates the cube using the arm
def rot(dir=1, release=0): 
        rotate.start_move_to(140, speed=20,brake=True)
        wait()
        rotate.start_move_to(105, speed=5,brake=True)
        wait()
        rotate.start_move_to(200, speed=20,brake=True)
        wait()
        if dir == 1:
            if release==0 or release==1:
                    rotate.start_move_by(-190, speed=20, brake=True)
                    wait()
                    rotate.start_move_for(1, speed=5, direction=-1, brake=True)
                    wait()
            else:
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()
                
                
        if dir == 2:
            if release==0 or release==1:
                rotate.start_move_to(200, speed=20,brake=True)
                wait()
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()
                rotate.start_move_to(200, speed=20, brake=True)
                wait()
                rotate.start_move_by(-190, speed=20, brake=True)
                wait()
                rotate.start_move_for(1, speed=5, direction=-1, brake=True)
                wait()
            else:
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()
                rotate.start_move_to(200, speed=20, brake=True)
                wait()
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()

        if dir == 3:
            if release==0 or release==1:
                rotate.start_move_to(200, speed=20,brake=True)
                wait()
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()
                rotate.start_move_to(200, speed=20, brake=True)
                wait()
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()
                rotate.start_move_to(200, speed=20, brake=True)
                wait()
                rotate.start_move_by(-190, speed=20, brake=True)
                wait()
                rotate.start_move_for(1, speed=5, direction=-1, brake=True)
                wait()
            else:
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()
                rotate.start_move_to(200, speed=20, brake=True)
                wait()
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()
                rotate.start_move_to(200, speed=20, brake=True)
                wait()
                rotate.start_move_to(110, speed=20, brake=True)
                wait()
                rotate.start_move_to(130, speed=10, brake=True)
                wait()
                


#rotates the cube using the platform
def turn(dir=1,times=1):
        
        if times==1:
                turnn.start_move_by(-310*dir, speed=60,brake=True)
                waitT()
                turnn.start_move_by(40*dir, speed=60,brake=True)
                waitT()
        if times==2:
                turnn.start_move_by(-580*dir, speed=60,brake=True)
                waitT()
                turnn.start_move_by(40*dir, speed=60,brake=True)
                waitT()
        if times==3:
                turnn.start_move_by(310*dir, speed=60,brake=True)
                waitT()
                turnn.start_move_by(-40*dir, speed=60,brake=True)
                waitT()


def R_move(timesMove=1):
        turn(-1,1)
        rot(1, -1)
        turn(1, timesMove)
        rot(3, 1)
        turn(1,1)

def L_move(timesMove=1):
        turn(1,1)
        rot(1,-1)
        turn(1,timesMove)
        rot(3, 1)
        turn(-1)

def F_move(timesMove=1):
        rot(1, -1)
        turn(1,timesMove)
        rot(3, 1)

def B_move(timesMove=1):
        turn(1,2)
        rot(1, -1)
        turn(1,timesMove)
        rot(3, 1)
        turn(1,2)

def U_move(timesMove=1):
        rot(2, -1)
        turn(1,timesMove)
        rot(2, 1)

def D_move(timesMove=1):
        hold()
        turn(1,timesMove)
        release()


#solve the cube
def solve():

        stepCount=1

        stepstr=kociemba.solve(kociembaStr)

        steps = stepstr.split()

        for step in steps:
            print("Step: "+str(stepCount) +" of "+str(len(steps))+ " - "+ step)
            stepCount+=1
            if step=="R":
                R_move(1)
            elif step=="R2":
                R_move(2)
            elif step=="R'":
                R_move(3)
            
            elif step=="L":
                L_move(1)
            elif step=="L2":
                L_move(2)
            elif step=="L'":
                L_move(3)

            elif step=="U":
                U_move(1)
            elif step=="U2":
                U_move(2)
            elif step=="U'":
                U_move(3)

            elif step=="D":
                D_move(1)
            elif step=="D2":
                D_move(2)
            elif step=="D'":
                D_move(3)

            elif step=="F":
                F_move(1)
            elif step=="F2":
                F_move(2)
            elif step=="F'":
                F_move(3)

            elif step=="B":
                B_move(1)
            elif step=="B2":
                B_move(2)
            elif step=="B'":
                B_move(3)
            
            time.sleep(0.1)


        seconds = time.time()-timeItTakes
        minutes,seconds=divmod(seconds, 60)
        print("Final time = "+ str(minutes)[0]+ " : "+ str(seconds))



solve()






