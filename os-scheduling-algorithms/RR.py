def waitTime(n, bt, wt, quantum):
    rem_bt = [0] * n
    t = 0

    for i in range(n):
        rem_bt[i] = bt[i]

    while (1):
        done = True

        for i in range(n):
            if (rem_bt[i] > 0):
                done = False
                if (rem_bt[i] > quantum):
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if (done == True):
            break

def findavgTime(n, bt, quantum):
    wt = [0] * n
    waitTime(n, bt, wt, quantum)
    total_wt = 0

    for i in range(n):
        total_wt = total_wt + wt[i]
    print("\nAverage waiting time = %.3f " % (total_wt / n))


burst_time = [24, 3, 3]
n = len(burst_time)
quantum = 1
findavgTime(n, burst_time, quantum)
