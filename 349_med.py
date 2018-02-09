import itertools
import math
from utils import check_progress

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def do_it(str_in):
    num_stacks, boxes = str_in.split(" ")
    boxes = [int(x) for x in boxes]
    print()
    print("Testing " + str(boxes) +", stacks of " + str(num_stacks))
    
    for p in itertools.permutations(boxes):
        for i in range(1,len(p)-1):
            for j in range(i+1, len(p)-1):
                if sum(p[:i]) == sum(p[i:j]) == sum(p[j:]):
                    return ("Found: \n" + "".join([str(x) for x in p[:i]]) + "\n" + "".join([str(x) for x in p[i:j]]) + "\n" + "".join([str(x) for x in p[j:]]))

print(do_it("3 912743471352"))
print(do_it("3 42137586"))
print(do_it("9 2"))
print(do_it("4 064876318535318"))