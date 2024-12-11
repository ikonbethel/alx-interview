#!/usr/bin/python3
'''Prime Game'''


def isPrime(num: int) -> bool:
    """
    Checks if a number is prime.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.

    The function uses the square root of the number
    to reduce the number of iterations in the loop.
    It checks divisibility only up to the square root
    of the number, as any factor larger than the square root
    would have a corresponding factor smaller
    than the square root.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    numSqrt = int(num ** (0.5)) + 1
    for i in range(5, numSqrt, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def findNextPrime(set: list) -> int:
    """
    Finds the next prime number in a given set.

    Parameters:
    set (set): A set of integers.

    Returns:
    int: The next prime number in the set.
         If no prime number is found,
         returns None.

    The function iterates through each element in the set.
    For each element, it checks if it is greater than 1
    and a prime number.
    If a prime number is found, it is returned immediately.
    If no prime number is found after iterating through all elements,
    None is returned.
    """
    for element in set:
        if element > 1 and isPrime(element):
            return element
    return None


def containsPrime(set: list) -> bool:
    """
    Checks if a set contains any prime numbers.

    Parameters:
    set (set): The set of numbers to check.

    Returns:
    bool: True if the set contains at least one prime number,
          False otherwise.
    """
    for element in set:
        if element > 1 and isPrime(element):
            return True
    return False


def isWinner(x: int, nums: list) -> str:
    """
    Determines the winner of a prime game.

    The game involves two players, Ben and Maria,
    who take turns removing prime numbers from a set of numbers.
    The game continues until there are no prime numbers left
    in the set. The player with the most prime numbers removed wins.

    Parameters:
    x (int): The number of rounds in the game.
    nums (list): A list of integers representing the upper limit
                 for each round's set of numbers.

    Returns:
    str: The name of the winner ('Ben' or 'Maria').
         If there is no winner (e.g., no rounds played),
         returns None.

    """
    if not nums or len(nums) < 1 or not x or x < 1:
        return None

    benWins, MariaWins = 0, 0

    try:
        for i in range(x):
            currentSet = list(range(1, nums[i] + 1))
            turns = 3  # Chose odd number to properly count turns
            # print(f'Round {i + 1}')

            while containsPrime(currentSet):
                # print(f'Maria\'s Turn' if turns % 2 else 'Ben\'s Turn')
                # print('Current Set:', currentSet)

                currentPrime = findNextPrime(currentSet)

                if currentPrime:
                    # print(f'{'Maria' if turns % 2 else 'Ben'} '
                    #       f'removing {currentPrime} and its multiples')
                    currentSet.remove(currentPrime)
                    currentSet = [num for num in currentSet
                                  if num % currentPrime != 0]
                turns += 1

            if turns % 2 == 0:
                MariaWins += 1
                # print(f'Maria wins round {i + 1}')
            else:
                benWins += 1
                # print(f'Ben wins round {i + 1}')
            # print(f'Score: Maria {MariaWins} vs {benWins} Ben')
        if MariaWins > benWins:
            return 'Maria'
        elif benWins > MariaWins:
            return 'Ben'

        return None
    except IndexError:
        pass
