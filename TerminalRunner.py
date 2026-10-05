import keyboard
import time
import os
from collections import deque
from itertools import cycle, islice
Display=deque([" "]*150)
Runner=input("Choose the RUNNER: ")
item=input("Choose your ENEMY: ")
speed=int(input("Choose the speed:(1-10): "))
Wall_gap=int(input("Choose gap: "))
snake=input("snake or not?(y to enable) ").lower()
speed=speed/100
index=2
attack_range=[50,70]
attack_list=[pos for pos in range(attack_range[0],attack_range[1])]
attack_list.extend(attack_list[::-1])
score=0
Wall_1= list(islice(cycle(attack_list), 1000))
Wall_2= list(islice(cycle([pos+Wall_gap for pos in attack_list]), 10000))
x=0
Display[75]=Runner
def s(l):
    return "".join(l)
while True:
    Display[0]=f"Score:{score}"
    if keyboard.is_pressed('space'):
        print("-"*70+"Exiting Game"+"-"*70)
        print("-"*70+f"Score:{score}"+"-"*70)
        break
    if x<len(Display)-1:
        if keyboard.is_pressed('right'):
            x=Display.index(Runner)
            Display[x]=" "
            Display[x+1]=Runner
        if keyboard.is_pressed('left'):
            x=Display.index(Runner)
            Display[x]=" "
            Display[x-1]=Runner
    Display[Wall_1[index]]=item
    Display[Wall_2[index]]=item
    print(s(Display))
    Display[Wall_1[index]]=" "
    Display[Wall_2[index]]=" "
    index+=1
    score+=1
    time.sleep(speed)
    if index>140:
        index=0
    if Runner not in Display or Wall_1[index]==Display.index(Runner)or Wall_2[index]==Display.index(Runner):
        print("-"*70+"GAME OVER"+"-"*70)
        print("-"*70+f"Score:{score}"+"-"*70)
        break
    if snake!='y':
        os.system('cls')


