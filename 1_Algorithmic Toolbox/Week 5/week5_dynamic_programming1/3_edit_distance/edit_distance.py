def edit_distance(first_string, second_string):
    s1_len = len(first_string)
    s2_len = len(second_string)

    # Create a 2D array of size (s1_len + 1) x (s2_len + 1)
    distance = [[0 for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]

    for i in range(s1_len + 1):
        distance[i][0] = i
    
    for j in range(s2_len + 1):
        distance[0][j] = j

    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            insertion = distance[i][j - 1] + 1
            deletion = distance[i - 1][j] + 1
            match = distance[i - 1][j - 1]
            mismatch = distance[i - 1][j - 1] + 1
            if first_string[i-1] == second_string[j-1]:
                distance[i][j] = min(insertion, deletion, match)
            else:
                distance[i][j] = min(insertion, deletion, mismatch)
            # print(distance)
    return distance[s1_len][s2_len]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
