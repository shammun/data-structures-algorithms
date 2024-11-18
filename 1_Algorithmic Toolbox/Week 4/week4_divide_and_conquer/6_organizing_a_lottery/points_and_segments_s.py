
def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

def points_cover_efficient(starts, ends, points):
    assert len(starts) == len(ends)

    START, POINT, END = 'start', 'point', 'end'

    events = []
    point_indices = {p:i for i, p in enumerate(points)}

    # Add segment start and end
    for start, end in zip(starts, ends):
        events.append((start, START))
        events.append((end, END))

    # Add points
    for point in points:
        events.append((point, POINT))

    # Sort events
    events.sort(key=lambda x: (x[0], x[1]==START, x[1]==POINT))

    # Initialize active segments counter
    active_segments = 0
    point_counts = [0] * len(points)

    # Sweep line algorithm
    for event in events:
        position, event_type = event
        if event_type == START:
            active_segments += 1
        elif event_type == END:
            active_segments -= 1
        elif event_type == POINT:
            point_counts[point_indices[position]] = active_segments
    return point_counts

if __name__ == '__main__':
    n, m = map(int, input().split())
    starts, ends = [], []
    for _ in range(n):
        l, r = map(int, input().split())
        starts.append(l)
        ends.append(r)
    points = list(map(int, input().split()))

    result = points_cover_efficient(starts, ends, points)
    print(*result)
