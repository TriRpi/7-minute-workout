#!/usr/bin/env python3

import os
from time import sleep

# clear screen
os.system('cls' if os.name == 'nt' else 'clear')

print("welcome to the 7 minute work-out")

# list with all exercizes to perform
exercises = ["jumping jacks", "Wall sit", "Push-up", "Abdominal crunch", "Step-up onto chair", "squat", "triceps dip on chair", "Plank", "High knees running in place", "Lunge", "Push-up and rotation", "Side Plank"]

exercise_duration = 1 # time of exercize
rest_duration = 1     # time of rest

# when enter gets pressed, program will continue
input("press enter to continue")

# for every exercize do
for workout in exercises:
   
   print(workout)

# if it isn't last workout
   if not (workout == exercises[-1]):
       nextup = exercises.index(workout) + 1
       print("next up: " + exercises[nextup])

       sleep(exercise_duration)

       print("rest")
       sleep(rest_duration)
   else:
       sleep(exercise_duration)

print("well done, you burned 100000000 calories")
