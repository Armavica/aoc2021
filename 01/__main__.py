import numpy as np
from aoc2021 import lines

numbers = lines('i')
print(sum(numbers[1:] > numbers[:-1]))
print(sum(numbers[3:] > numbers[:-3]))

