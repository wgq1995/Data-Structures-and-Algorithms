class Node:
    """
    链表结点类
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(val_list):
    """
    从一个列表按顺序建立链表，返回头结点
    :param val_list: list，存Node中的值
    :return: Node, 头结点
    """
    if not val_list:
        return None
    head_node = Node(0)
    cur = head_node
    for val in val_list:
        cur.next = Node(val)
        cur = cur.next
    return head_node.next


def show_linked_list(head):
    """
    按顺序显示链表
    :param head: Node, 头结点
    :return: list, 依次为每个node中的val
    """
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def reverse_linked_list(head):
    """
    反转链表
    :param head:Node, 头结点
    :return: Node，反转后的头结点
    """
    if not head:
        return None
    pre = None
    cur = head
    nex = head.next
    while nex:
        cur.next = pre
        pre = cur
        cur = nex
        nex = cur.next
    cur.next = pre
    return cur


if __name__ == '__main__':
    a = [1, 3, 5, 2, 7]
    head = build_linked_list(a)
    res = show_linked_list(head)
    print("原链表", res)
    reversed_head = reverse_linked_list(head)
    reversed_res = show_linked_list(reversed_head)
    print("反转链表", reversed_res)
    # 运行结果为
    # 原链表[1, 3, 5, 2, 7]
    # 反转链表[7, 2, 5, 3, 1]
