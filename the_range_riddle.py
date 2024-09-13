import random

moods = ["happy", "sad", "energetic", "calm"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for day in days:
    mood = random.choice(moods)
    print(f"On {day} you felt {mood}")
