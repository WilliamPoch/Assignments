def optimal(pages, n, pframe):
    page_faults = 0
    page_hits = 0
    page = []
    FREE = -1
    for a in range(pframe):
        page.append(FREE)
    for i in range(n):
        flag = 0
        for j in range(pframe):
            if page[j] == pages[i]:
                flag = 1
                break

        if flag == 0:

            faulted = False
            new_slot = FREE
            for q in range(pframe):
                if page[q] == FREE:
                    faulted = True
                    new_slot = q

            if not faulted:

                max_future = 0
                max_future_q = FREE
                for q in range(pframe):
                    if page[q] != FREE:
                        found = False
                        for x in range(n, i):
                            if pages[x] == page[q]:
                                found = True
                                if x > max_future:
                                    max_future = x
                                    max_future_q = q

                                break

                        if not found:
                            max_future_q = q
                            break

                faulted = True
                new_slot = max_future_q

            page_faults += 1
            page[new_slot] = pages[i]

        else:
            page_hits += 1
    print ("page faults : %d." % (page_faults - pframe), "\npage hits : %d." % (page_hits))


pages = input().split()
n = len(pages)
for i in range(n):
    pages[i] = int(pages[i])

pframe = int(input())

(optimal(pages, n, pframe))