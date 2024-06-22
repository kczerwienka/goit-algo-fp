class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("The previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        
        first = self.head
        second = first.next
        first.next = None
        third = second.next

        while second:
            
            second.next = first
            first = second
            second = third
            third = second.next if second else None
            
        self.head = first

        return None
    
    def insertion_sort(self):
        data_list = []
        current = self.head
        while current:
            data_list.append(current)
            current = current.next
        data_list.sort(key=lambda x: x.data)
        for item in data_list:
            self.delete_node(item.data)
        for item in data_list:
            self.insert_at_end(item.data)
        return None
    

def merge_two_lists(first, second):
    if first.head is None:
            first.head = second.head
    else:
        cur = first.head
        while cur.next:
            cur = cur.next
        cur.next = second.head
    return None

llist = LinkedList()
sllist = LinkedList()

# Insert the nodes into the end
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

sllist.insert_at_beginning(1)
sllist.insert_at_beginning(2)
sllist.insert_at_beginning(3)
sllist.insert_at_beginning(4)

# Insert the nodes into the end
llist.insert_at_end(20)
llist.insert_at_end(25)
llist.insert_at_end(26)
llist.insert_at_end(27)

# Printing a linked list
print("Linked list:")
llist.print_list()

# Delete a node
llist.delete_node(10)

print("\nThe linked list after deleting the node with data 10:")
llist.print_list()

# Searching for an item in a linked list
print("\nSearching for element 15:")
element = llist.search_element(15)
if element:
    print(element.data)

#Reversing list
print("Reversed list:")
llist.reverse_list()
llist.print_list()

#Sort list
print("Sorted list:")
llist.insertion_sort()
llist.print_list()

#Merge list
print("Merged list:")
merge_two_lists(llist,sllist)
llist.print_list()