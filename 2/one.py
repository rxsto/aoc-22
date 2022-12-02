input_file = open('input.txt', 'r')
lines = input_file.readlines()

# Rock 1 - A & X
# Paper 2 - B & Y
# Scissors 3 - C & Z

# Loss 0
# Tie 3
# Win 6

points = 0

point_dict = {
  'A X': 4, # 3 + 1
  'A Y': 8, # 6 + 2
  'A Z': 3, # 0 + 3
  'B X': 1, # 0 + 1
  'B Y': 5, # 3 + 2
  'B Z': 9, # 6 + 3
  'C X': 7, # 6 + 1
  'C Y': 2, # 0 + 2
  'C Z': 6, # 3 + 3
}

for line in lines:
  points += point_dict[line.strip()]

print(points)
