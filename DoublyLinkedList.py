class Node:
  def __init__(self,data):
    self.data = data
    self.prev = data 
    self.next = None

class DoublyLinkedList:
  def __init__(self):
      self.head = None 

  def insert_end(self,data):
      new_node = Node(data)

      if self.head is None:
          self.head = new_node
          return

      temp = self.head
      while temp.next is not None:
          temp = temp.next
      temp.next = new_node
      new_node.prev = temp

  def display_forward (self):
      temp = self.head
      while temp is not None:
          print(temp.data, end="<->")
          temp = temp.next
      print("none")     

  def display_backward(self):
      if self.head is None:
          print("list is empty")
          return
      
      temp = self.head
      while temp is not None:
           temp = temp.next
      while temp is not None:
           print(temp.data,end="<->")
           temp = temp.prev

      print("None")
  

dll = DoublyLinkedList()
dll.insert_end(30)
dll.insert_end(60)
dll.insert_end(90)
dll.insert_end(120)
dll.display_forward()
dll.display_backward()




          