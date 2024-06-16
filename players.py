"""
here is a list of players that every one should give a prize to a random player
no one can give or receive prize twice and no one can give a prize to themselves
"""
import random

players = ['Fred', 'Wilima', 'Barney', 'Pebble', 'Bee Ban']
random_choices = players.copy()
out = []
received = {player: False for player in players}  # Initialize a dictionary to track received status

for p in players:
    possible_choices = [x for x in random_choices if x != p and not received[x]]
    if not possible_choices:
        raise ValueError("No valid choices available. There may be an issue with the logic.")

    ran = random.choice(possible_choices)
    received[ran] = True
    out.append([p, ran])
    random_choices.remove(ran)

print(out)
