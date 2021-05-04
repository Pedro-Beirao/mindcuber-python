#!/usr/bin/env python3

import os
import sys
import subprocess
import rubikscubetracker

arg=" "

try:
    arg = sys.argv[1]
except:
    subprocess.Popen("rubiks-cube-tracker.py --webcam 0", shell=True)

if arg == "-h":
        print("\n-----------------")
        print("-------HELP------")
        print("----------------- \n")
        print("-w : Choose a different webcam. Usage: -w 1 (default webcam is 0)")
        print("-local : See where the script are installed")
        print("-credit : Show the credits")

        print("")

elif arg== "-w":
    subprocess.Popen("rubiks-cube-tracker.py --webcam "+ sys.argv[2], shell=True)

elif arg=="-local":
    pathToRubiksCubeTracker = os.path.abspath(rubikscubetracker.__file__)[:-11]
    pathToThis = os.path.abspath(__file__)[:-8]
    print("\nColor detection script: "+pathToRubiksCubeTracker)
    print("This and the mindcuber-python.py scripts: "+ pathToThis+"\n")

elif arg=="-credit":
    print("\nCREDITS:\n\nProgram made by Pedro Beirão.\nThanks to the creators of 'ev3_dc' and 'rubiks-cube-tracker' for the amazing tools that helped me make this project.\n")