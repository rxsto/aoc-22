input_file = open('input.txt', 'r')
lines = input_file.readlines()

biggest = 0

acc = 0

for line in lines:
  if line == '\n':
    if (acc > biggest):
      biggest = acc
    acc = 0
  else:
    acc += int(line)

print(biggest)
