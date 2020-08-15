def copyList(head):
    d = dict()
    if not head:
        return

    ch = Node(head.data)
    chh = ch

    d[head] = ch

    h = head.next

    while h:
        nn = Node(h.data)
        chh.next = nn
        d[h] = nn

        h = h.next
        chh = nn

    h = head

    chh = ch

    while h:
        if h.arb:
            chh.arb = d[h.arb]
        h = h.next
        chh = chh.next

    return ch