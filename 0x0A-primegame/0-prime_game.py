#!/usr/bin/python3
"""
Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
"""


def generate_primes(n):
    """Generate a list of prime numbers up to n
    """
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes


def isWinner(x, nums):
    """Determine the winner of a prime game
    """
    max_num = max(nums)
    primes = generate_primes(max_num)
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        moves = [False] * (n + 1)
        moves[0] = moves[1] = True

        for p in primes:
            if p > n:
                break
            for i in range(p, n + 1, p):
                moves[i] = True

        # Count prime moves
        prime_moves = sum(moves)

        # Maria starts, so if the number of prime moves is odd, she wins
        if prime_moves % 2 == 1:
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1

    max_wins = max(wins.values())
    if wins["Maria"] == wins["Ben"]:
        return None
    return max(wins, key=wins.get)
