class Priority:
    def __init__(self, start, p,  finish):
        self.start = 0
        self.p = p
        self.finish = finish

def getKey(x):
  return x.p

def avgTime(list, n):
    for i in range(n):
        if i == 0:
            continue
        else:
            list[i].start = list[i-1].finish
            list[i].finish += list[i].start
    avg = 0
    for i in range(n):
        if i == 0:
            continue
        else:
            avg += list[i].start

    avg = avg/n

    print("\nAvg waiting time = %.3f "%(avg))

proc = [4, 10, 9, 6]
pri = [2, 1, 3 ,4]
list = []
n = len(proc)
for i in range(len(proc)):
    s = Priority(0, pri[i], proc[i])
    list.append(s)
list.sort(key = getKey)
avgTime(list, n)