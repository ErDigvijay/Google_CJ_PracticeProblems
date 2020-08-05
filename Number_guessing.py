import sys


def Guess(lower_end, upper_end, max_tries):
    tries = 0
    while (tries <= max_tries):

        guess = (lower_end + upper_end) // 2

        print(guess)
        sys.stdout.flush()
        s = str(input())

        if s == "TOO_BIG":
            upper_end = guess
        elif s == "TOO_SMALL":
            lower_end = guess + 1
        elif s == "CORRECT":
            break
        elif s == "WRONG_ANSWER":
            return 0
        tries += 1
    return


t = int(input()) 
for i in range(t):
    l = list(map(int, input().split()))
    a = l[0]
    b = l[1]
    n = int(input())
    Guess(a, b, n)
