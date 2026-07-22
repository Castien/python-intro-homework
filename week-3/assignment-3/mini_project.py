

# Mini-Project — Day Planner
# Write a program that asks the user for a day of the week and a time of day
# (morning, afternoon, or evening), then suggests an activity.
# Requirements:
# Cover at least 3 days × 3 times = 9 combinations with distinct suggestions
# Handle any unrecognized day or time with a friendly fallback message
# Normalize input so capitalization doesn't matter 
# (e.g., "Monday" and "monday" both work)

print("Welcome to your Own Personal Cynical Planner Program.")

answer = input("I am so excited to plan your day. Can't you tell? ").strip().lower()
if answer == "yes" or answer == "y": 
    print("You're so great at reading the room...")
elif answer == "no" or answer == "n":
    print("No? Sorry, let me add some enthusiasm. ~Yay.~")
else:
    print("Maybe it's time to touch some grass this week.")

print("Let's get this over with.")
day = input("What day of the week is it? ").strip().lower()
time = input("What time of day is it? ").strip().lower()

invalid_time = (f"Sorry, {day} is not a valid input. I only recognize the time of day as 'morning', 'afternoon', 'evening' or 'night'.")

if day == "monday":
    if time == "morning":
        print("Gaze into the void while pretending coffee is a personality trait.")
    elif time == "afternoon":
        print("Question your life choices... but try to look productive.")
    elif time == "evening":
        print("Cook something healthy, healthy adjacent.. or just order something and call it self-care.")
    elif time == "night":
        print("Celebrate surviving another day of questionable decisions with Netflix and denial.")
    else:
        print(f"{invalid_time}")
elif day == "tuesday":
    if time == "morning":
        print("Breakfast is the perfect time for you to consider escaping to a cottage in the woods and living like a hermit.")
    elif time == "afternoon":
        print("Attend meetings and practice your professional nodding skills.")
    elif time == "evening":
        print("Finish your tasks before Future You has a reason to hate you.")
    elif time == "night":
        print("Recover from the day by staring dramatically at the ceiling.")
    else:
        print(f"{invalid_time}")
elif day == "wednesday":
    if time == "morning":
        print("Check your schedule and begin negotiating with reality.")
    elif time == "afternoon":
        print("Count the hours until freedom like a workplace prisoner.")
    elif time == "evening":
        print("Hydrate. Apparently that's important or something.")
    elif time == "night":
        print("Celebrate making it halfway through the week with a completely unnecessary snack.")
    else:
        print(f"{invalid_time}")
elif day == "thursday":
    if time == "morning":
        print("Look in the mirror and congratulate yourself for loading successfully.")
    elif time == "afternoon":
        print("Make a to-do list so you can avoid tasks more efficiently.")
    elif time == "evening":
        print("Try something new. Regret builds character.")
    elif time == "night":
        print("Have an existential crisis before bed. It's tradition.")
    else:
        print(f"{invalid_time}")
elif day == "friday":
    if time == "morning":
        print("Meditate to achieve inner peace. Immediately lose it when you check emails.")
    elif time == "afternoon":
        print("Go outside and confirm the sun still exists.")
    elif time == "evening":
        print("Learn a skill you'll abandon in three weeks.")
    elif time == "night":
        print("Pretend tomorrow is Friday. Enjoy the illusion.")
    else:
        print(f"{invalid_time}")
elif day == "saturday":
    if time == "morning":
        print("Rejoice. It is the weekend. You don't have to be anywhere, do you? Do you still have friends offline?")
    elif time == "afternoon":
        print("Exercise: because your body keeps sending bug reports.")
    elif time == "evening":
        print("Try something new. Regret builds character.")
    elif time == "night":
        print("Do absolutely nothing. You've earned the privilege of being useless for a while.")
    else:
        print(f"{invalid_time}")
elif day == "sunday":
    if time == "morning":
        print("Sleep in until your adulting responsibilities start filing complaints.")
    elif time == "afternoon":
        print("Clean something... unless you're still deluding yourself that the pile of dirty dishes is a 'modern art' exhibit.")
    elif time == "evening":
        print("Prepare for Monday by completely ignoring it exists.")
    elif time == "night":
        print("Now is the perfect time to remember a task you forgot to do because your brain was on 'Do Not Disturb' all weekend.")
    else:
        print(f"{invalid_time}")
else:
    print("The inputed day is invalid. Are you from this planet? I only recognize Earth weekdays.")

print("*~Throws confetti~*")

