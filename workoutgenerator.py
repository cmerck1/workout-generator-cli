from random import sample
from exercises import *

#Create the generator class which will actually create the routines according to the desired number of days per week.
class Generator(object):
    days = input("How many days would you like to workout this week?\n>>> ")
    #Get  input from user for goals and store it in a variable called "goal".
    goal = input("Is your goal to gain strength, endurance, or hypertrophy?\n>>> ")
    goal = goal.lower()
    #This section changes the information printed out and the format printed according to the goal.
    if "strength" in goal:
        sets = "5-8"
        target_reps = "1-6"
        actual_reps = "__/__/__/__/__/__/__/__"
        template = '| {:^35} | {:^7} | {:^6} | {:^12} | {:^27} |'
    elif "endurance" in goal:
        sets = "1-3"
        target_reps = "15-20"
        actual_reps = "__/__/__"
        template = '| {:^50} | {:^7} | {:^6} | {:^12} | {:^12} |'
    elif "hypertrophy" in goal:
        sets = "4"
        target_reps = "8-12"
        actual_reps = "__/__/__/__"
        template = '| {:^50} | {:^7} | {:^6} | {:^12} | {:^12} |'
    else:
        print ("Sorry, please try again.")
    #Loop through the input request until the user gives a number. The loop continues until a number is given.
    while True:
        try:
            days = int(days)
        except ValueError:
            print ("Oops, try entering a number, like 3.")
            days = input("How many days would you like to workout this week?\n>>> ")
        else:
            break
    #If the user only wants to work out 1 day of the week, a full body workout will be generated.
    if days == 1:
        #The format for the header.
        print("-" * 103)
        print('| {:^99} |'.format("You should workout at least 2-3 times a week, but if you can only manage one day this week,"))
        print('| {:^99} |'.format("here's your routine:"))
        print("|", "-" * 99, "|")
        #The sample method grabs a number of random exercises from the given list and stores it in a variable according to the exercise.
        chest_exercises = sample(Chest.exercises, 1)
        back_exercises = sample(Back.exercises, 1)
        legs_exercises = sample(Legs.exercises, 1)
        lower_legs_exercises = sample(Lower_Legs.exercises, 1)
        biceps_exercises = sample(Biceps.exercises, 1)
        triceps_exercises = sample(Triceps.exercises, 1)
        shoulders_exercises = sample(Shoulders.exercises, 1)
        forearms_exercises = sample(Forearms.exercises, 1)
        abs_exercises = sample(Abs.exercises, 1)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        #This section prints out the exercises in a list according to the template above.
        for item in chest_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in back_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in biceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in triceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in forearms_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in abs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"))
        print("-" * 103)
    #A 2 day split should consist of an upper body and a lower body day.
    elif days == 2:
        print("-" * 103)
        print('| {:^99} |'.format("Upper Body Day"))
        print("|", "-" * 99, "|")
        chest_exercises = sample(Chest.exercises, 2)
        back_exercises = sample(Back.exercises, 2)
        biceps_exercises = sample(Biceps.exercises, 1)
        triceps_exercises = sample(Triceps.exercises, 1)
        shoulders_exercises = sample(Shoulders.exercises, 1)
        forearms_exercises = sample(Forearms.exercises, 1)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in chest_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in back_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in biceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in triceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in forearms_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Lower Body Day"))
        print("|", "-" * 99, "|")
        legs_exercises = sample(Legs.exercises, 3)
        lower_legs_exercises = sample(Lower_Legs.exercises, 2)
        abs_exercises = sample(Abs.exercises, 2)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in abs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"))
        print("-" * 103)
    #A 3 day split will have a chest day, back day, and leg day.
    elif days == 3:
        print("-" * 103)
        print('| {:^99} |'.format("Chest Day"))
        print("|", "-" * 99, "|")
        chest_exercises = sample(Chest.exercises, 3)
        triceps_exercises = sample(Triceps.exercises, 2)
        shoulders_exercises = sample(Shoulders.exercises, 2)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in chest_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in triceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Back Day"))
        print("|", "-" * 99, "|")
        back_exercises = sample(Back.exercises, 3)
        biceps_exercises = sample(Biceps.exercises, 2)
        forearms_exercises = sample(Forearms.exercises, 2)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in back_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in biceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in forearms_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Leg Day"))
        print("|", "-" * 99, "|")
        legs_exercises = sample(Legs.exercises, 3)
        lower_legs_exercises = sample(Lower_Legs.exercises, 2)
        abs_exercises = sample(Abs.exercises, 2)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in abs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"))
        print("-" * 103)
    #A 4 day split should have a Chest Day, Back Day, Leg Day, and Shoulder/Forearm/Ab Day
    elif days == 4:
        print("-" * 103)
        print('| {:^99} |'.format("Chest Day"))
        print("|", "-" * 99, "|")
        chest_exercises = sample(Chest.exercises, 4)
        triceps_exercises = sample(Triceps.exercises, 3)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in chest_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in triceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Back Day"))
        print("|", "-" * 99, "|")
        back_exercises = sample(Back.exercises, 4)
        biceps_exercises = sample(Biceps.exercises, 3)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in back_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in biceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Leg Day"))
        print("|", "-" * 99, "|")
        legs_exercises = sample(Legs.exercises, 4)
        lower_legs_exercises = sample(Lower_Legs.exercises, 3)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Arm Day"))
        print("|", "-" * 99, "|")
        shoulders_exercises = sample(Shoulders.exercises, 3)
        forearms_exercises = sample(Forearms.exercises, 3)
        abs_exercises = sample(Abs.exercises, 3)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in shoulders_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in forearms_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        for item in abs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps)) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"))
        print("-" * 103)
    #If the user tries to input more than 6 days, a warning comes up that they should rest at least one day and
    #no workout is generated. In the future I'd like to make this loop so that it continues until the number 
    #given is less than 7.
    elif days >= 5:
        print ("You should take a couple of days per week to rest.")
        pass
