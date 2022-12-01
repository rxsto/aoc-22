elf_cals = []

input_file = open('input.txt', 'r')
lines = input_file.readlines()

acc = 0

for line in lines:
  if line == '\n':
    elf_cals.append(acc)
    acc = 0
  else:
    acc += int(line)

elf_cals.sort(reverse=True)

print(sum(elf_cals[:3], 0))
