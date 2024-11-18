from collections import namedtuple
from itertools import combinations
from math import sqrt
import math

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

def minimum_distance_squared_efficient(points):
    # Sort the points by x and y coordinates
    points.sort(key=lambda p: (p[0], p[1]))

    def distance(p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    def closest_pair_recursive(points):
        if len(points) <= 3:
            return min(
            (distance(points[i], points[j]) for i in range(len(points)) for j in range(i + 1, len(points))),
            default=float('inf')
        )
        
        mid = len(points) // 2
        mid_x = points[mid][0]

        left_half = points[:mid]
        right_half = points[mid:]

        d1 = closest_pair_recursive(left_half)
        d2 = closest_pair_recursive(right_half)

        d = min(d1, d2)

        strip = [p for p in points if abs(p[0] -mid_x) < d]
        strip.sort(key=lambda p: p[1]) # sort by y coordinate

        min_d_strip = d
        for i in range(len(strip)):
            for j in range(i+1, len(strip)):
                if strip[j][1] - strip[i][1] >= d:
                    break
                min_d_strip = min(min_d_strip, distance(strip[i], strip[j]))

        return min(d, min_d_strip)
    
    return closest_pair_recursive(points)

if __name__ == '__main__':
    """
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
    """
    n = int(input().strip())
    points = [tuple(map(int, input().strip().split())) for _ in range(n)]

    result = minimum_distance_squared_efficient(points)
    print(f"{result:.9f}")
