# Mindcuber-Python
A program written in python3 (3.9) that solves a Rubik's cube with a ev3 Mindstorms, without needing a SD card.

Video: https://www.youtube.com/watch?v=Iczwq0FZBBg

___

Very easy to setup. Just follow the steps.

You need to build the mindcuber robot. The "MindCub3r-v1p0.pdf" file has the building instructions (You can also find them  at https://www.mindcuber.com).

The motor of the arm should connect to the A Port.
The motor of the platform should connect to the B Port.

Don't mind connecting the other cables. This program doesnt use them.

See this to connect your pc with the ev3 (Bluetooh does not work for MacOS) - https://ev3-dc.readthedocs.io/en/latest/examples_ev3.html#connect-with-the-ev3-device
(I strongly recommend USB)
### Table of contents
1. Installation
2. Setup
3. Run
4. Dependecies

## Installation

```
 # If you don't have opencv installed
$ pip install opencv-python

$ pip install git+https://github.com/PBeGood4/mindcuber-python
 # This will install all dependecies (except the opencv, that one needs to be installed separatly)
```

## Setup

**Open mindcuber-python.py**

To find this file:

### MacOS / Linux

```
which mindcuber-python.py
```

### Windows

```
where mindcuber-python.py
```

**Go to `ev3Device = ev3.EV3(protocol=ev3.USB, host='00:16:53:3D:F8:DF')`**

**Change `ev3.USB` To the protocol you want: `ev3.USB`, `ev3.BLUETOOTH` or `ev3.WIFI`** (I strongly recommend USB)

**Change `host='00:16:53:3D:F8:DF'` to your ev3's MAC adress** (Find the MAC adr in: Brick Info / ID).

 






## Run

```
$ rubik.py 
```

The scripts were installed to your PATH, there is no need to call "python3"

If it doesnt work, don't be afraid to open an *issue*.


## Dependecies

```
ev3-dc : https://github.com/ChristophGaukel/ev3-python3

kociemba : https://github.com/muodov/kociemba

opencv : https://github.com/opencv/opencv-python

rubiks-cube-tracker : https://github.com/dwalton76/rubiks-cube-tracker

rubiks-color-resolver : https://github.com/dwalton76/rubiks-color-resolver
```
