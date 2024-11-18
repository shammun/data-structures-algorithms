from sys import stdin

def min_refills(distance, tank, stops):
    current_position = 0
    num_refills = 0
    tank_curr = tank

    for stop in stops:
        distance = stop - current_position
        if distance > tank_curr:
            tank_curr += tank
            num_refills += 1
        if tank_curr + current_position >= stop:
            current_position = stop
            tank_curr -= distance
        else:
            return -1
        
if __name__ == "__main__":
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))