"""When can the monkey cross the river?

In this problem, a monkey is trying to jump across a certain 
distance across a river, using stones in the river to break its
jumps into sections.

However, the monkey can only jump N number of stones at a time.

As an added piece of complexity, the water level is decreasing 
with each hour, and as the water level gets lower, more stones 
emerge for the monkey to use to cross the river.

We can represent the `stones` in the river like this::

    [ 1, 2, 5, 0, 3, 4 ]

Where the number in the array corresponds to when the stone will 
emerge. (Bigger numbers are later in time.)

The stone times are **unique** -- numbers in
the list will never appear more than once.

So, for the above array, at time `t`, the stones would emerge as::

    t     river (* stone, - not yet a stone)
    -     ----------------------------------
    0     [ -  -  -  *  -  -  ]
    1     [ *  -  -  *  -  -  ]
    2     [ *  *  -  *  -  -  ]
    3     [ *  *  -  *  *  -  ]
    4     [ *  *  -  *  *  *  ]

Write a function that given the `stones` in the river as represented 
above, and the number of stones the monkey is able to jump, the earliest
time `t` that the monkey would be able to make it across the river.

For example::

    >>> earliest_arrival(3, [1, 2, 3, 0])
    1

    >>> earliest_arrival(2, [1, 2, 3, 0])
    2

    >>> earliest_arrival(3, [1, 4, 0, 2, 3, 5])
    2

    >>> earliest_arrival(5, [5, 2, 3, 8, 9, 99, 4, 0])
    3

"""

def available_stones(time, stones):
    """Given a list of times that the stones are available, return a list of True, 
    False for which stones are available at the given time.

    >>> stones = [1, 2, 5, 0, 3, 4]
    >>> available_stones(0, stones)
    [False, False, False, True, False, False]

    >>> available_stones(3, stones)
    [True, True, False, True, True, False]
    """

    new_stones = []

    for stone in stones:
        new_stones.append(stone <= time)

    return new_stones


def can_traverse(available, jump_distance):

    available.append(True)  # this represents the shore - we can always jump there

    next_stone = available.index(True)
    while next_stone < len(available):
        if next_stone < jump_distance:
            available = available[next_stone+1:]
            if True in available:
                next_stone = available.index(True)

        else:
            return False

    return True


def earliest_arrival(jump_distance, stones):
    """Find the earliest time a monkey can jump across a river."""

    latest = max(stones)

    for time in range(latest):
        available = available_stones(time, stones)
        if can_traverse(available, jump_distance):
            return time





if __name__ == "__main__":
    import doctest
    if not doctest.testmod().failed:
        print "\n*** ALL TESTS PASS; YOU MUST BE JUMPING WITH JOY\n"
