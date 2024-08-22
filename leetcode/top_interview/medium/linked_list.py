class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


def print_lists(head, end='\n'):
    while head:
        print(head.data, end=' -> ' if head.next else '')
        head = head.next
        print(end=end)


def add_two_numbers(l1, l2):
    head = None
    tmp = None
    carry = 0

    while l1 is not None or l2 is not None:
        sum_value = carry

        if l1 is not None:
            sum_value += l1.data
            l1 = l1.next
        if l2 is not None:
            sum_value += l2.data
            l2 = l2.next

        node = Node(sum_value % 10)
        carry = sum_value // 10

        if tmp is None:
            tmp = head = node

        else:
            tmp.next = node
            tmp = tmp.next

    if carry > 0:
        tmp.next = Node(carry)
    print_lists(head, '')


def odd_even_linked(head: Node):
    odd = head
    even = head.next
    head_even = head.next

    while even is not None and even.next is not None:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = head_even
    print_lists(head)


def intersection_two_linked_list(headA, headB):
    stackA = []
    stackB = []

    while headA or headB:
        if headA:
            stackA.append(headA)
            headA = headA.next
        if headB:
            stackB.append(headB)
            headB = headB.next

    prev = None
    while stackA and stackB:
        nodeA = stackA.pop(-1)
        nodeB = stackB.pop(-1)

        if nodeA != nodeB:
            return prev
        prev = nodeA
