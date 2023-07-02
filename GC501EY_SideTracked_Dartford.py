import pprint as pp
import math

# N51 26. (C+(A/A)  (A-B)  ((B+B)/C)
# E000 12. (C)  (B-(C+C)) (A-B)

def satisfied(a, b, c) -> bool:
    r1 = 0 <= c <= 9
    r2 = 0 <= (b - 2 * c) <= 9
    r3 = 0 <= (a - b) <= 9
    r4 = ((2 * b) % c) == 0
    r5 = 0 <= ((2 * b) // c) <= 9
    r6 = 0 <= (c + 1) <= 9
    return r1 and r2 and r3 and r4 and r5 and r6

def coords(a, b, c) -> tuple[int, int]:
    n1 = int(f'{c+1}{a-b}{(2*b)//c}')
    n2 = int(f'{c}{b-2*c}{a-b}')
    print(a, b, c, ':', n1, n2)
    return n1, n2

def distance(n1, n2) -> float:
    n1a = 26 + n1 / 1000
    n2a = 12 + n2 / 1000
    return math.sqrt((26.830 - n1a)**2 + (13.200 - n2a)**2)

if __name__ == '__main__':
    candidates_l = []
    for a in range(0, 20):
        for b in range(0, 20):
            for c in range(1, 20):
                if satisfied(a, b, c):
                    candidate = coords(a, b, c)
                    candidates_l.append(candidate)

    candidates = sorted(list(set(candidates_l)), key=lambda t: distance(*t))
    for candidate in candidates:
        print(candidate, distance(*candidate))