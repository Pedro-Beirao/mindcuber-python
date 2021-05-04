from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ev3_dc","kociemba","python-opencv","rubiks-cube-tracker @ git+https://github.com/dwalton76/rubiks-cube-tracker","rubiks-color-resolver @ git+https://github.com/dwalton76/rubiks-color-resolver"]

setup(
    name="mindcuber-python",
    version="1",
    author="PBeGood4",
    author_email="pbegood.mail@gmail.com",
    description="A program written in python that solves a Rubik's cube with a ev3 Mindstorms, without needing a SD card.",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="mindcuber python ev3 rubiks",
    url="https://github.com/PBeGood4/mindcuber-python/",
    scripts=["rubik.py","mindcuber-python.py"],
    packages=["rubikscubetracker"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
