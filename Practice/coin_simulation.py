import random


def coin():
    if random.randint(0, 1) == 1:
        return "heads"
    else:
        return "tails"


if __name__ == '__main__':
    heads_tally = 0
    tails_tally = 0
    count = 0
    for toss in range(10000):
        if coin() == "heads":
            heads_tally = heads_tally + 1
        elif coin() == "tails":
            tails_tally = tails_tally + 1
            break
        count = count + 1

    print(f"{heads_tally}   {tails_tally}      {count}")
