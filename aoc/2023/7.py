from collections import Counter
import aoc_api

day_input = aoc_api.get_input(7).strip()


def get_rank(hand):
    return max([
        [
            (1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)
        ].index(
            tuple(
                sorted(
                    Counter(hand.replace('J', r)).values())
            )
        )
        for r in '23456789TQKA'
    ]), ['J23456789T@QKA'.index(i) for i in hand]


list(print(
    sum(
        i * b + b for i, (_, b) in enumerate(
            sorted(
                (get_rank(hand.replace('J', r)), int(bid))
                for hand, bid in (
                    line.split() for line in day_input.splitlines()
                )
            )
        )
    )
) for r in '@J')


