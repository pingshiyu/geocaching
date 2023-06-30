import math
import pprint as pp

# ABE
ABE = [(3, 2, 6), (4, 2, 8), (3, 3, 9), (4, 3, 12)]
# E + 2C = 10, 11, 12    ==>   C = (10-E)/2, (11-E)/2, (12-E)/2
# C <= D <= E - C

# find closest to published coords
def distance_to_published(tup: tuple[float, float]) -> float:
    published = (25.100, 11.000)
    return math.sqrt((tup[0] - published[0])**2 + (tup[1] - published[1])**2)

if __name__ == '__main__':
    sols = []

    for a, b, e in ABE:
        # find what C should be
        c = (10-e)//2
        while (e + 2*c <= 12):
            # find what D should be
            for d in range(c, e-c+1):
                if (d-c) > 9 or (e-d-c) > 9:
                    continue
                # print(f"{a=} {b=} {c=} {d=} {e=}")
                sol = (float(f"25.{a-b}{a}{e-d-c}"), float(f"{e+2*c}.{d-c}{e//b}{e//a}"))
                # print(f"25.{a-b}{a}{e-d-c} {e+2*c}.{d-c}{e//b}{e//a}") # distance: {distance_to_published(sol)}")
                sols.append(sol)
                pass
            c += 1
    
    for sol in sorted(sols, key=distance_to_published):
        print(sol, f"distance: {distance_to_published(sol)}")