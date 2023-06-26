# Read about Donald michie, computer science creator of the memo functions 

from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1} # default cases

def fib_mem(n: int) -> int:

    if n not in memo:
        memo[n] = fib_mem(n - 1) + (n - 2)

    return memo[n]

if __name__=='__main__':
    print(fib_mem(50))

