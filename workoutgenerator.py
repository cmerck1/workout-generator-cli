from random import sample
from exercises import *
log = open("/home/billy/Desktop/Workout.txt", "w")

#Create the generator class which will actually create the routines according to the desired number of days per week.
class Generator(object):
    #Get  input from user for goals and store it in a variable called "goal".
    goal = input("Is your goal to gain strength, endurance, or hypertrophy?\n>>> ")
    goal = goal.lower()
    #This section changes the information printed out and the format printed according to the goal.
    if "strength" in goal:
        sets = "5-8"
        target_reps = "1-6"
        actual_reps = "__/__/__/__/__/__/__/__"
        template = '| {:^38} | {:^7} | {:^6} | {:^12} | {:^24} |'
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
    #Ask the user how many days per week they want to work out and store that number in a variable called
    #"days".
    days = input("How many days would you like to workout this week?\n>>> ")
    #Loop through the input request until the user gives a number. The loop continues until a number is given.
    while True:
        try:
            days = int(days)
        except ValueError:
            print ("Oops, try entering a number, like 3.")
            days = input("How many days would you like to workout this week?\n>>> ")
        else:
            break
    def user_preference(equipment0, equipment1, equipment2, equipment3, equipment4, equipment5, equipment6, equipment7, equipment8, name):
        preference = input("Do you like doing {!s} exercises?\n>>> ".format(name))
        if "y" in preference:
            for exercise in equipment0:
                Chest.exercises.append(exercise)
            for exercise in equipment1:
                Back.exercises.append(exercise)
            for exercise in equipment2:
                Legs.exercises.append(exercise)
            for exercise in equipment3:
                Lower_Legs.exercises.append(exercise)
            for exercise in equipment4:
                Biceps.exercises.append(exercise)
            for exercise in equipment5:
                Triceps.exercises.append(exercise)
            for exercise in equipment6:
                Shoulders.exercises.append(exercise)
            for exercise in equipment7:
                Forearms.exercises.append(exercise)
            for exercise in equipment8:
                Abs.exercises.append(exercise)
        elif "n" in preference:
            pass
        else:
            print ("Sorry, please try inputting yes or no.")
    user_preference(Chest.selectorized, Back.selectorized, Legs.selectorized, Lower_Legs.selectorized, Biceps.selectorized, Triceps.selectorized, Shoulders.selectorized, Forearms.selectorized, Abs.selectorized, "selectorized equipment")
    user_preference(Chest.dumbbell, Back.dumbbell, Legs.dumbbell, Lower_Legs.dumbbell, Biceps.dumbbell, Triceps.dumbbell, Shoulders.dumbbell, Forearms.dumbbell, Abs.dumbbell, "dumbbell")
    user_preference(Chest.barbell, Back.barbell, Legs.barbell, Lower_Legs.barbell, Biceps.barbell, Triceps.barbell, Shoulders.barbell, Forearms.barbell, Abs.barbell, "barbell")
    user_preference(Chest.calisthenics, Back.calisthenics, Legs.calisthenics, Lower_Legs.calisthenics, Biceps.calisthenics, Triceps.calisthenics, Shoulders.calisthenics, Forearms.calisthenics, Abs.calisthenics, "calisthenics")
    user_preference(Chest.cable, Back.cable, Legs.cable, Lower_Legs.cable, Biceps.cable, Triceps.cable, Shoulders.cable, Forearms.cable, Abs.cable, "cable equipment")
    #If the user only wants to work out 1 day of the week, a full body workout will be generated.
    if days == 1:
        #The format for the header.
        print("-" * 103, file = log)
        print('| {:^99} |'.format("Full Body Day"), file = log)
        print("|", "-" * 99, "|", file = log)
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
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        #This section prints out the exercises in a list according to the template above.
        for item in chest_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in back_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in biceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in triceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in forearms_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in abs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"), file = log)
        print("-" * 103, file = log)
    #A 2 day split should consist of an upper body and a lower body day.
    elif days == 2:
        print("-" * 103, file = log)
        print('| {:^99} |'.format("Upper Body Day"), file = log)
        print("|", "-" * 99, "|", file = log)
        chest_exercises = sample(Chest.exercises, 2)
        back_exercises = sample(Back.exercises, 2)
        biceps_exercises = sample(Biceps.exercises, 1)
        triceps_exercises = sample(Triceps.exercises, 1)
        shoulders_exercises = sample(Shoulders.exercises, 1)
        forearms_exercises = sample(Forearms.exercises, 1)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        for item in chest_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in back_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in biceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in triceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in forearms_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Lower Body Day"), file = log)
        print("|", "-" * 99, "|", file = log)
        legs_exercises = sample(Legs.exercises, 3)
        lower_legs_exercises = sample(Lower_Legs.exercises, 2)
        abs_exercises = sample(Abs.exercises, 2)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        for item in legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in abs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"), file = log)
        print("-" * 103, file = log)
    #A 3 day split will have a chest day, back day, and leg day.
    elif days == 3:
        print("-" * 103, file = log)
        print('| {:^99} |'.format("Chest Day"), file = log)
        print("|", "-" * 99, "|", file = log)
        chest_exercises = sample(Chest.exercises, 3)
        triceps_exercises = sample(Triceps.exercises, 2)
        shoulders_exercises = sample(Shoulders.exercises, 2)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        for item in chest_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in triceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Back Day"), file = log)
        print("|", "-" * 99, "|", file = log)
        back_exercises = sample(Back.exercises, 3)
        biceps_exercises = sample(Biceps.exercises, 2)
        forearms_exercises = sample(Forearms.exercises, 2)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        for item in back_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in biceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in forearms_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Leg Day"), file = log)
        print("|", "-" * 99, "|", file = log)
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
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"), file = log)
        print("-" * 103, file = log)
    #A 4 day split should have a Chest Day, Back Day, Leg Day, and Shoulder/Forearm/Ab Day
    elif days == 4:
        print("-" * 103, file = log)
        print('| {:^99} |'.format("Chest Day"), file = log)
        print("|", "-" * 99, "|", file = log)
        chest_exercises = sample(Chest.exercises, 4)
        triceps_exercises = sample(Triceps.exercises, 3)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        for item in chest_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in triceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Back Day"), file = log)
        print("|", "-" * 99, "|", file = log)
        back_exercises = sample(Back.exercises, 4)
        biceps_exercises = sample(Biceps.exercises, 3)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        for item in back_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in biceps_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Leg Day"), file = log)
        print("|", "-" * 99, "|", file = log)
        legs_exercises = sample(Legs.exercises, 4)
        lower_legs_exercises = sample(Lower_Legs.exercises, 3)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        for item in legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Arm Day"), file = log)
        print("|", "-" * 99, "|", file = log)
        shoulders_exercises = sample(Shoulders.exercises, 3)
        forearms_exercises = sample(Forearms.exercises, 3)
        abs_exercises = sample(Abs.exercises, 3)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)
        for item in shoulders_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in forearms_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        for item in abs_exercises:
            print (template.format(item, '_____', sets, target_reps, actual_reps), file = log) 
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"), file = log)
        print("-" * 103, file = log)
    #If the user tries to input more than 6 days, a warning comes up that they should rest at least one day and
    #no workout is generated. In the future I'd like to make this loop so that it continues until the number 
    #given is less than 7.
    elif days >= 5:
        print ("You should take a couple of days per week to rest.")
        pass
