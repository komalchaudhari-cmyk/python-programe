class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

      
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


sll = SinglyLinkedList()

sll.insert_end(30)
sll.insert_end(60)
sll.insert_end(90)
sll.display()
sll.delete_first()
sll.display()

