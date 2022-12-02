input_file = open('input.txt', 'r')
lines = input_file.readlines()

# Rock 1 - A
# Paper 2 - B
# Scissors 3 - C

# X - need to lose(0)
# Y - need to tie(3)
# Z - need to win(6)

# loss 0
# tie 3
# win 6

points = 0

point_dict = {
  'A X': 3, # lose(0) -> C(3)
  'A Y': 4, # tie(3) -> A(1)
  'A Z': 8, # win(6) -> B(2)
  'B X': 1, # lose(0) -> A(1)
  'B Y': 5, # tie(3) -> B(2)
  'B Z': 9, # win(6) -> C(3)
  'C X': 2, # lose(0) -> B(2)
  'C Y': 6, # tie(3) -> C(3)
  'C Z': 7, # win(6) -> A(1)
}

for line in lines:
  points += point_dict[line.strip()]

print(points)
