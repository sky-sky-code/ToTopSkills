import collections


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(data=value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def delete(self, value):
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        raise Exception

    def remove_id_node(self, id):
        current_id = 0
        current_node = self.head
        if current_id == id:
            self.head = current_node.next
            return
        while current_node.next is not None:
            if current_id + 1 == id:
                current_node.next = current_node.next.next
            current_id += 1
            current_node = current_node.next
        raise Exception

    def print_lists(self, end='\n'):
        while self.head:
            print(self.head.data, end=' -> ' if self.head.next else '')
            head = self.head.next
            print(end=end)


# head = Node(1, Node(2, Node(3, Node(4))))

def print_lists(head, end='\n'):
    while head:
        print(head.data, end=' -> ' if head.next else '')
        head = head.next
        print(end=end)


# Delete node in Linked

def delete_node(head, data):
    current = head
    following = current.next

    while following:
        if following.data == data:
            current.next = following.next
            break
        current = following
        following = following.next
    print_lists(head)


# Reverse Linked

def reverse_linked(head):
    previous = None
    current = head
    following = current.next

    while current:
        current.next = previous
        previous = current
        current = following
        if following:
            following = following.next
    return previous


# Merge Linked

def merge_linked(head1, head2):
    s = t = Node()
    while not (head1 is None or head2 is None):
        if head1.data <= head2.data:
            current = head1
            head1 = head1.next
        else:
            current = head2
            head2 = head2.next

        t.next = current
        t = t.next
    t.next = head1 or head2
    return s.next


def merge_linked_v2(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if h1.data < h2.data:
        h1.next = merge_linked_v2(h1.next, h2)
        return h1
    else:
        h2.next = merge_linked_v2(h2.next, h1)
        return h2


def merge_linked_v3(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if h1.data < h2.data:
        h1.next = merge_linked_v3(h1.next, h2)
        return h1
    else:
        h2.next = merge_linked_v2(h2.next, h1)
        return h2


# Polidrom Linked

def palindrome_linked_list(head):
    if head.next is None:
        return True

    counter = {}
    index = 1
    current = head

    while current:
        counter[index] = current.data
        current = current.next
        index += 1

    mid = index // 2 if index != 1 else 1

    for idx, key in enumerate(reversed(counter.keys())):
        if idx == mid:
            return True
        if counter[idx + 1] != counter[key]:
            return False


def palindrome_linked_list_v2(head):
    slow = head

    stack = []

    ispalin = True

    while slow != None:
        stack.append(slow.data)
        slow = slow.next

    while head is not None:
        i = stack.pop()
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break

        # Move ahead
        head = head.next

    return ispalin


def polidrome_linked_list_v3(head):
    slow = head
    fast = head
    while fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    prev = None
    current = slow
    following = slow.next
    while current:
        current.next = prev
        prev = current
        current = following
        if following:
            following = following.next
    while prev:
        if prev.data != head.data:
            return False
        prev = prev.next
        head = head.next
    return True


# Linked list Cycle

def linked_list_cycle(head):
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return True
    return False

