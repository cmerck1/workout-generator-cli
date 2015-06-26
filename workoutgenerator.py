from random import sample
from exercises import *
log = open("/home/billy/Desktop/Workout.txt", "w")

#Create the generator class which will actually create the routines according to the desired number of days per week.
class Generator(object):
    def get_goal(self):
        #Get  input from user for goals and store it in a variable called "goal".
        goal = input("Is your goal to gain strength, endurance, or hypertrophy?\n>>> ")
        goal = goal.lower()
        #This section changes the information printed out and the format printed according to the goal.
        while True:
            if "strength" in goal:
                self.sets = "5-8"
                self.target_reps = "1-6"
                self.actual_reps = "__/__/__/__/__/__/__/__"
                self.template = '| {:^38} | {:^7} | {:^6} | {:^12} | {:^24} |'
                break
            elif "endurance" in goal:
                self.sets = "1-3"
                self.target_reps = "15-20"
                self.actual_reps = "__/__/__"
                self.template = '| {:^50} | {:^7} | {:^6} | {:^12} | {:^12} |'
                break
            elif "hypertrophy" in goal:
                self.sets = "4"
                self.target_reps = "8-12"
                self.actual_reps = "__/__/__/__"
                self.template = '| {:^50} | {:^7} | {:^6} | {:^12} | {:^12} |'
                break
            else:
                print ("Sorry, please try again.")
                goal = input("Is your goal to gain strength, endurance, or hypertrophy?\n>>> ")
                goal = goal.lower()
        return self.sets, self.target_reps, self.actual_reps, self.template

    def get_frequency(self):
        #Ask the user how many days per week they want to work out and store that number in a variable called
        #"days".
        self.days = input("How many days would you like to workout this week?\n>>> ")

        #Loop through the input request until the user gives a number. The loop continues until a number is given.
        while True:
            try:
                self.days = int(self.days)
            except ValueError:
                print ("Oops, try entering a number, like 3.")
                self.days = input("How many days would you like to workout this week?\n>>> ")
            else:
                break
        return self.days

    #This funciton takes the user's preferences for each given category of exercises and if the user says
    #they do like using a given piece of equipment/style of working out, then the list of those exercises
    #for each muscle group are added to the main list for each muscle group. If the user says they don't
    #like a certain type of exercise, then the list of those exercises is just ignored. Only exercises
    #found in the main exercises list are used when generating the workout.
    def user_preference(self, equipment0, equipment1, equipment2, equipment3, equipment4, equipment5, equipment6, equipment7, equipment8, name):
        preference = input("Do you like using and/or have access to {!s}?\n>>> ".format(name))
        while True:
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
                break
            elif "n" in preference:
                break
            else:
                print ("Sorry, please try inputting yes or no.")
                preference = input("Do you like using and/or have access to {!s}?\n>>> ".format(name))
        return preference

    def get_preferences(self):
        #Here the function is called for each type of exercise to build the main exercise list which
        #is the only list considered in generating the workout.
        Generator.user_preference(self, Chest.selectorized, Back.selectorized, Legs.selectorized, Lower_Legs.selectorized, Biceps.selectorized, Triceps.selectorized, Shoulders.selectorized, Forearms.selectorized, Abs.selectorized, "selectorized equipment")
        #In order to remove some repition, and since dumbbells and barbells are part of the free
        #weights category, the program will only ask the user if they want to use dumbbells and
        #barbells if they have already said that they like free weights. Otherwise, those two
        #options are skipped.
        fwpref = Generator.user_preference(self, Chest.free_weights, Back.free_weights, Legs.free_weights, Lower_Legs.free_weights, Biceps.free_weights, Triceps.free_weights, Shoulders.free_weights, Forearms.free_weights, Abs.free_weights, "free weights")
        if "y" in fwpref:
            Generator.user_preference(self, Chest.dumbbell, Back.dumbbell, Legs.dumbbell, Lower_Legs.dumbbell, Biceps.dumbbell, Triceps.dumbbell, Shoulders.dumbbell, Forearms.dumbbell, Abs.dumbbell, "dumbbell")
            Generator.user_preference(self, Chest.barbell, Back.barbell, Legs.barbell, Lower_Legs.barbell, Biceps.barbell, Triceps.barbell, Shoulders.barbell, Forearms.barbell, Abs.barbell, "barbell")
        else:
            pass
        Generator.user_preference(self, Chest.calisthenics, Back.calisthenics, Legs.calisthenics, Lower_Legs.calisthenics, Biceps.calisthenics, Triceps.calisthenics, Shoulders.calisthenics, Forearms.calisthenics, Abs.calisthenics, "calisthenic exercises")
        Generator.user_preference(self, Chest.cable, Back.cable, Legs.cable, Lower_Legs.cable, Biceps.cable, Triceps.cable, Shoulders.cable, Forearms.cable, Abs.cable, "cable equipment")

    #The format for the header, taking the name of the workout day as an argument.
    def header(workout):
        if "Chest" in workout or "Full" in workout or "Upper" in workout:
            print("-" * 103, file = log)
            print('| {:^99} |'.format(workout), file = log)
            print("|", "-" * 99, "|", file = log)
        else:
            print("|", "-" * 99, "|", file = log)
            print('| {:^99} |'.format(workout), file = log)
            print("|", "-" * 99, "|", file = log)

    def section(name):
        if name == "Warm Ups":
            print('| {:<99} |'.format(name), file = log)
            print("|", "-" * 99, "|", file = log)
            print('| {:^99} |'.format("Refer to the " + name + " section of the app for the muscles you are training."), file = log)
            print("|", "-" * 99, "|", file = log)
        elif name == "Cool Down":
            print("|", "-" * 99, "|", file = log)
            print('| {:<99} |'.format(name), file = log)
            print("|", "-" * 99, "|", file = log)
            print('| {:^99} |'.format("Refer to the " + name + " section of the app for the muscles you are training."), file = log)
        else:
            print('| {:<99} |'.format(name), file = log)
            print("|", "-" * 99, "|", file = log)

    #This formats the titles of the columns.
    def titles(self):
        print (self.template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"), file = log)
        print("|", "-" * 99, "|", file = log)

    #This closes up the table at the bottom and adds a little note.
    def footer():
        print("|", "-" * 99, "|", file = log)
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"), file = log)
        print("-" * 103, file = log)

    #These methods print out all of the exercises for each given muscle group.
    def print_exercises(self, muscle_group):
        for item in muscle_group:
            print (self.template.format(item, '_____', self.sets, self.target_reps, self.actual_reps), file = log) 

    def give_workout(self, days):
        #If the user only wants to work out 1 day of the week, a full body workout will be generated.
        if self.days == 1:
            Generator.header("Full Body Day")
            #The sample method grabs a number of random exercises from the given list and stores
            #them in a variable according to the exercise.
            chest_exercises = sample(Chest.exercises, 1)
            back_exercises = sample(Back.exercises, 1)
            legs_exercises = sample(Legs.exercises, 1)
            lower_legs_exercises = sample(Lower_Legs.exercises, 1)
            biceps_exercises = sample(Biceps.exercises, 1)
            triceps_exercises = sample(Triceps.exercises, 1)
            shoulders_exercises = sample(Shoulders.exercises, 1)
            forearms_exercises = sample(Forearms.exercises, 1)
            abs_exercises = sample(Abs.exercises, 1)
            Generator.section("Warm Ups")
            #This section prints out the exercises in a list according to the template above.
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, chest_exercises)
            Generator.print_exercises(self, back_exercises)
            Generator.print_exercises(self, legs_exercises)
            Generator.print_exercises(self, lower_legs_exercises)
            Generator.print_exercises(self, biceps_exercises)
            Generator.print_exercises(self, triceps_exercises)
            Generator.print_exercises(self, shoulders_exercises)
            Generator.print_exercises(self, forearms_exercises)
            Generator.print_exercises(self, abs_exercises)
            Generator.section("Cool Down")
            Generator.footer()
        #A 2 day split should consist of an upper body and a lower body day.
        elif days == 2:
            Generator.header("Upper Body Day")
            chest_exercises = sample(Chest.exercises, 2)
            back_exercises = sample(Back.exercises, 2)
            biceps_exercises = sample(Biceps.exercises, 1)
            triceps_exercises = sample(Triceps.exercises, 1)
            shoulders_exercises = sample(Shoulders.exercises, 1)
            forearms_exercises = sample(Forearms.exercises, 1)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, chest_exercises)
            Generator.print_exercises(self, back_exercises)
            Generator.print_exercises(self, biceps_exercises)
            Generator.print_exercises(self, triceps_exercises)
            Generator.print_exercises(self, shoulders_exercises)
            Generator.print_exercises(self, forearms_exercises)
            Generator.section("Cool Down")
            Generator.header("Lower Body Day")
            legs_exercises = sample(Legs.exercises, 3)
            lower_legs_exercises = sample(Lower_Legs.exercises, 2)
            abs_exercises = sample(Abs.exercises, 2)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, legs_exercises)
            Generator.print_exercises(self, lower_legs_exercises)
            Generator.print_exercises(self, abs_exercises)
            Generator.section("Cool Down")
            Generator.footer()
        #A 3 day split will have a chest day, back day, and leg day.
        elif days == 3:
            Generator.header("Chest Day")
            chest_exercises = sample(Chest.exercises, 3)
            triceps_exercises = sample(Triceps.exercises, 2)
            shoulders_exercises = sample(Shoulders.exercises, 2)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, chest_exercises)
            Generator.print_exercises(self, triceps_exercises)
            Generator.print_exercises(self, shoulders_exercises)
            Generator.section("Cool Down")
            Generator.header("Back Day")
            back_exercises = sample(Back.exercises, 3)
            biceps_exercises = sample(Biceps.exercises, 2)
            forearms_exercises = sample(Forearms.exercises, 2)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, back_exercises)
            Generator.print_exercises(self, biceps_exercises)
            Generator.print_exercises(self, forearms_exercises)
            Generator.section("Cool Down")
            Generator.header("Leg Day")
            legs_exercises = sample(Legs.exercises, 3)
            lower_legs_exercises = sample(Lower_Legs.exercises, 2)
            abs_exercises = sample(Abs.exercises, 2)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, legs_exercises)
            Generator.print_exercises(self, lower_legs_exercises)
            Generator.print_exercises(self, abs_exercises)
            Generator.section("Cool Down")
            Generator.footer()
        #A 4 day split should have a Chest Day, Back Day, Leg Day, and Shoulder/Forearm/Ab Day
        elif days == 4:
            Generator.header("Chest Day")
            chest_exercises = sample(Chest.exercises, 4)
            triceps_exercises = sample(Triceps.exercises, 3)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, chest_exercises)
            Generator.print_exercises(self, triceps_exercises)
            Generator.section("Cool Down")
            Generator.header("Back Day")
            back_exercises = sample(Back.exercises, 4)
            biceps_exercises = sample(Biceps.exercises, 3)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, back_exercises)
            Generator.print_exercises(self, biceps_exercises)
            Generator.section("Cool Down")
            Generator.header("Leg Day")
            legs_exercises = sample(Legs.exercises, 4)
            lower_legs_exercises = sample(Lower_Legs.exercises, 3)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, legs_exercises)
            Generator.print_exercises(self, lower_legs_exercises)
            Generator.section("Cool Down")
            Generator.header("Arm Day")
            shoulders_exercises = sample(Shoulders.exercises, 3)
            forearms_exercises = sample(Forearms.exercises, 3)
            abs_exercises = sample(Abs.exercises, 3)
            Generator.section("Warm Ups")
            Generator.section("Workout")
            Generator.titles(self)
            Generator.print_exercises(self, shoulders_exercises)
            Generator.print_exercises(self, forearms_exercises)
            Generator.print_exercises(self, abs_exercises)
            Generator.section("Cool Down")
            Generator.footer()
        #If the user tries to input more than 6 days, a warning comes up that they should rest at least one day and
        #no workout is generated. In the future I'd like to make this loop so that it continues until the number 
        #given is less than 7.
        elif days >= 5:
            print ("You should take a couple of days per week to rest.")
            pass

gen1 = Generator()
gen1.get_goal()
gen1.get_preferences()
days = gen1.get_frequency()
gen1.give_workout(days)
