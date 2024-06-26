class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    try:
      current_node = self.get_head_node()
      if current_node.get_value() == value_to_remove:
        self.head_node = current_node.get_next_node()
      else:
        while current_node:
          next_node = current_node.get_next_node()
          if next_node.get_value() == value_to_remove:
            current_node.set_next_node(next_node.get_next_node())
            current_node = None
          else:
            current_node = next_node
    except AttributeError:
      print(f'invalid value to remove -> {value_to_remove}')

  def remove_all_nodes(self, value_to_remove):
    try:
      prev_node = None
      current_node = self.get_head_node()
      while current_node:
        if current_node.get_value() == value_to_remove:
          if prev_node:
            prev_node.set_next_node(current_node.get_next_node())
          else:
            self.head_node = current_node.get_next_node()
          current_node = current_node.get_next_node()
        else:
          prev_node = current_node
          current_node = current_node.get_next_node()
    except AttributeError:
      print(f'invalid value to remove -> {value_to_remove}')


  def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}')
  
    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node
  
    if val1 == val2:
      print("Elements are the same - no swap needed")
      return
  
    while node1 is not None:
      if node1.get_value() == val1:
        break
      node1_prev = node1
      node1 = node1.get_next_node()
  
    while node2 is not None:
      if node2.get_value() == val2:
        break
      node2_prev = node2
      node2 = node2.get_next_node()
  
    if (node1 is None or node2 is None):
      print("Swap not possible - one or more element is not in the list")
      return
  
    if node1_prev is None:
      input_list.head_node = node2
    else:
      node1_prev.set_next_node(node2)
  
    if node2_prev is None:
      input_list.head_node = node1
    else:
      node2_prev.set_next_node(node1)
  
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)

  def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 1
    while tail_seeker:
      tail_seeker = tail_seeker.get_next_node()
      count += 1
      if count > n+1:
        if current is None:
          current = linked_list.head_node
        else:
          current = current.get_next_node()
    return current
  
  def generate_test_linked_list():
    linked_list = LinkedList()
    for i in range(50, 0, -1):
      linked_list.insert_beginning(i)
    return linked_list

  def find_middle(linked_list):
  slow = linked_list.head_node
  fast = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if fast:
      slow = slow.get_next_node()
      fast = fast.get_next_node()
  return slow


# Use this to test your code:
test_list = generate_test_linked_list(8)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)

ll = LinkedList.LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())
