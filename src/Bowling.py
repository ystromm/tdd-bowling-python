def score(rolls: str):
    prev_current_next_nextagain = list(zip(" " + rolls[:-1], rolls, rolls[1:]+" ", rolls[2:]+"  "))

    score = 0
    for prev_roll, current_roll, next_roll, next_again_roll in prev_current_next_nextagain:
        if current_roll == 'X':
            score += 10 + int(next_roll) + int(next_again_roll)
        elif current_roll == '/':
            score += 10 - int(prev_roll) + int(next_roll)
        else:
            score += int(current_roll)

    return score
