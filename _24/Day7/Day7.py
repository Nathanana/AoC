from Shortcuts.all import *

inp = str_input(24, 7).split("\n")

inp = [[int(line.split(":")[0]), list(map(int, line.split(":")[1].split()))] for line in inp]
total = [0, 0]

def test(nums, goal, p2):
    stack = deque([(nums[0], 0)])
    while stack:
        current_sum, i = stack.pop()
        if current_sum == goal and i == len(nums) - 1:
            return goal
        if i + 1 < len(nums):
            next_num = nums[i + 1]
            stack.append((current_sum + next_num, i + 1))
            stack.append((current_sum * next_num, i + 1))
            if p2:
                stack.append((current_sum * 10 ** (floor(log10(next_num)) + 1) + next_num, i + 1))
    return 0
        
total[0] = sum(test(line[1], line[0], False) for line in inp)
total[1] = sum(test(line[1], line[0], True) for line in inp)

printTotal(total)