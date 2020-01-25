def waitTime(processes, n, a, w, ser):
    w[0] = 0
    ser[0] = 0
    for i in range(1, n):
        ser[i] = ser[i-1] + processes[i - 1]
    for i in range(1, n):
        w[i] = ser[i] - a[i]


def avgTime( processes, n, a): 
    w = [0] * n
    ser = [0] * n
    total_w = 0
    waitTime(processes, n, a, w, ser)
  
    print("Processes Arrival time " + " Waiting time ")

    for i in range(n): 
        total_w = total_w + w[i]
        print(str(i + 1) + "\t\t" + "\t\t" + str(a[i]) + "\t " + "\t\t" + str(w[i]) + "\t\t ")
    print("Avg waiting time = "+ str(total_w / n))


processes = [4, 10, 9, 6]
n = len(processes)
ar_time = [0, 1, 2, 3]
avgTime(processes, n, ar_time) 
