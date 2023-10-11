def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []

    for name in names:
        badges.append(f"Hello, my name is {name}.") 
    return badges

def assign_rooms(names):
    welcome_messages = []

    for i, name in enumerate(names, start=1):
        welcome_messages.append(f"Hello, {name}! You'll be assigned to room {i}!")
    return welcome_messages

def printer(names):
    badges = batch_badge_creator(names)
    welcome_messages = assign_rooms(names)

    for badge in badges:
        print(badge)

    for message in welcome_messages:
        print(message)