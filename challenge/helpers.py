from collections import Counter
from constants import *


def common_digit_count(guess, num):
    count_guess = Counter(guess)
    count_num = Counter(num)
    sum_ = 0
    seen = set()

    for s in guess:
        if s in num and s not in seen:
            sum_ += count_num[s] if count_guess[s] > count_num[s] else count_guess[s]
            seen.add(s)
    return sum_

        




