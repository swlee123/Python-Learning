import time
import random
N = 10000000
TURN = 5

turn = TURN
average = 0
while turn:
    circle_points = 0
    square_points = 0
    interval = 0

    start = time.perf_counter()
    while interval < N:
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        distance = x**2 + y**2
        if distance <= 1:
            circle_points += 1

        square_points += 1
        interval += 1

    stop = time.perf_counter()
    time_in_s = stop-start
    average += time_in_s

    pie = 4.0*circle_points/square_points

    print(f"pie: {pie}")
    print('%.3f' % time_in_s)

    turn -= 1

average /= TURN
print("Average time : %.3f" % average)
print(f"N = {N}")












