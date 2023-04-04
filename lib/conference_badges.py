def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_list = []
    for name in names:
        badge = f"Hello, my name is {name}."
        badge_list.append(badge)
    return badge_list

def assign_rooms(names):
    room_assignmet = []
    for index, name in enumerate(names):
        room = index + 1
        message = f"Hello, {name}! You'll be assigned to room {room}!"
        room_assignmet.append(message)
    return room_assignmet

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for rooms in assign_rooms(names):
        print(rooms)