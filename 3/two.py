input_file = open('input.txt', 'r')
lines = list(map(lambda x: x.strip(), input_file.readlines()))

priorities = list(map(chr, range(ord('a'), ord('z')+1))) + list(map(chr, range(ord('A'), ord('Z')+1)))

group_size = 3

total_sum = 0

for i in range(0, len(lines), group_size):
  rucksacks = lines[i:(i + group_size)]
  mutual_char = next(iter(set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])))
  total_sum += (priorities.index(mutual_char) + 1)

print(total_sum)
