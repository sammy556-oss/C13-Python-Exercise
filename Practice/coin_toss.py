import random


def coin():
    if random.randint(0,1) == 1:
        return "heads"
    else:
        return "tails"


heads_tally = 0
tails_tally = 0

for toss in range(10000):
    if coin() == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

print(f"{heads_tally}\n {tails_tally}")
