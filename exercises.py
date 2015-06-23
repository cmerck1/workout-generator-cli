#Create different classes for each muscle group and store a list of exercises in each.
#Exercises should be separated according to the equipment used.
class Chest(object):
    exercises = []
    selectorized = ["Seated Chest Press", "Seated Fly"]
    dumbbell = ["Dumbbell Chest Press", "Dumbbell Flies", "Inclined Dumbbell Chest Press", "Declined Dumbbell Chest Press",]
    barbell = ["Barbell Chest Press", "Inclined Barbell Chest Press", "Declined Barbell Chest Press"]
    cable = ["Cable Crossovers"]
    calisthenics = ["Push Ups", "Inclined Push Ups", "Stability Ball Pushups", "Medicine Ball Push Ups"]

class Back(object):
    exercises = []
    selectorized = []
    dumbbell = ["Dumbbell Bent-Over Row",]
    barbell = ["Barbell Bent-Over Row",]
    cable = ["Seated Cable Row", "Seated Cable Lat-Pulldown"]
    calisthenics = ["Pull Ups",]

class Legs(object):
    exercises = []
    selectorized = ["Leg Press", "Quadriceps Extensions", "Hamstring Curls"]
    dumbbell = []
    barbell = ["Barbell Deadlifts",]
    cable = []
    calisthenics = ["Squats"]

class Lower_Legs(object):
    exercises = []
    selectorized = ["Smith Press Calf Raises", "Leg Press Calf Raises"]
    dumbbell = ["Dumbbell Calf Raises", ]
    barbell = []
    cable = []
    calisthenics = []

class Biceps(object):
    exercises = ["Dumbbell Preacher Curls", "Dumbbell Hammer Curls", "Barbell Preacher Curls", "Cable Hammer Curls", "Cable Preacher Curls"]
    selectorized = []
    dumbbell = []
    barbell = []
    cable = []
    calisthenics = []

class Triceps(object):
    exercises = ["Overhead Dumbbell Triceps Extensions", "Overhead Cable Triceps Extensions", "Narrow-Grip Barbell Bench Press", "Narrow-Grip Dumbbell Bench Press", "Weighted Dips", "Cable Triceps Pull-Down"]
    selectorized = []
    dumbbell = []
    barbell = []
    cable = []
    calisthenics = []

class Shoulders(object):
    exercises = ["Dumbbell Lateral Flies", "Dumbbell Shoulder Press", "Barbell Shoulder Press", "Cable Reverse Crossover"]
    selectorized = []
    dumbbell = []
    barbell = []
    cable = []
    calisthenics = []

class Forearms(object):
    exercises = ["Barbell Wrist Flexion", "Barbell Wrist Extension", "Weighted String Flexion", "Weighted String Extension"]
    selectorized = []
    dumbbell = []
    barbell = []
    cable = []
    calisthenics = []

class Abs(object):
    exercises = ["Crunches", "Dead Bugs", "Hanging Leg Lifts", "Windshield Wipers", "Planks", "Flutter Kicks"]
    selectorized = []
    dumbbell = []
    barbell = []
    cable = []
    calisthenics = []
