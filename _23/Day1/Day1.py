with open("_23/Day1/Day1.txt", "r") as file:
    lines = [line.strip() for line in file]
    
numbers = {"one"  : 1,
           "two"  : 2,
           "three": 3,
           "four" : 4,
           "five" : 5,
           "six"  : 6,
           "seven": 7,
           "eight": 8,
           "nine" : 9,
           "zero" : 0}

def find_num(index, line, p2):
    if p2:
        for i in range(2, 6):
            if line[index:index+i] in numbers:
                return numbers[line[index:index+i]]
    if line[index].isdigit():
        return int(line[index])

def solution(p2):
    result = 0
    for line in lines:
        nums = [x for x in [find_num(i, line, p2) for i in range(len(line))] if x is not None]
        result += 10*nums[0] + nums[-1]
    return result
            
print(solution(True))