'''
You're playing Battleship on a grid of cells with R rows and C columns. There are 0 or more battleships on the grid, each occupying a single distinct cell. The cell in the ith row from the top and jth column from the left either contains a battleship (G_{i,j} = 1) or doesn't (G_{i,j} = 0).

You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random from the R*C possible cells. You're interested in the probability that the cell hit by your shot contains a battleship.

Your task is to implement the function getHitProbability(R, C, G) which returns this probability.

Note: Your return value must have an absolute or relative error of at most 10^{-6}10^-6 to be considered correct.
'''

from typing import List
# Write any import statements here


def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    total = 0.0

    for ship in G:
        total += sum(ship)

    return total / (R * C)
