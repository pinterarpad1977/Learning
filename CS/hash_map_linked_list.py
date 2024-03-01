from linked_list import LinkedList, Node
from blossom_lib import flower_definitions

class HashMap():
  def __init__(self, size):
    self.size = size
    self.array = [LinkedList() for i in range(self.size)]
    
  def hash(self, key):
    binary_key = key.encode()
    hash_code = sum(binary_key)
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.size

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    '''
    We can iterate through the linked list, because it has an iter method defined:
    def __iter__(self):
      current_node = self.head_node
      while(current_node):
        yield current_node.get_value()
        current_node = current_node.get_next_node()
    '''
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return
    list_at_array.insert(payload)


  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if key == item[0]:
        return item[1]
    return None
     
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('sunflower'))
