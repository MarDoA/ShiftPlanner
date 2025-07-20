from graphics import Window
from logic import *
import json

def main():
    people = load()
        
    win = Window(1000,800,people)
    win.wait_for_close()
        



main()