import random

NUM_QUICK_PICKS = 5
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def generate_quick_picks(num_quick_picks):
    for _ in range(num_quick_picks):
        quick_pick = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_LINE)
        quick_pick.sort()
        print(" ".join(str(number).rjust(2) for number in quick_pick))

num_quick_picks = int(input("How many quick picks? "))
generate_quick_picks(num_quick_picks)