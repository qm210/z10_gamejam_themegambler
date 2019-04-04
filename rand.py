#!/usr/bin/python3

from numpy.random import choice
import sys
import os
import time
from math import *

if __name__ == '__main__':
    with open('wordlist','r') as f:
        wordlist = f.read().split()

    mode = sys.argv[1] if len(sys.argv)>1 else ''

    boxlength = len(max(wordlist, key=len)) + 2
    box1 = boxlength*' '
    box2 = boxlength*' '
    box3 = boxlength*' '
    boxwidth = 3*boxlength + 6
    boxtitle = "Z10 GAME JAM THEME GAMBLE     - v4/19 QM"
    boxspacesL = int(0.5*(boxwidth - len(boxtitle)))
    boxspacesR = int(0.5*(boxwidth - len(boxtitle))+.5)

    margin_h = 70
    margin_v = 20

    shufflesteps  = 200

    for counter in range(3):

        for step in range(shufflesteps):
    
            word = choice(wordlist)	
            spacesL = int(0.5*(boxlength - len(word)))
            spacesR = int(0.5*(boxlength - len(word))+.5)


            if counter == 0:
                box1 = spacesL*' ' + word + spacesR*' '
            elif counter == 1:
                box2 = spacesL*' ' + word + spacesR*' '
            elif counter == 2:
                box3 = spacesL*' ' + word + spacesR*' '
              
            os.system('clear')
            for _ in range(margin_v): print()
            print(margin_h*' ' + '╔═' + boxwidth*'═' + '═╗')
            print(margin_h*' ' + '║ ' + boxwidth*' ' + ' ║')
            print(margin_h*' ' + '║ ' + boxspacesL*' ' + boxtitle + boxspacesR*' ' + ' ║')
            print(margin_h*' ' + '║ ' + boxwidth*' ' + ' ║')
            print(margin_h*' ' + '╠═' + boxlength*'═' + '═╦═' + boxlength*'═' + '═╦═' + boxlength*'═' + '═╣')
            print(margin_h*' ' + '║ ' + box1 + ' ║ ' + box2 + ' ║ ' + box3 + ' ║')
            print(margin_h*' ' + '╚═' + boxlength*'═' + '═╩═' + boxlength*'═' + '═╩═' + boxlength*'═' + '═╝')
            for _ in range(margin_v): print()
              
            delaytime = .01 + .99 * pow(float(step)/shufflesteps, 20)
            time.sleep(delaytime)

        wordlist.remove(word)
