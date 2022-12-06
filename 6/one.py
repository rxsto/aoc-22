input_file = open('input.txt', 'r')
lines = list(map(lambda x: x.strip(), input_file.readlines()))

signal = lines[0]

buffer = list(signal[:4])

step = len(buffer) - 1

for char in signal[4:]:
  step += 1

  has_equal = False

  for i in range(0, len(buffer)):
    for j in range(0, len(buffer)):
      if i == j:
        continue

      if buffer[i] == buffer[j]:
        has_equal = True
  
  if has_equal:
    del buffer[0]
    buffer.append(char)
  else:
    break

print(step)
