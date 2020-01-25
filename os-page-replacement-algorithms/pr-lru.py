def lru(pages, n, pframe):
    x = 0
    page_faults = 0
    page_hits = 0
    page = []
    for i in range(pframe):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(pframe):
            if(page[j] == pages[i]):
                flag = 1
                break
        if (flag == 0):
            if (page[x] != -1):
                min = 999
                for k in range(pframe):
                    flag = 0
                    j = i
                    while j>0:
                        j -= 1
                        if (page[k] == pages[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k
            page[x] = pages[i]
            x = (x + 1) % pframe
            page_faults += 1
        else:
            page_hits += 1

    print ("page faults : %d." % (page_faults - pframe), "\npage hits : %d." % (page_hits))


pages = input().split()
n = len(pages)
for i in range(n):
    pages[i] = int(pages[i])

pframe = int(input())

(lru(pages, n, pframe))