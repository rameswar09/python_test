class Node:
    def __init__(self, new_ele):
        self.key = new_ele
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_ele(self, new_ele):
        new_node = Node(new_ele)
        if(self.length == 0):
            self.head = new_node
        else:
            curr = self.head
            while(curr.next != None):
                curr = curr.next
            curr.next = new_node
        self.length += 1

    def add_ele_at_point(self, position, new_ele):
        new_node = Node(new_ele)
        curr = self.head
        while(curr.key != position):
            curr = curr.next
        temp = curr.next
        curr.next = new_node
        new_node.next = temp
        self.length += 1

    def delete_node(self, del_node):
        curr = self.head
        while(curr.next.key != del_node):
            curr = curr.next
        temp = curr.next.next
        curr.next = temp
        self.length -= 1

    def print(self):
        if self.length == 0:
            print("Linked list is empty")
        curr = self.head
        while(curr != None):
            print(curr.key)
            curr = curr.next

    def print_length(self):
        print(self.length)


l1 = Linked_list()
l1.add_ele(12)
l1.add_ele(13)
l1.add_ele(14)
l1.print()
l1.print_length()
print("=====================================")
l1.add_ele_at_point(13, 11)
l1.print()
l1.print_length()
print("=====================================")

l1.delete_node(13)
l1.print()
l1.print_length()
