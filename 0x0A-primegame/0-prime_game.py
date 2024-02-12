#!/usr/bin/python3
"""Prime Game Module"""


def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner of each round"""
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = [i for i in range(1, n + 1) if is_prime(i)]

        # Maria always starts first
        maria_turn = True
        while primes:
            max_prime = max(primes)
            primes = [p for p in primes if p % max_prime != 0]

            if maria_turn:
                wins["Maria"] += 1
            else:
                wins["Ben"] += 1

            maria_turn = not maria_turn

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
