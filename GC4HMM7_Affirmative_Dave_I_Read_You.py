# 3 numbers

# N51 22. ((A-B) + B/C) ((A-B) + B/C) (B-C)
# E000 11. (A-B) (B- (B/C)) C

import pprint as pp

def satisfied(a, b, c) -> bool:
    r1 = 0 <= a - b <= 9
    r2 = b % c == 0
    r3 = 0 <= b - c <= 9

    c1 = (a-b + b//c)
    r4 = 0 <= c1 <= 9

    c2 = b - b // c
    r5 = 0 <= c2 <= 9

    r6 = 0 <= c <= 9
    return r1 and r2 and r3 and r4 and r5 and r6

def coords(a, b, c) -> tuple[int, int]:
    n1 = int(f'{a-b+b//c}{a-b+b//c}{b-c}')
    n2 = int(f'{a-b}{b-b//c}{c}')
    print(a, b, c, ':', n1, n2)
    return n1, n2

if __name__ == '__main__':
    candidates = []
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(1, 10):
                if satisfied(a, b, c):
                    candidate = coords(a, b, c)
                    candidates.append(candidate)

    pp.pprint(set(candidates))
    print(len(candidates), len(set(candidates)))