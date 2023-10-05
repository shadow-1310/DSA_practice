#this is the final working solution on GFG testcases
#main problem is in some input cases there some trailing zeroes, so we have to remove those before getting legth of the numbers
#one other problem is linked lists are given in forward direction, so we have to reverse then do the calculation then again return the final output in forward direction
#before returning we have to remove the trailing zeroes
def subLinkedList(l1, l2):
    def reverse(node):
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev
    
    def length(node):
        count = 0
        while node:
            node = node.next
            count += 1
            
        return count

    while l1 and l1.data == 0:
        l1 = l1.next

    while l2 and l2.data == 0:
        l2 = l2.next
        
    n1 = length(l1)
    n2 = length(l2)
    
    if n1 > n2:
        big = l1
        small = l2
    elif n1 < n2:
        big = l2
        small = l1

    else:
        t1 = l1
        t2 = l2
        while t1.data == t2.data:
            t1 = t1.next
            t2 = t2.next

            if not t1:
                return Node(0)

        if t1.data > t2.data:
            big = l1
            small = l2

        elif t1.data < t2.data:
            big = l2
            small = l1
            
    big = reverse(big)
    small = reverse(small)


    dummy = Node(0)
    curr = dummy
    borrow = False
    while big or small:
        v1 = big.data if big else 0
        v2 = small.data if small else 0
        if borrow:
            v1 -= 1
            borrow = False
        if v2 > v1:
            borrow = True
            v1 += 10

        v3 = v1 - v2
        curr.next = Node(v3)
        curr = curr.next
        big = big.next
        small = small.next if small else small
        
    res = reverse(dummy.next)
    while res and res.data == 0:
        res = res.next
    return res


