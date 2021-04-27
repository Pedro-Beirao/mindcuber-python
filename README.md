# mindcuber-python
A program that solves a Rubik's cube with a ev3 Mindstorms, without needing a SD card.

You need to build the mindcuber robot. The "MindCub3r-v1p0.pdf" file has the building instructions (You can also find them  at https://www.mindcuber.com).

This program uses a library called "ev3-dc" (https://pypi.org/project/ev3-dc/) and uses Kociemba (https://pypi.org/project/kociemba/).

```
pip install ev3-dc
pip install kociemba
```

The motor of the arm should connect to the A Port.
The motor of the platform should connect to the B Port.

To run the program:
```
$ python3 mindcuber-python CUBESTRING
```

See https://pypi.org/project/kociemba/ to understand what a Cubestring is

Instead of using the color sensor of the ev3, I use https://github.com/dwalton76/rubiks-cube-tracker to get the cubestring. This is faster and more reliable.
Follow the exact instruction for this package. You will need both https://github.com/dwalton76/rubiks-color-resolver and https://github.com/dwalton76/rubiks-cube-NxNxN-solver. As described on the readme.md.

After installing those 3 packages, run the following:
```
$ cd ~/rubiks-cube-NxNxN-solver
$ source ./venv/bin/activate
$ rubiks-cube-tracker.py --webcam 0
  # ^^^ this will print alot of things in the console. Look for something like BLBUUDRRFDRUURRRBRBBLLFRLLFUDDUDDDDUUFDLLULBFRBLFBFFFB
  
$ python3 mindcuber-python BLBUUDRRFDRUURRRBRBBLLFRLLFUDDUDDDDUUFDLLULBFRBLFBFFFB
  #Instead of "mindcuber-python", write the full path for it
```

You can also automate this. 
1. Go to **site-packages** of your version of python (mine is here: /lib/python3.9/site-packages/).
2. Open the folder "rubikscubetracker"
3. Open __init__.py
4. 
