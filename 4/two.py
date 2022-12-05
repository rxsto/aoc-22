input_file = open('input.txt', 'r')
lines = list(map(lambda x: x.strip(), input_file.readlines()))

count = 0

for line in lines:
  pairs = line.split(',')

  (x1, x2) = pairs[0].split('-')
  (y1, y2) = pairs[1].split('-')

  x1 = int(x1)
  x2 = int(x2)
  y1 = int(y1)
  y2 = int(y2)

  if (y1 <= x2 and y2 >= x1) or (x1 <= y2 and x2 >= y1):
    count += 1

print(count)
