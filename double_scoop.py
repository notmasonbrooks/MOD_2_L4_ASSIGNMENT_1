import random

days_of_week = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]
time_of_day = ["morning", "afternoon", "evening"]
moods = ["happy", "sad", "calm", "energietic"]
for day in days_of_week:
    for time in time_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were feeling {mood}")
