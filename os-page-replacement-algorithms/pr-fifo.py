from queue import Queue

def fifo(pages, n, pframe):
    s = set()
    indexes = Queue()
    page_faults = 0
    page_hits = 0
    for i in range(n):
        if (len(s)<pframe):
            if (pages[i] not in s):
                s.add(pages[i])
                indexes.put(pages[i])
            else:
                page_hits += 1
        else:
            if (pages[i] not in s):
                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1
            else:
                page_hits += 1
    print("page faults : %d." % (page_faults), "\npage hits : %d." % (page_hits))

pages = input().split()
n = len(pages)
for i in range(n):
    pages[i] = int(pages[i])

pframe = int(input())

(fifo(pages, n, pframe))