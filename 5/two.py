input_file = open('input.txt', 'r')
lines = list(map(lambda x: x.strip(), input_file.readlines()))

crates = []
instructions = []

flipped = False

for line in lines:
  if line == '':
    flipped = True
  elif flipped:
    instructions.append(line)
  else:
    crates.append(line)

crates.reverse()

crates_width = int(crates[0][-1])

del crates[0]

crates_height = len(crates)

stacks = []

for i in range(-1, crates_height):
  for j in range(0, crates_width):
    if i == -1:
      stacks.append([])
    else:
      start_location = j * 4
      crate = crates[i][start_location:start_location + 3][1:2]
      if crate != ' ' and crate != '':
        stacks[j].append(crate)

for instruction in instructions:
  parsed_instruction = instruction.split(' ')

  amount = int(parsed_instruction[1])
  origin = int(parsed_instruction[3]) - 1
  destination = int(parsed_instruction[5]) - 1

  stack_to_move = stacks[origin][-amount:]

  del stacks[origin][-amount:]

  stacks[destination].extend(stack_to_move)

top_items = ''

for stack in stacks:
  top_items += stack[-1]

print(top_items)
