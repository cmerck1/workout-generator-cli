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












