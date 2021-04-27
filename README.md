# mindcuber-python
A program that solves a Rubik's cube with a ev3 Mindstorms, without needing a SD card.

You need to build the mindcuber robot. The "MindCub3r-v1p0.pdf" file has the building instructions (You can also find them  at https://www.mindcuber.com).

This program uses a library called "ev3-dc" (https://pypi.org/project/ev3-dc/).

```
pip install ev3-dc
```

The motor of the arm should connect to the A Port.
The motor of the platform should connect to the B Port.

To run the program:
```
python3 mindcuber-python CUBESTRING
```
