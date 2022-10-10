'''
There's a multiple-choice test with NN questions, numbered from 11 to NN. Each question has 22 answer options, labelled A and B. You know that the correct answer for the iith question is the iith character in the string CC, which is either "A" or "B", but you want to get a score of 00 on this test by answering every question incorrectly.

Your task is to implement the function getWrongAnswers(N, C) which returns a string with NN characters, the iith of which is the answer you should give for question ii in order to get it wrong (either "A" or "B").
'''


def getWrongAnswers(N: int, C: str) -> str:
    swap = ''

    for char in C:
        # If char is A add B to the list
        if char == 'A':
            swap += 'B'

        # If char is B add A to the list
        else:
            swap += 'A'

    return swap
