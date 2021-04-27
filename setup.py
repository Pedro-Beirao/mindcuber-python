
from setuptools import setup

setup(
    name="mindcuber-python-noSDcard",
    version="1.0.0",
    description="Uses a ev3 mindstorms to solve a rubiks cube. Written in python. Whitout the need of a SD card",
    keywords="rubiks cube mindcuber ev3 mindstorms python",
    url="https://github.com/PBeGood4/mindcuber-python-noSDcard",
    author="PBeGood4",
    author_email="pedrocbeirao@gmail.com",
    license="GNU",
    scripts=["usr/bin/rubik.py"],
    packages=["ev3cubetracker"],
)