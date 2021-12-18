class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode, l2:ListNode):
    """
    Solve by recursive call
    - base case -> if l1 is null return l2 and viceversa
    - if l1.val < l2.val call the function recursively and assign 
    l1.next to the call else l2.next
    """
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    if l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2