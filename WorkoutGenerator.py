from random import sample

#Create different classes for each muscle group and store a list of exercises in each.
class Muscle_Group(object):
    exercises = []

class Chest(Muscle_Group):
    exercises = ["Push Ups","Barbell Chest Press", "Dumbbell Chest Press","Dumbbell Flies","Cable Crossovers","Inclined Dumbbell Chest Press","Inclined Barbell Chest Press","Declined Dumbbell Chest Press","Declined Barbell Chest Press"]

class Back(Muscle_Group):
    exercises = ["Pull Ups","Barbell Bent-Over Row","Seated Cable Row","Dumbbell Bent-Over Row","Seated Lat-Pulldown"]

class Legs(Muscle_Group):
    exercises = ["Squats", "Deadlifts", "Leg Press", "Quadriceps Extensions", "Hamstring Curls"]

class Lower_Legs(Muscle_Group):
    exercises = ["Dumbbell Calf Raises", "Smith Press Calf Raises", "Leg Press Calf Raises"]

class Biceps(Muscle_Group):
    exercises = ["Dumbbell Preacher Curls", "Dumbbell Hammer Curls", "Barbell Preacher Curls", "Cable Hammer Curls", "Cable Preacher Curls"]

class Triceps(Muscle_Group):
    exercises = ["Overhead Dumbbell Triceps Extensions", "Overhead Cable Triceps Extensions", "Narrow-Grip Barbell Bench Press", "Narrow-Grip Dumbbell Bench Press", "Weighted Dips", "Cable Triceps Pull-Down"]

class Shoulders(Muscle_Group):
    exercises = ["Dumbbell Lateral Flies", "Dumbbell Shoulder Press", "Barbell Shoulder Press", "Cable Reverse Crossover"]

class Forearms(Muscle_Group):
    exercises = ["Barbell Wrist Flexion", "Barbell Wrist Extension", "Weighted String Flexion", "Weighted String Extension"]

class Abs(Muscle_Group):
    exercises = ["Crunches", "Dead Bugs", "Hanging Leg Lifts", "Windshield Wipers", "Planks", "Flutter Kicks"]

#Create the generator class which will actually create the routines according to the desired number of days per week.
class Generator(object):
    #This will be the template for the table so that it all prints out uniformly.
    template = '| {:^50} | {:^7} | {:^6} | {:^12} | {:^12} |'
    #Get input from the user for number of days per week to work out and store it in a variable called "days".
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
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in back_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in legs_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in biceps_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in triceps_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in forearms_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in abs_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
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
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in back_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in biceps_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in triceps_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in forearms_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Lower Body Day"))
        print("|", "-" * 99, "|")
        legs_exercises = sample(Legs.exercises, 3)
        lower_legs_exercises = sample(Lower_Legs.exercises, 2)
        abs_exercises = sample(Abs.exercises, 2)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in legs_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in lower_legs_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in abs_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"))
        print("-" * 103)
    #A 3 day split will have a chest day, back day, and leg day.
    elif days == 3:
        print("-" * 103)
        print('| {:^99} |'.format("Chest Day"))
        print("|", "-" * 99, "|")
        chest_exercises = sample(Chest.exercises, 1)
        triceps_exercises = sample(Triceps.exercises, 1)
        shoulders_exercises = sample(Shoulders.exercises, 1)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in chest_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in triceps_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in shoulders_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        print("|", "-" * 99, "|")
        print('| {:^99} |'.format("Back Day"))
        print("|", "-" * 99, "|")
        back_exercises = sample(Back.exercises, 2)
        biceps_exercises = sample(Biceps.exercises, 1)
        forearms_exercises = sample(Forearms.exercises, 1)
        print (template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))
        print("|", "-" * 99, "|")
        for item in back_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in biceps_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
        for item in forearms_exercises:
            print (template.format(item, '_____', '4', '8-12', '_____')) 
    #If the user tries to input more than 6 days, a warning comes up that they should rest at least one day and
    #no workout is generated. In the future I'd like to make this loop so that it continues until the number 
    #given is less than 7.
    elif days > 6:
        print ("You should take at least one day per week to rest.")
        pass
