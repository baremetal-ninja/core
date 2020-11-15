"""Core bare metal build"""

__version__ = "0.0.0"

from . import core

def main():
    print("hello ninja")
    core.build()
