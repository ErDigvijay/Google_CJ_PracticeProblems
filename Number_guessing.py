import sys, random


def Guess(low_end, high_end, max_tries):
    tries = 0
    while (tries <= max_tries):

        guess = (low_end + high_end) // 2

        print(guess)
        sys.stdout.flush()
        s = str(sys.stdin.readline())

        if s == "TOO_BIG":
            high_end = guess
        elif s == "TOO_SMALL":
            low_end = guess + 1
        elif s == "CORRECT":
            break
        elif s == "WRONG_ANSWER":
            return 0
        tries += 1
    return


t = int(input())
for i in range(t):
    l = list(map(int, (sys.stdin.readline()).split()))
    a = l[0]
    b = l[1]
    n = int(sys.stdin.readline())
    Guess(a, b, n)
Guess(a, b, n)