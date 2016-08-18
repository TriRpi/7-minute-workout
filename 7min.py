#!/usr/bin/env python3

import os 
import time

# clear screen
os.system('clear')

print("welcome to the 7 minute work-out")

# list with all exercizes to perform
exercizes = ["jumping jacks", "Wall sit", "Push-up", "Abdominal crunch", "Step-up onto chair", "squat", "triceps dip on chair", "Plank", "High knees running in place", "Lunge", "Push-up and rotation", "Side Plank"]

exercize_duration = 1 # time of exercize
rest_duration = 1     # time of rest

print("press enter to continue")

# when enter gets pressed, program will continue
input()

# for every exercize do
for workout in range(len(exercizes)):
   
   print(exercizes[workout])

# if it isn't last workout
   if not (workout == len(exercizes)):
       nextup = exercizes[workout + 1]
       print("next up: " + nextup)

   time.sleep(exercize_duration)

   print("rest")
   time.sleep(rest_duration)

print("well done, you burned 100000000 calories")
