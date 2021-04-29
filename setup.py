import os
import sys
import time
import subprocess
import rubikscubetracker
import platform

if platform.system()=="Windows":
        pathToRubiksCubeTracker = os.path.abspath(rubikscubetracker.__file__)[:-11]
        pathToThis = os.path.abspath(__file__)[:-8]

        subprocess.Popen("cd " + str(pathToRubiksCubeTracker) + " && cp " + pathToThis + "init.py " + pathToRubiksCubeTracker + "__init__.py",shell=True)
        subprocess.Popen("mkdir %homepath%/usr && mkdir %homepath%/usr/local && mkdir %homepath%/usr/local/bin ",shell=True)
        subprocess.Popen("cd %homepath%/usr/local/bin/" + " && cp " + pathToThis + "mindcuber-python.py %homepath%/usr/local/bin/mindcuber-python.py",shell=True)

        print("\n Setup Sucessful. \n \n Installed __init__.py at "+pathToRubiksCubeTracker + "\n Installed mindcuber-python at %homepath%/usr/local/bin/ \n \n rubiks-cube-tracker.py is the file that starts the program. Just run 'rubiks-cube-tracker.py --webcam 0' on the cmd")

else:
    try:
        if sys.argv[1] == "--user":
            pathToRubiksCubeTracker = os.path.abspath(rubikscubetracker.__file__)[:-11]
            pathToThis = os.path.abspath(__file__)[:-8]
            subprocess.Popen("cd " + str(pathToRubiksCubeTracker) + " && cp " + pathToThis + "init.py " + pathToRubiksCubeTracker + "__init__.py",shell=True)
            subprocess.Popen("mkdir ~/usr/ && mkdir ~/usr/local/ && mkdir ~/usr/local/bin/  ",shell=True)
            time.sleep(3)
            subprocess.Popen("cd ~/usr/local/bin/" + " && cp " + pathToThis + "rubik.py ~/usr/local/bin/rubik.py && chmod a+x rubik.py",shell=True)
            subprocess.Popen("cd ~/usr/local/bin/" + " && cp " + pathToThis + "mindcuber-python.py ~/usr/local/bin/mindcuber-python.py && chmod a+x mindcuber-python.py",shell=True)
            subprocess.Popen("export PATH=~/usr/local/bin/:$PATH",shell=True)

            print("\n Setup Sucessful (For this user only). \n \n Installed __init__.py at "+pathToRubiksCubeTracker + "\n Installed rubik.py and mindcuber-python at ~/usr/local/bin/ \n \n rubik.py is the file that starts the program. Just run 'rubik.py' on the terminal")

    except:
        pathToRubiksCubeTracker = os.path.abspath(rubikscubetracker.__file__)[:-11]
        pathToThis = os.path.abspath(__file__)[:-8]

        subprocess.Popen("cd " + str(pathToRubiksCubeTracker) + " && cp " + pathToThis + "init.py " + pathToRubiksCubeTracker + "__init__.py",shell=True)
        subprocess.Popen("cd /usr/local/bin/" + " && cp " + pathToThis + "rubik.py /usr/local/bin/rubik.py && chmod a+x rubik.py",shell=True)
        subprocess.Popen("cd /usr/local/bin/" + " && cp " + pathToThis + "mindcuber-python.py /usr/local/bin/mindcuber-python.py && chmod a+x mindcuber-python.py",shell=True)

        print("\n Setup Sucessful. \n \n Installed __init__.py at "+pathToRubiksCubeTracker + "\n Installed rubik.py and mindcuber-python at /usr/local/bin/ \n \n rubik.py is the file that starts the program. Just run 'rubik.py' on the terminal")


