input_file = open('input.txt', 'r')
lines = input_file.readlines()

priorities = list(map(chr, range(ord('a'), ord('z')+1))) + list(map(chr, range(ord('A'), ord('Z')+1)))

total_sum = 0

for line in lines:
  contents = line.strip()

  mid_index = int(len(contents) / 2)
  mutual_char = next(iter(set(contents[:mid_index]) & set(contents[mid_index:])))

  total_sum += (priorities.index(mutual_char) + 1)

print(total_sum)
