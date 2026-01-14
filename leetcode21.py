# =========================
# Definition for singly-linked list
# =========================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # value stored in this node
        self.next = next    # pointer to the next node


# =========================
# Helper: build linked list from Python list
# =========================
def build_list(arr):
    """
    Converts a Python list into a linked list.
    Example: [1,2,4] -> 1 -> 2 -> 4 -> None
    """
    dummy = ListNode()     # dummy head (doesn't count)
    curr = dummy

    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next     # real head


# =========================
# Helper: print linked list
# =========================
def print_list(head):
    """
    Prints the linked list in readable form.
    """
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# =========================
# Merge Two Sorted Lists (ITERATIVE)
# =========================
def mergeTwoLists(l1, l2):
    """
    Merges two sorted linked lists and returns the head.
    """

    # Dummy node simplifies edge cases (empty lists)
    dummy = ListNode()
    curr = dummy

    # Walk both lists while neither is exhausted
    while l1 and l2:

        # Compare current node values
        if l1.val <= l2.val:
            curr.next = l1      # point to l1 node
            l1 = l1.next       # move l1 forward
        else:
            curr.next = l2      # point to l2 node
            l2 = l2.next       # move l2 forward

        curr = curr.next        # advance merged list pointer

    # Attach remaining nodes (only one list can be non-empty)
    curr.next = l1 if l1 else l2

    return dummy.next           # head of merged list


# =========================
# TEST CASE (runs in Thonny)
# =========================
l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])

print("List 1:")
print_list(l1)

print("\nList 2:")
print_list(l2)

merged = mergeTwoLists(l1, l2)


print(merged)
