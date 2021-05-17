def score(rolls: str):
    prev_current_next_nextagain = list(zip("0" + rolls[:-1], rolls[0:10], rolls[1:]+"0", rolls[2:]+"00"))

    score = 0
    for prev_roll, current_roll, next_roll, next_again_roll in prev_current_next_nextagain:
        if current_roll == 'X':
            score += _score(current_roll) + _score(next_roll) + _score(next_again_roll)
        elif current_roll == '/':
            score += 10 - _score(prev_roll) + _score(next_roll)
        else:
            score += _score(current_roll)

    return score

def _score(roll: str):
    if roll == 'X':
        return 10
    else:
        return int(roll)



