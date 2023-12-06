
test_input = """
Time:      7  15   30
Distance:  9  40  200
"""

test_input = """
Time:        40     82     84     92
Distance:   233   1011   1110   1487
"""

test_input = test_input.strip()
times = [time for time in test_input.splitlines()[0].split(" ")[1:] if time != '']
times = [int(time) for time in times]
distances = [distance for distance in test_input.splitlines()[1].split(" ")[1:] if distance != '']
distances = [int(distance) for distance in distances]

def distance_for_hold(time_hold: int, race_time: int)-> int:
    # print(f"Time hold: {time_hold}")
    # print(f"race time {race_time}")
    if time_hold == 0:
        return 0
    else:
        return time_hold * (race_time - time_hold)
        
        

def winning_distance(time: int, distance: int) -> int:
    lower_bound = 0
    upper_bound = time
    won = False
    while not won:
        lower_bound += 1
        curr_distance = distance_for_hold(lower_bound, time)
        # print(f"curr_distance {curr_distance}")
        # print(f"distance {distance}")
        if curr_distance > distance:
            print("won")
            won = True

    won = False
    while not won:
        upper_bound -= 1
        curr_distance = distance_for_hold(upper_bound, time)
        if curr_distance > distance:
            won = True
    print(f"lower_bound {lower_bound}")
    print(f"upper_bound {upper_bound}")
    return upper_bound - lower_bound + 1
    
winning_distances = []

for idx, time in enumerate(times):
    print(f"Time: {time} Distance: {distances[idx]}")
    curr = winning_distance(time, distances[idx])
    print(f"Distance: {curr}")
    winning_distances.append(curr)

    
sum = 1
for curr in winning_distances:
    sum *= curr
print(sum)
