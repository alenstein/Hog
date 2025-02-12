# sample
def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """

    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'

    # BEGIN Question 1
    if num_rolls == 1 and dice() == 1:
        return 1
    else:
        rolls = [dice() for i in range(num_rolls)]
        if 1 in rolls:
            return 1
        return sum(rolls)

    # END Question 1