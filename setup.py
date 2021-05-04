from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pynput>=1.7.3"]

setup(
    name="cookie_clicker-bot",
    version="1",
    author="PBeGood4",
    author_email="pbegood.mail@gmail.com",
    description="Fastest cookie clicker bot in the west.",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="cookie clicker bot python",
    url="https://github.com/PBeGood4/cookie_clicker-bot/",
    scripts=["cookiebot.py"],
    packages=[],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
