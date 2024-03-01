# stack must be created or imported
# stack was given a print_items method!

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack('Left')
right_stack = Stack('Right')
middle_stack = Stack('Middle')

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = 0
while num_disks < 3:
  num_disks = int(input("\nHow many disks do you want to play with?\n"))

for disk in range(num_disks,0, -1):
  left_stack.push(disk)

num_optimal_moves = 2**(num_disks-1)
print(f'\nThe fastest you can solve this game is in {num_optimal_moves} moves')

def get_input():
  choices = [stack.get_name()[0].upper() for stack in stacks]
  while True:
    for i in range(len(stacks)):
      print(f'Enter {choices[i]} for {stacks[i].get_name()}')
    user_input = input(' ').upper()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

#Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n... Current Stacks...")
  for stack in stacks:
    stack.print_items()

  while True:
    print("Which stack do you want to move from?\n")
    from_stack = get_input()
    print("Which stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print('Invalid Move. Try Again!')
    elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
      print(to_stack.is_empty())
      disk = from_stack.pop()
      num_user_moves += 1
      to_stack.push(disk)
      break
    else:
      print('Invalid Move. Try Again!')

print(f'You completed the game in {num_user_moves} and the optimal number of moves is {num_optimal_moves}')
