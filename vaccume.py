import random as rand
import time

def room_clean(n):
    env = [[rand.randint(0, 1) for _ in range(n)] for _ in range(n)]
    performance_count = 0
    for i in range(len(env)):
        for j in range(len(env[i])):
            print(env[i][j], end=" ")
        print()
    stime = time.time()
    for i in range(len(env)):
        for j in range(len(env[i])):
            if env[i][j] == 1:
                performance_count += 1
                env[i][j] = 0
    etime = time.time()
    performance = (performance_count / n ** 2) * 100
    print(f"performance is: {performance}")
    print(f"Time taken is {etime - stime}")
    for i in range(len(env)):
        for j in range(len(env[i])):
            print(env[i][j], end=" ")
        print()

