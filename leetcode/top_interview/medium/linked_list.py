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


"""
Полиндромный Linked List
"""


# 1 варинат использование списка

def is_palindrome_help_list(head):
    list_vals = []

    while head:
        list_vals.append(head.data)
        head = head.next

    left, right = 0, len(list_vals) - 1

    while left < right and list_vals[left] == list_vals[right]:
        left += 1
        right -= 1
    return left >= right


# 2 вариант

def is_palindrome_help_stack(head):
    stack = []
    while head:
        stack.append(head.data)
        head = head.next
    curr = head
    while curr and curr.data == stack.pop():
        curr = curr.next
    return curr is None


# 3 вариант

def reverse(head):
    curr = head
    prev = None
    while curr:
        next_curr = curr.next
        curr.next = prev
        prev = curr
        curr = next_curr
    return prev


def is_palindrome_help_linked_help(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    reverse_head = reverse(slow)
    while reverse_head:
        if reverse_head.data != head.data:
            return False
        reverse_head = reverse_head.next
        head = head.next
    return True


def delete_duplicates(head):
    curr = head
    while head.next is not None:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next
    arr = []
    while curr:
        arr.append(curr.data)
        curr = curr.next
    print(arr)


def get_interaction_node(headA, headB):
    stackA = []
    stackB = []

    while headA or headB:
        if headA:
            stackA.append(headA)
            headA = headA.next
        else:
            stackB.append(headB)
            headB = headB.next

    curr_node = None
    while stackA and stackB:
        a_node = stackA.pop()
        b_node = stackB.pop()
        if a_node is b_node:
            curr_node = a_node
    return curr_node


def remove_element(head, val):
    prev = Node(0, head)

    def recursion(prev, curr):
        if curr is None:
            return
        if curr.data == val:
            prev.next = curr.next
        else:
            prev = prev.next
        return recursion(prev, curr.next)

    recursion(prev, prev.next)
    return prev.next


def is_palindrome(head):
    curr = head
    fast = head
    while head.next is not None:
        curr = curr.next
        fast = fast.next.next
    reverse_head = reverse(curr)

    while head.next is not None:
        if head.data != reverse_head.data:
            return False
        curr = curr.next
        reverse_head = reverse_head.next
    return True


def middle(head):
    curr = head
    fast = head
    while fast and fast.next:
        curr = curr.next
        fast = fast.next.next
    return curr


def merge_two_lists(list1, list2):
    result = None
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.data <= list2.data:
        result = list2
        result.next = merge_two_lists(list1.next, list2)
    else:
        result = list1
        result.next = merge_two_lists(list1, list2.next)
    return result


def merge_two_lists_iterative(list1, list2):
    head = None
    tail = None
    if list1.data <= list2.data:
        head = tail = list1
        list1 = list1.next
    else:
        head = tail = list2
        list2 = list2.next
    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            tail = list1
            list1 = list1.next
        else:
            tail.next = list2
            tail = list2
            list2 = list2.next
    return head


def add_two_numbers(list1, list2):
    dummy = Node()
    res = dummy
    total = carry = 0
    while list1 and list2 or carry:
        total = carry

        if list1:
            total += list1.data
            list1 = list1.next
        if list2:
            total += list2.data
            list2 = list2.next

        num = total % 10
        carry = total // 10
        dummy.next = Node(num)
        dummy = dummy.next

    return res.next

