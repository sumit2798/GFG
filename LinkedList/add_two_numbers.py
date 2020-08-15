def addSameSize(h1, h2, carry):
    if not h1:
        return

    sm = 0
    result = Node(sm)
    result.next = addSameSize(h1.next, h2.next, carry)

    sm = h1.data + h2.data + carry.data
    carry.data = sm // 10
    sm = sm % 10

    result.data = sm

    return result