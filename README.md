# tdd-bowling-python
Bowling scoring TDD kata

## Test Driven Development

- Write a failing test
- Make the test pass in a simple way
- Refactor
- Start over

## Requirements for bowling scoring

A game is made up of 10 frames.
Each frame has 10 pins and is reset each frame.
A frame can be one or two rolls, depending on:
1. A strike (knocking all 10 pins down on the first roll of the frame) ends the frame.
2. Any number below 10 on the first roll allows a second roll.
The final (or running) score is the sum of all frames where:
1. A strike is 10 points + the next two rolls.
2. A spare is 10 points + the next roll.
3. Anything else is 1 point per pin cleared in each roll.
If a spare is thrown in the final (10th) frame the player is awarded one more roll. This roll awards the number of pins cleared onto their score (0 to 10 bonus points).

Copied from https://elliotchance.medium.com/kata-the-bowling-game-my-first-attempt-6fce18a85270.


## Fluent assertions

```python
assert_that("a"+"bcd").is_not_empty().contains("a").contains("bc")
```
## 

The input is given as a string with numbers '0' through '9' and characters '/' and 'X'. 

If the first roll of a frame knocks down 0 to 9 pins the input is '0', '1', up to '9'.

If the second roll knocks down all remaining pins this is denoted by '/'. Otherwise the number of pins is given.

If all pins are knocked down in the first roll, a strike, this is denoted by 'X'.

## Examples

- A game with all misses receives a score of 0.

```python
"0"*20
```

- If the first roll knocks down 1 pin the score should be 1.

```python
"1"+"0"*19
```

- If all rolls knocks down 1 pin the score should be 20.

```python
"1"*20
```

- If the first 9 rolls knocks down one more pin each roll the score should be 45.

```python
"0123456789"+"0"*10
```

- A strike in the first roll followed by misses should get 10.

```python
"X"+"0"*18
```

- One pin knocked down and a spare followed by misses should get 10.

```python
"1/"+"0"*18
```

- Two pins and a spare in the first frame followed by misses should get 10.

```python
"2/"+"0"*18
```

- Two pins and a spare followed by one pin should get bonus 12.

```python
"2/1"+"0"*17
```

- Strike should get bonus from the two following, 16.

```python
"X21"+"0"*16
```

Two strikes should get 30:

```python
"XX"+ "0"*16
```

A spare at the end should get one bonus roll, 11.

```python
"0"*18+"1/1"
```

A strike at the end should get two bonus rolls, 13.

```python
"0"*18+"X12"
```

All strikes should get 300:

```python
"X"*12
```

## Bonus Examples

Strange characters:
```python
"1a"+"0"*18
```

Missing bonus rounds:

```python
"X"*10
```

