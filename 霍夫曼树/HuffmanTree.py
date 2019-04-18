class HuffmanTreeNode:
    def __init__(self):
        self.name = None
        self.weight = 0
        self.left = None
        self.right = None
        self.encode = None

class HuffmanTree:
    def build_tree(self, nodes):
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.weight, reverse=True)
            node1 = nodes.pop()
            node2 = nodes.pop()
            new_node = HuffmanTreeNode()
            new_node.weight = node1.weight + node2.weight
            new_node.left = node1
            new_node.right = node2
            nodes.append(new_node)
        return nodes[0]

    def show_tree(self, node):
        stack = [node]
        res = []
        while stack:
            cur_node = stack.pop()
            res.append([cur_node.weight, cur_node.name])
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        print(res)


if __name__ == '__main__':
    words = [
        ["a", 1], ["b", 2], ["c", 5], ["d", 7],
    ]

    nodes = []
    for word in words:
        cur_node = HuffmanTreeNode()
        cur_node.name = word[0]
        cur_node.weight = word[1]
        nodes.append(cur_node)
    h = HuffmanTree()
    root = h.build_tree(nodes)
    h.show_tree(root)
"""
output:
[[15, None], [7, 'd'], [8, None], [3, None], [1, 'a'], [2, 'b'], [5, 'c']]
"""
