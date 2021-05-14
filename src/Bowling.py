def score(rolls: [int]):
    for roll in rolls:
        if roll < 0 or roll > 10:
            raise Exception()
    return sum(rolls)