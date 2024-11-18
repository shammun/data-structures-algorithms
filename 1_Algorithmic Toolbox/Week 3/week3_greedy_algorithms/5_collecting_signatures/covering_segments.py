from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

def optimal_points_efficient(segments):
    points = []
    # Sort segments by their end point in ascending order
    segments.sort(key=lambda x: x.end)
    # Initialize the current point to negative infinity
    current_point = float('-inf')
    for s in segments:
        # If the current point is not contained in the segment
        if current_point < s.start:
            # Add the end point of the segment to the points list
            points.append(s.end)
            # Update the current point to the end point of the segment
            current_point = s.end
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points_efficient(segments)
    print(len(points))
    print(*points)
