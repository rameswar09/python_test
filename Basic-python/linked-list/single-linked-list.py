class Node:
    def __init__(self, new_node_data):
        self.value = new_node_data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def insert_one(self, data):
        new_node = Node(data)
        cur = self.head

        if self.head is None:
            self.head = new_node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            print(self.head.value)
            print(cur.value)
            print('============================')

    def print_linked(self):
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next


l1 = linked_list()
l1.insert_one(12)
l1.insert_one(13)
l1.insert_one(30)
l1.print_linked()
