# Mindcuber-Python
A program written in python3 (3.9) that solves a Rubik's cube with a ev3 Mindstorms, without needing a SD card.

Very easy to setup. Just follow the steps.

You need to build the mindcuber robot. The "MindCub3r-v1p0.pdf" file has the building instructions (You can also find them  at https://www.mindcuber.com).

### Table of contents
1. Installation
2. Automatic setup
3. Manual setup (Use this if automatic fails)

### Table of contents

1. Color detection
2. Automating color detection / solving cube

## Installation

This program uses a library called "ev3-dc" (https://pypi.org/project/ev3-dc/) and uses Kociemba (https://pypi.org/project/kociemba/).

```
pip install ev3-dc
pip install kociemba
```

The motor of the arm should connect to the A Port.
The motor of the platform should connect to the B Port.

Save the file mindcuber-python.py in some place you can access easily.

To run the program:
```
$ python3 mindcuber-python.py CUBESTRING
  #Instead of "mindcuber-python", write the full path of it
```

See https://pypi.org/project/kociemba/ to understand what a Cubestring is

## Color detection

Instead of using the color sensor of the ev3, I use https://github.com/dwalton76/rubiks-cube-tracker to get the cubestring. This is faster and more reliable.
You will also need https://github.com/dwalton76/rubiks-color-resolver.

```
$ pip install python-opencv
  # ^^^ rubiks-cube-tracker uses opencv
  
$ pip install git+https://github.com/dwalton76/rubiks-cube-tracker.git

$ pip install git+https://github.com/dwalton76/rubiks-color-resolver.git
```

After installing those packages, run the following:
```
$ rubiks-cube-tracker.py --webcam 0
  # ^^^ this will print alot of things in the console. Look for something like BLBUUDRRFDRUURRRBRBBLLFRLLFUDDUDDDDUUFDLLULBFRBLFBFFFB
  
$ python3 mindcuber-python.py BLBUUDRRFDRUURRRBRBBLLFRLLFUDDUDDDDUUFDLLULBFRBLFBFFFB
  #Instead of "mindcuber-python", write the full path of it
```

## Automating color detection / solving cube

Instead of getting the cubestring and then running "mindcuber-python.py" with it, we can automate it:

1. Go to **site-packages** of your version of python (mine is here: /lib/python3.9/site-packages/).
2. Open the folder "rubikscubetracker"
3. Open \__init\__.py
4. Search for "kociemba_string"
<img width="783" alt="Screenshot 2021-04-27 at 17 03 15" src="https://user-images.githubusercontent.com/82064173/116274326-796d7f80-a77a-11eb-9296-4f65b016f07a.png">
5. Add the following:

```python3
import subprocess
subprocess.Popen("python3 path_to_mindcuber-python.py " + kociemba_string, shell=True)
                            #^^^ again, write the full path
```

<img width="852" alt="Screenshot 2021-04-27 at 17 05 31" src="https://user-images.githubusercontent.com/82064173/116274671-c81b1980-a77a-11eb-8cf1-6325ce6b7a07.png">

6. Just run:

```
$ rubiks-cube-tracker.py --webcam 0
```

This will get the colors and start solving the cube.

Pretty nice, right?


Sorry I couldnt include this "automation" in this repo. Im new to github and it is really weird.

Any questions, just open up an *issue*. I'll anwser as fast as possible.

Hope this helped :)
